import os
import re
import uuid
import threading
from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from sqlalchemy import create_engine, text, Column, String, Integer, Float, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

PORT = int(os.environ.get("COMPANY_PORT", 8000))
DATABASE_URL = os.environ.get("DATABASE_URL", "")
COMPANY_SLUG = re.sub(r"[^a-z0-9_]", "_", os.environ.get("COMPANY_SLUG", "company").lower())

db_engine = None
SessionLocal = None

class Base(DeclarativeBase):
    pass

if DATABASE_URL:
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    db_engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        pool_size=2,
        max_overflow=3,
        pool_recycle=300,
        connect_args={"options": f"-csearch_path={COMPANY_SLUG},public"},
    )
    SessionLocal = sessionmaker(bind=db_engine)
    with db_engine.connect() as _conn:
        _conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{COMPANY_SLUG}"'))
        _conn.commit()

# ─── MODELS ───────────────────────────────────────────────────────
class Agent(Base):
    __tablename__ = "agents"
    __table_args__ = {"schema": COMPANY_SLUG}
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    status = Column(String, default="draft")
    type = Column(String, default="custom")
    tools = Column(Text, default="[]")
    knowledge = Column(Text, default="[]")
    lastDeployed = Column(DateTime, nullable=True)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Knowledge(Base):
    __tablename__ = "knowledge"
    __table_args__ = {"schema": COMPANY_SLUG}
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    source = Column(String, nullable=False)
    type = Column(String, default="doc")
    content = Column(Text, default="")
    lastUpdated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Deployment(Base):
    __tablename__ = "deployments"
    __table_args__ = {"schema": COMPANY_SLUG}
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    agentId = Column(String, ForeignKey(f"{COMPANY_SLUG}.agents.id"), nullable=False)
    status = Column(String, default="pending")
    startedAt = Column(DateTime, default=datetime.utcnow)
    endedAt = Column(DateTime, nullable=True)

class Subscription(Base):
    __tablename__ = "subscriptions"
    __table_args__ = {"schema": COMPANY_SLUG}
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_email = Column(String, nullable=False, index=True)
    plan = Column(String, nullable=False)
    status = Column(String, default="active")
    stripe_session_id = Column(String, nullable=True)
    stripe_customer_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

if db_engine:
    try:
        Base.metadata.create_all(db_engine)
    except Exception as _e:
        print(f"[{COMPANY_SLUG}] DB init warning: {_e}")

app = FastAPI(title="QL Agents API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── ENV VARS ──────────────────────────────────────────────────────
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_CONNECT_ID = os.environ.get("STRIPE_CONNECT_ID", "")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "")

AI_KEY = os.environ.get("DEEPSEEK_API_KEY", "") or os.environ.get("OPENAI_API_KEY", "")
AI_BASE = "https://api.deepseek.com/v1" if os.environ.get("DEEPSEEK_API_KEY") else "https://api.openai.com/v1"
AI_MODEL = "deepseek-chat" if os.environ.get("DEEPSEEK_API_KEY") else "gpt-4o-mini"

# ─── NANOCORP SYNC ────────────────────────────────────────────────
_NANOCORP_BASE = 'https://nanocorp.app'
_NANOCORP_CO = 'QL Agents'
_NANOCORP_TOKEN = 'f28b61589c2beecee1debd3875e78e79'

def _nanocorp_sync(db):
    import datetime
    try:
        import requests as _req
    except ImportError:
        return
    try:
        User = next((m.class_ for m in db._mapper_registry.mappers if m.class_.__name__ in ('User','AppUser','Account','Member','Customer')), None)
        Lead = None
        Order = next((m.class_ for m in db._mapper_registry.mappers if m.class_.__name__ in ('Subscription',)), None)
        def _safe(obj, *keys):
            for k in keys:
                v = getattr(obj, k, None)
                if v is not None: return v
            return ''
        customers = []
        if User:
            for u in db.query(User).all():
                customers.append({'id': str(_safe(u,'id')), 'email': str(_safe(u,'email')),
                    'name': str(_safe(u,'name','full_name','')), 'plan': str(_safe(u,'plan','tier','subscription','free')),
                    'mrr': float(_safe(u,'mrr','monthly_revenue') or 0),
                    'created_at': str(_safe(u,'created_at','joined_at','registered_at'))})
        orders = []
        if Order:
            for o in db.query(Order).all():
                orders.append({'id': str(_safe(o,'id')), 'customer_email': str(_safe(o,'user_email','email','')),
                    'product': str(_safe(o,'plan','product_name','')), 'amount': 0,
                    'created_at': str(_safe(o,'created_at'))})
        total_mrr = sum(float(c.get('mrr',0)) for c in customers)
        metrics = {'total_users': len(customers), 'mrr': total_mrr, 'arr': total_mrr*12,
                   'active_today': 0, 'churn_rate': 0}
        _req.post(f'{_NANOCORP_BASE}/api/company/{_NANOCORP_CO}/sync',
            json={'customers': customers, 'leads': [], 'orders': orders, 'metrics': metrics},
            headers={'Authorization': f'Bearer {_NANOCORP_TOKEN}', 'Content-Type': 'application/json'},
            timeout=6)
    except Exception:
        pass

def _sync_async(db):
    t = threading.Thread(target=_nanocorp_sync, args=(db,), daemon=True)
    t.start()

# ─── Pydantic Schemas ─────────────────────────────────────────────
class AgentCreate(BaseModel):
    name: str
    type: str = "custom"
    tools: List[str] = []
    knowledge: List[str] = []

class AgentUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    tools: Optional[List[str]] = None
    knowledge: Optional[List[str]] = None

class DeploymentCreate(BaseModel):
    agentId: str

class CheckoutRequest(BaseModel):
    plan: str
    user_email: str
    success_url: str = "https://example.com/success"
    cancel_url: str = "https://example.com/cancel"

class AIRequest(BaseModel):
    prompt: str

# ─── Pricing Tiers ────────────────────────────────────────────────
PRICING_TIERS = {
    "starter": {"name": "Starter", "amount": 49900, "interval": "month", "description": "1 tailored agent, 5 knowledge sources, basic analytics"},
    "growth": {"name": "Growth", "amount": 149900, "interval": "month", "description": "5 tailored agents, 20 knowledge sources, advanced analytics"},
    "enterprise": {"name": "Enterprise", "amount": None, "interval": "month", "description": "Unlimited agents, dedicated support, custom integrations"}
}

# ─── Helper ────────────────────────────────────────────────────────
def get_db():
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        yield db

def parse_tools(tools_str: Optional[str]) -> List[str]:
    if not tools_str:
        return []
    try:
        import json
        return json.loads(tools_str)
    except:
        return []

def parse_knowledge(knowledge_str: Optional[str]) -> List[str]:
    if not knowledge_str:
        return []
    try:
        import json
        return json.loads(knowledge_str)
    except:
        return []

# ─── LIFESPAN ──────────────────────────────────────────────────────
@app.on_event("startup")
async def startup_event():
    if SessionLocal:
        with SessionLocal() as db:
            _sync_async(db)

# ─── HEALTH & INFO ─────────────────────────────────────────────────
@app.get("/health")
def health():
    return {"status": "ok", "schema": COMPANY_SLUG, "db": bool(db_engine)}

@app.get("/api/info")
def company_info():
    return {
        "name": "QL Agents",
        "tagline": "Develop highly tailored agents to companies and leaders requiring specialized knowledge and tools.",
        "founded": 2024,
        "team_size": 10,
        "pricing": [
            {"plan": "Starter", "price": 499, "description": "1 tailored agent, 5 knowledge sources, basic analytics"},
            {"plan": "Growth", "price": 1499, "description": "5 tailored agents, 20 knowledge sources, advanced analytics"},
            {"plan": "Enterprise", "price": "Custom", "description": "Unlimited agents, dedicated support, custom integrations"}
        ]
    }

# ─── METRICS ───────────────────────────────────────────────────────
@app.get("/api/metrics")
def get_metrics():
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        agent_count = db.query(Agent).count()
        deployment_count = db.query(Deployment).count()
        active_deployments = db.query(Deployment).filter(Deployment.status == "active").count()
        knowledge_count = db.query(Knowledge).count()
        
        return [{
            "deployments": deployment_count,
            "timeSaved": deployment_count * 8,  # assume 8 hours saved per deployment
            "usage": agent_count * 100 if agent_count > 0 else 0
        }]

# ─── AGENTS ────────────────────────────────────────────────────────
@app.get("/api/agents")
def list_agents():
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        agents = db.query(Agent).all()
        return [{
            "id": a.id,
            "name": a.name,
            "status": a.status,
            "type": a.type,
            "lastDeployed": a.lastDeployed.isoformat() if a.lastDeployed else None
        } for a in agents]

@app.post("/api/agents")
def create_agent(body: AgentCreate):
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        import json
        agent = Agent(
            id=str(uuid.uuid4()),
            name=body.name,
            type=body.type,
            status="draft",
            tools=json.dumps(body.tools),
            knowledge=json.dumps(body.knowledge),
            createdAt=datetime.utcnow()
        )
        db.add(agent)
        db.commit()
        db.refresh(agent)
        return {
            "id": agent.id,
            "name": agent.name,
            "status": agent.status,
            "type": agent.type,
            "createdAt": agent.createdAt.isoformat()
        }

@app.get("/api/agents/{agent_id}")
def get_agent(agent_id: str):
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        agent = db.query(Agent).filter(Agent.id == agent_id).first()
        if not agent:
            raise HTTPException(404, "Agent not found")
        
        deployments = db.query(Deployment).filter(Deployment.agentId == agent_id).all()
        deployment_history = [{
            "id": d.id,
            "status": d.status,
            "startedAt": d.startedAt.isoformat() if d.startedAt else None,
            "endedAt": d.endedAt.isoformat() if d.endedAt else None
        } for d in deployments]
        
        return {
            "id": agent.id,
            "name": agent.name,
            "type": agent.type,
            "tools": parse_tools(agent.tools),
            "knowledge": parse_knowledge(agent.knowledge),
            "deploymentHistory": deployment_history
        }

@app.put("/api/agents/{agent_id}")
def update_agent(agent_id: str, body: AgentUpdate):
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        agent = db.query(Agent).filter(Agent.id == agent_id).first()
        if not agent:
            raise HTTPException(404, "Agent not found")
        
        import json
        if body.name is not None:
            agent.name = body.name
        if body.type is not None:
            agent.type = body.type
        if body.tools is not None:
            agent.tools = json.dumps(body.tools)
        if body.knowledge is not None:
            agent.knowledge = json.dumps(body.knowledge)
        
        agent.updatedAt = datetime.utcnow()
        db.commit()
        db.refresh(agent)
        return {
            "id": agent.id,
            "name": agent.name,
            "type": agent.type,
            "tools": parse_tools(agent.tools),
            "knowledge": parse_knowledge(agent.knowledge),
            "updatedAt": agent.updatedAt.isoformat()
        }

@app.delete("/api/agents/{agent_id}")
def delete_agent(agent_id: str):
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        agent = db.query(Agent).filter(Agent.id == agent_id).first()
        if not agent:
            raise HTTPException(404, "Agent not found")
        db.delete(agent)
        db.commit()
        return {"deleted": True}

# ─── KNOWLEDGE ─────────────────────────────────────────────────────
@app.get("/api/knowledge")
def list_knowledge():
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        knowledge = db.query(Knowledge).all()
        return [{
            "id": k.id,
            "source": k.source,
            "type": k.type,
            "lastUpdated": k.lastUpdated.isoformat() if k.lastUpdated else None
        } for k in knowledge]

# ─── DEPLOYMENTS ───────────────────────────────────────────────────
@app.post("/api/deployments")
def create_deployment(body: DeploymentCreate):
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        agent = db.query(Agent).filter(Agent.id == body.agentId).first()
        if not agent:
            raise HTTPException(404, "Agent not found")
        
        deployment = Deployment(
            id=str(uuid.uuid4()),
            agentId=body.agentId,
            status="deploying",
            startedAt=datetime.utcnow()
        )
        db.add(deployment)
        agent.status = "deployed"
        agent.lastDeployed = datetime.utcnow()
        db.commit()
        db.refresh(deployment)
        _sync_async(db)
        return {
            "id": deployment.id,
            "agentId": deployment.agentId,
            "status": deployment.status,
            "startedAt": deployment.startedAt.isoformat(),
            "endedAt": None
        }

# ─── STRIPE PAYMENTS ───────────────────────────────────────────────
@app.post("/api/checkout")
def create_checkout(body: CheckoutRequest):
    if not STRIPE_SECRET_KEY:
        return {"error": "Payments not configured"}, 503
    if body.plan not in PRICING_TIERS:
        raise HTTPException(400, "Invalid plan")
    
    import stripe
    stripe.api_key = STRIPE_SECRET_KEY
    
    tier = PRICING_TIERS[body.plan]
    if tier["amount"] is None:
        # Enterprise - custom
        raise HTTPException(400, "Contact sales for enterprise pricing")
    
    try:
        session = stripe.checkout.Session.create(
            mode="subscription",
            customer_email=body.user_email,
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "unit_amount": tier["amount"],
                    "recurring": {"interval": "month"},
                    "product_data": {
                        "name": f"QL Agents {tier['name']} Plan"
                    }
                },
                "quantity": 1,
            }],
            success_url=body.success_url,
            cancel_url=body.cancel_url,
            metadata={"plan": body.plan, "user_email": body.user_email}
        )
        
        # Add Connect destination charge if configured
        if STRIPE_CONNECT_ID:
            session = stripe.checkout.Session.create(
                mode="subscription",
                customer_email=body.user_email,
                line_items=[{
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": tier["amount"],
                        "recurring": {"interval": "month"},
                        "product_data": {
                            "name": f"QL Agents {tier['name']} Plan"
                        }
                    },
                    "quantity": 1,
                }],
                success_url=body.success_url,
                cancel_url=body.cancel_url,
                payment_intent_data={
                    "application_fee_amount": int(tier["amount"] * 0.1),
                    "transfer_data": {"destination": STRIPE_CONNECT_ID}
                },
                metadata={"plan": body.plan, "user_email": body.user_email}
            )
        
        return {"checkout_url": session.url}
    except Exception as e:
        raise HTTPException(400, f"Stripe error: {str(e)}")

@app.post("/api/webhook")
async def stripe_webhook(request: Request):
    if not STRIPE_SECRET_KEY or not STRIPE_WEBHOOK_SECRET:
        return {"status": "ok"}
    
    import stripe
    stripe.api_key = STRIPE_SECRET_KEY
    
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_WEBHOOK_SECRET)
    except ValueError:
        raise HTTPException(400, "Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(400, "Invalid signature")
    
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        plan = session.get("metadata", {}).get("plan", "starter")
        email = session.get("metadata", {}).get("user_email") or session.get("customer_email", "")
        
        if SessionLocal:
            with SessionLocal() as db:
                sub = Subscription(
                    id=str(uuid.uuid4()),
                    user_email=email,
                    plan=plan,
                    status="active",
                    stripe_session_id=session.get("id"),
                    stripe_customer_id=session.get("customer")
                )
                db.add(sub)
                db.commit()
                _sync_async(db)
    
    return {"status": "ok"}

@app.get("/api/subscription")
def get_subscription(email: str):
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        sub = db.query(Subscription).filter(
            Subscription.user_email == email,
            Subscription.status == "active"
        ).first()
        if sub:
            return {"plan": sub.plan, "status": "active"}
        return {"plan": "free", "status": "none"}

@app.post("/api/portal")
def create_portal(body: dict):
    if not STRIPE_SECRET_KEY:
        return {"error": "Payments not configured"}, 503
    
    import stripe
    stripe.api_key = STRIPE_SECRET_KEY
    
    try:
        session = stripe.billing_portal.Session.create(
            customer=body.get("customer_id")
        )
        return {"portal_url": session.url}
    except Exception as e:
        raise HTTPException(400, f"Stripe error: {str(e)}")

# ─── AI ENDPOINTS ──────────────────────────────────────────────────
@app.post("/api/ai/complete")
def ai_complete(body: AIRequest):
    if not AI_KEY:
        raise HTTPException(503, "AI not configured — add DEEPSEEK_API_KEY or OPENAI_API_KEY in the platform's Env Vars panel (the 🔐 button)")
    import requests as _rq
    r = _rq.post(
        f"{AI_BASE}/chat/completions",
        headers={"Authorization": f"Bearer {AI_KEY}"},
        json={"model": AI_MODEL, "messages": [{"role": "user", "content": body.prompt}]},
        timeout=60
    )
    r.raise_for_status()
    return {"text": r.json()["choices"][0]["message"]["content"]}

# ─── EXTRA SAAS DASHBOARD ENDPOINTS ────────────────────────────────
@app.get("/api/stats")
def get_stats():
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        agents = db.query(Agent).count()
        deployments = db.query(Deployment).count()
        knowledge = db.query(Knowledge).count()
        return {
            "agents": agents,
            "deployments": deployments,
            "knowledge_sources": knowledge,
            "active_agents": db.query(Agent).filter(Agent.status == "active").count()
        }

@app.get("/api/recent-activity")
def get_recent_activity():
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        deployments = db.query(Deployment).order_by(Deployment.startedAt.desc()).limit(10).all()
        return [{
            "id": d.id,
            "agentId": d.agentId,
            "status": d.status,
            "startedAt": d.startedAt.isoformat() if d.startedAt else None,
            "endedAt": d.endedAt.isoformat() if d.endedAt else None
        } for d in deployments]

@app.get("/api/chart-data")
def get_chart_data():
    if not SessionLocal:
        raise HTTPException(503, "DB not available")
    with SessionLocal() as db:
        deployments = db.query(Deployment).all()
        # Simple stats
        return {
            "total_deployments": len(deployments),
            "successful": len([d for d in deployments if d.status == "active"]),
            "failed": len([d for d in deployments if d.status == "failed"]),
            "pending": len([d for d in deployments if d.status == "deploying"])
        }

# ─── AUTO-MIGRATE (injected): add model columns create_all can't ────────────
def _nc_auto_migrate():
    if not db_engine:
        return
    try:
        from sqlalchemy import inspect as _sa_inspect, text as _sa_text
        if db_engine.dialect.name != "postgresql":
            return
        _insp = _sa_inspect(db_engine)
        with db_engine.connect() as _mc:
            for _tbl in Base.metadata.sorted_tables:
                _sch = _tbl.schema or "public"
                try:
                    if not _insp.has_table(_tbl.name, schema=_sch):
                        continue  # create_all creates brand-new tables whole
                    _have = {_c["name"] for _c in _insp.get_columns(_tbl.name, schema=_sch)}
                except Exception:
                    continue
                for _col in _tbl.columns:
                    if _col.name in _have:
                        continue
                    try:
                        _ddl = _col.type.compile(db_engine.dialect)
                        _mc.execute(_sa_text(
                            f'ALTER TABLE "{_sch}"."{_tbl.name}" '
                            f'ADD COLUMN IF NOT EXISTS "{_col.name}" {_ddl}'
                        ))
                        _mc.commit()
                        print(f"[DB] migrated: added {_tbl.name}.{_col.name} ({_ddl})", flush=True)
                    except Exception as _col_e:
                        print(f"[DB] migrate skip {_tbl.name}.{_col.name}: {_col_e}", flush=True)
    except Exception as _mig_e:
        print(f"[DB] auto-migrate warning: {_mig_e}", flush=True)

_nc_auto_migrate()
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)