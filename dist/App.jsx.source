import { Activity, ChevronDown, Clock, Database, FileText, Plus, Send, Trash2, Users, X } from 'lucide-react';
import { useEffect, useState } from 'react';

const LOGO = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3MiIgaGVpZ2h0PSI3MiIgdmlld0JveD0iMCAwIDcyIDcyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCIgeTE9IjAiIHgyPSI3MiIgeTI9IjcyIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agc3RvcC1jb2xvcj0iI0Y2QjUzRCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iI0RGODUyMyIvPjwvbGluZWFyR3JhZGllbnQ+PC9kZWZzPjxyZWN0IHdpZHRoPSI3MiIgaGVpZ2h0PSI3MiIgcng9IjE2IiBmaWxsPSJ1cmwoI2JnKSIvPjx0ZXh0IHg9IjM2IiB5PSI0NiIgZm9udC1mYW1pbHk9IkFyaWFsLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMzgiIGZvbnQtd2VpZ2h0PSI5MDAiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkE8L3RleHQ+PC9zdmc+';

const COLORS = {
  primary: '#F6B53D',
  primaryDark: '#DF8523',
  primaryBg: 'rgba(246,181,61,0.12)',
  primaryBorder: 'rgba(246,181,61,0.45)',
  navy: '#0A1F44',
  navyDark: '#071A35',
  navyLight: '#123A6B',
  textLight: '#A8C3E2',
  textMuted: '#6A87A8',
  textBody: '#33475B',
  bgLight: '#FFF8ED'
};

function LandingPage({ onGetStarted, onLogin }) {
  const [mobileOpen, setMobileOpen] = useState(false);
  const [hoveredFeature, setHoveredFeature] = useState(null);

  const features = [
    { title: 'Custom Agent Architecture', desc: 'We design agents around your specific workflows, data, and decision processes — not generic templates.' },
    { title: 'Expert Knowledge Injection', desc: 'Train agents with your proprietary documents, proprietary tools, and industry-specific expertise.' },
    { title: 'Enterprise-Grade Security', desc: 'SOC 2 compliant, encrypted by default, and permission-controlled at every layer of interaction.' },
    { title: 'Continuous Evolution', desc: 'Our agents learn from each interaction, refining their responses and accuracy over time.' },
    { title: 'Integrate Anything', desc: 'Connect to your CRM, ERP, and internal tools so your agents operate where your work actually happens.' },
    { title: 'Dedicated Success Team', desc: 'Work alongside our specialists to ensure your agent hits every goal you set.' }
  ];

  const stats = [
    { value: '90%', label: 'Time saved on repetitive tasks' },
    { value: '12+', label: 'Industries served' },
    { value: '24/7', label: 'Agent availability' }
  ];

  const pricing = [
    { name: 'Explorer', price: '$499/mo', features: ['Single custom agent', '2 integrations', 'Weekly optimization', 'Email support'] },
    { name: 'Scale', price: '$1,499/mo', features: ['3 custom agents', 'Unlimited integrations', 'Daily optimization', 'Priority support'] },
    { name: 'Enterprise', price: 'Custom', features: ['Unlimited agents', 'SLA & compliance', 'Dedicated engineer', '24/7 white-glove support'] }
  ];

  return (
    <div style={{ backgroundColor: COLORS.bgLight, minHeight: '100vh', fontFamily: 'system-ui, -apple-system, sans-serif', color: COLORS.navy }}>
      {/* NAV */}
      <nav style={{ backgroundColor: COLORS.navy, padding: '0 24px', height: 72, display: 'flex', alignItems: 'center', justifyContent: 'space-between', position: 'sticky', top: 0, zIndex: 100, boxShadow: '0 2px 12px rgba(10,31,68,0.15)' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12, cursor: 'pointer' }}>
          <img src={LOGO} alt="QL Agents" style={{ width: 36, height: 36, borderRadius: 10 }} />
          <span style={{ color: '#fff', fontSize: 22, fontWeight: 700, letterSpacing: '-0.5px' }}>QL Agents</span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 28, fontSize: 15, fontWeight: 500 }}>
          <span style={{ color: COLORS.textLight, cursor: 'pointer', transition: 'color 0.2s' }} onMouseEnter={e => e.target.style.color = COLORS.primary} onMouseLeave={e => e.target.style.color = COLORS.textLight}>How it works</span>
          <span style={{ color: COLORS.textLight, cursor: 'pointer', transition: 'color 0.2s' }} onMouseEnter={e => e.target.style.color = COLORS.primary} onMouseLeave={e => e.target.style.color = COLORS.textLight}>Pricing</span>
          <span style={{ color: COLORS.textLight, cursor: 'pointer', transition: 'color 0.2s' }} onMouseEnter={e => e.target.style.color = COLORS.primary} onMouseLeave={e => e.target.style.color = COLORS.textLight}>Contact</span>
          <button onClick={onLogin} style={{ color: COLORS.primary, backgroundColor: 'transparent', border: `1px solid ${COLORS.primary}`, padding: '8px 20px', borderRadius: 8, fontWeight: 600, cursor: 'pointer', transition: 'all 0.2s', fontSize: 14 }} 
            onMouseEnter={e => { e.target.style.backgroundColor = COLORS.primary; e.target.style.color = COLORS.navy; }}
            onMouseLeave={e => { e.target.style.backgroundColor = 'transparent'; e.target.style.color = COLORS.primary; }}>
            Sign in
          </button>
          <button onClick={onGetStarted} style={{ backgroundColor: COLORS.primary, color: COLORS.navy, border: 'none', padding: '10px 24px', borderRadius: 8, fontWeight: 700, cursor: 'pointer', transition: 'all 0.2s' }}
            onMouseEnter={e => { e.target.style.transform = 'scale(1.04)'; e.target.style.boxShadow = `0 4px 20px ${COLORS.primaryBorder}`; }}
            onMouseLeave={e => { e.target.style.transform = 'scale(1)'; e.target.style.boxShadow = 'none'; }}>
            Get started
          </button>
        </div>
      </nav>

      {/* HERO */}
      <header style={{ background: `linear-gradient(135deg, ${COLORS.navy} 0%, ${COLORS.navyLight} 50%, ${COLORS.primaryDark} 100%)`, padding: '120px 24px 140px', textAlign: 'center', position: 'relative', overflow: 'hidden' }}>
        <div style={{ position: 'absolute', inset: 0, opacity: 0.05, backgroundImage: `radial-gradient(circle at 25% 50%, ${COLORS.primary} 0%, transparent 30%), radial-gradient(circle at 75% 30%, ${COLORS.primary} 0%, transparent 30%)` }} />
        <div style={{ maxWidth: 800, margin: '0 auto', position: 'relative' }}>
          <img src={LOGO} alt="QL Agents" style={{ width: 72, height: 72, borderRadius: 16, marginBottom: 8 }} />
          <div style={{ display: 'inline-block', backgroundColor: COLORS.primaryBg, padding: '8px 20px', borderRadius: 30, color: COLORS.primary, fontWeight: 600, fontSize: 14, marginBottom: 24, letterSpacing: '0.5px' }}>
            Tailored AI agents for your operation
          </div>
          <h1 style={{ fontSize: '3.5rem', margin: '0 0 20px', lineHeight: 1.15, color: '#fff', fontWeight: 800, letterSpacing: '1px' }}>
            AI agents crafted for your{' '}
            <span style={{ background: `linear-gradient(90deg, ${COLORS.primary}, #FFD57E, ${COLORS.primary})`, backgroundSize: '200% auto', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent', animation: 'gradientMove 4s ease infinite' }}>
              exact business
            </span>
          </h1>
          <p style={{ fontSize: '1.25rem', color: COLORS.textLight, maxWidth: 600, margin: '0 auto 40px', lineHeight: 1.7, fontWeight: 300 }}>
            Custom-built AI agents with specialized knowledge, tools, and training to work like an expert in your field — from day one.
          </p>
          <div style={{ display: 'flex', gap: 16, justifyContent: 'center', flexWrap: 'wrap' }}>
            <button onClick={onGetStarted} style={{ backgroundColor: COLORS.primary, color: COLORS.navy, border: 'none', padding: '16px 40px', borderRadius: 10, fontWeight: 700, fontSize: 16, cursor: 'pointer', transition: 'all 0.2s', display: 'flex', alignItems: 'center', gap: 10 }}
              onMouseEnter={e => { e.target.style.transform = 'translateY(-2px)'; e.target.style.boxShadow = `0 8px 30px ${COLORS.primaryBorder}`; }}
              onMouseLeave={e => { e.target.style.transform = 'translateY(0)'; e.target.style.boxShadow = 'none'; }}>
              → Build my agent
            </button>
            <button onClick={onLogin} style={{ backgroundColor: 'transparent', color: '#fff', border: `1px solid ${COLORS.primary}`, padding: '16px 40px', borderRadius: 10, fontWeight: 600, fontSize: 16, cursor: 'pointer', transition: 'all 0.2s' }}
              onMouseEnter={e => { e.target.style.borderColor = COLORS.primary; e.target.style.color = COLORS.primary; }}
              onMouseLeave={e => { e.target.style.borderColor = COLORS.primary; e.target.style.color = '#fff'; }}>
              See how it works
            </button>
          </div>
          <div style={{ display: 'flex', gap: 48, justifyContent: 'center', marginTop: 50, flexWrap: 'wrap' }}>
            {(stats || []).map(s => (
              <div key={s.label} style={{ textAlign: 'center' }}>
                <div style={{ fontSize: '2.5rem', fontWeight: 800, color: COLORS.primary }}>{s.value}</div>
                <div style={{ fontSize: '0.9rem', color: COLORS.textLight, marginTop: 4 }}>{s.label}</div>
              </div>
            ))}
          </div>
        </div>
      </header>

      {/* HOW IT WORKS */}
      <section style={{ padding: '90px 24px', margin: '0 auto', maxWidth: 1100 }}>
        <div style={{ maxWidth: 600, marginBottom: 60 }}>
          <h2 style={{ fontSize: '2.5rem', color: COLORS.navy, margin: '0 0 16px', fontWeight: 800 }}>Purpose-built intelligence</h2>
          <p style={{ color: COLORS.textBody, fontSize: '1.1rem', lineHeight: 1.7 }}>Your agents are not off-the-shelf. They're built with your knowledge, your tools, your goals — and polished through live optimization.</p>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 20 }}>
          {(features || []).map((f, i) => (
            <div key={f.title} onMouseEnter={() => setHoveredFeature(i)} onMouseLeave={() => setHoveredFeature(null)} style={{ backgroundColor: hoveredFeature === i ? '#fff' : '#FFFFFF', border: `1px solid ${COLORS.primaryBorder}`, borderRadius: 16, padding: 28, transition: 'all 0.25s, transform 0.2s', transform: hoveredFeature === i ? 'translateY(-4px)' : 'translateY(0)', boxShadow: hoveredFeature === i ? `0 10px 40px ${COLORS.primaryBorder}` : '0 2px 8px rgba(10,31,68,0.04)' }}>
              <div style={{ fontSize: '1.6rem', marginBottom: 14, fontWeight: 800, color: COLORS.primary, background: COLORS.primaryBg, width: 48, height: 48, display: 'flex', alignItems: 'center', justifyContent: 'center', borderRadius: 12, padding: 8 }}>{i + 1}</div>
              <h3 style={{ fontSize: '1.1rem', color: COLORS.navy, margin: '0 0 10px', fontWeight: 700 }}>{f.title}</h3>
              <p style={{ color: COLORS.textBody, fontSize: '0.95rem', lineHeight: 1.6, margin: 0 }}>{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* PRICING */}
      <section style={{ backgroundColor: COLORS.navy, padding: '90px 24px', margin: '0 auto' }}>
        <div style={{ maxWidth: 1100, margin: '0 auto' }}>
          <div style={{ maxWidth: 600, marginBottom: 60 }}>
            <h2 style={{ fontSize: '2.5rem', color: '#fff', margin: '0 0 16px', fontWeight: 800 }}>Simple plans, clear value</h2>
            <p style={{ color: COLORS.textLight, fontSize: '1.1rem', lineHeight: 1.7 }}>Start small, scale with your needs. Every plan includes hands-on setup so your agent is live in days, not months.</p>
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 24 }}>
            {(pricing || []).map((p, idx) => (
              <div key={p.name} style={{ backgroundColor: idx === 1 ? COLORS.primary : COLORS.navyLight, padding: 32, borderRadius: 16, border: idx === 1 ? 'none' : '1px solid #234A79', position: 'relative', display: 'flex', flexDirection: 'column' }}>
                {idx === 1 && <div style={{ position: 'absolute', top: -14, left: '50%', transform: 'translateX(-50%)', backgroundColor: COLORS.navy, color: COLORS.primary, padding: '4px 14px', borderRadius: 20, fontSize: 12, fontWeight: 700 }}>Most popular</div>}
                <h3 style={{ fontSize: '1.2rem', margin: '0 0 6px', color: idx === 1 ? COLORS.navy : '#fff', fontWeight: 700 }}>{p.name}</h3>
                <div style={{ fontSize: '2rem', fontWeight: 800, color: idx === 1 ? COLORS.navy : COLORS.primary, marginBottom: 20 }}>{p.price}</div>
                <ul style={{ listStyle: 'none', padding: 0, margin: '0 0 28px', flex: 1 }}>
                  {p.features.map(f => (
                    <li key={f} style={{ padding: '8px 0', color: idx === 1 ? COLORS.navy : COLORS.textLight, fontSize: '0.95rem', borderBottom: '1px solid rgba(255,255,255,0.1)' }}>✓ {f}</li>
                  ))}
                </ul>
                <button onClick={onGetStarted} style={{ padding: '14px', borderRadius: 8, border: 'none', cursor: 'pointer', fontWeight: 700, fontSize: 14, backgroundColor: idx === 1 ? COLORS.navy : 'transparent', color: idx === 1 ? '#fff' : COLORS.primary, border: idx === 1 ? 'none' : `1px solid ${COLORS.primary}`, transition: 'all 0.2s' }}>
                  {idx === 2 ? 'Contact sales' : 'Get started'}
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section style={{ padding: '100px 24px', textAlign: 'center', background: `linear-gradient(180deg, ${COLORS.bgLight} 0%, #FBEED9 100%)` }}>
        <div style={{ maxWidth: 700, margin: '0 auto' }}>
          <img src={LOGO} alt="QL Agents" style={{ width: 56, height: 56, borderRadius: 12, marginBottom: 20 }} />
          <h2 style={{ fontSize: '2.4rem', fontWeight: 800, color: COLORS.navy, margin: '0 0 20px' }}>Ready for an agent that works like an expert in your field?</h2>
          <p style={{ color: COLORS.textBody, fontSize: '1.15rem', marginBottom: 36, lineHeight: 1.6 }}>Tell us about your business — we'll show you exactly how a tailored QL Agent can transform your team's productivity.</p>
          <div style={{ display: 'flex', gap: 16, justifyContent: 'center', flexWrap: 'wrap' }}>
            <button onClick={onGetStarted} style={{ backgroundColor: COLORS.primary, color: COLORS.navy, padding: '16px 40px', borderRadius: 10, border: 'none', fontWeight: 800, fontSize: 16, cursor: 'pointer', transition: 'all 0.2s' }}
              onMouseEnter={e => { e.target.style.boxShadow = `0 8px 30px ${COLORS.primaryBorder}`; e.target.style.transform = 'translateY(-2px)'; }}
              onMouseLeave={e => { e.target.style.boxShadow = 'none'; e.target.style.transform = 'translateY(0)'; }}>
              → Build my agent
            </button>
            <button onClick={onLogin} style={{ backgroundColor: 'transparent', color: COLORS.navy, border: `1px solid ${COLORS.navy}`, padding: '16px 40px', borderRadius: 10, fontWeight: 600, fontSize: 16, cursor: 'pointer', transition: 'all 0.2s' }}>
              Already a client — log in
            </button>
          </div>
        </div>
      </section>

      {/* FOOTER */}
      <footer style={{ backgroundColor: COLORS.navy, borderTop: `1px solid ${COLORS.navyLight}`, padding: '50px 24px 30px' }}>
        <div style={{ maxWidth: 1100, margin: '0 auto', display: 'flex', flexDirection: 'column', gap: 20 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 12, justifyContent: 'space-between' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
              <img src={LOGO} alt="QL Agents" style={{ width: 32, height: 32, borderRadius: 8 }} />
              <span style={{ color: '#fff', fontWeight: 600, fontSize: 18 }}>QL Agents</span>
            </div>
            <div style={{ display: 'flex', gap: 24 }}>
              <span style={{ color: COLORS.textLight, fontSize: 14, cursor: 'pointer' }}>Privacy</span>
              <span style={{ color: COLORS.textLight, fontSize: 14, cursor: 'pointer' }}>Terms</span>
              <span style={{ color: COLORS.textLight, fontSize: 14, cursor: 'pointer' }}>Contact</span>
            </div>
          </div>
          <div style={{ color: COLORS.textMuted, fontSize: 13 }}>© 2025 QL Agents. AI built for your business. All rights reserved.</div>
        </div>
      </footer>

      <style>{`
        @keyframes gradientMove {
          0% { background-position: 0% 50%; }
          50% { background-position: 100% 50%; }
          100% { background-position: 0% 50%; }
        }
        @media (max-width: 768px) {
          h1 { font-size: 2.5rem !important; }
          nav > div:last-child { display: none !important; }
        }
      `}</style>
    </div>
  );
}

function HighlyTailoredAgentsSection({ user }) {
  const [metrics, setMetrics] = useState([]);
  const [agents, setAgents] = useState([]);
  const [knowledge, setKnowledge] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [showCreate, setShowCreate] = useState(false);
  const [newAgent, setNewAgent] = useState({ name: '', type: 'general' });

  useEffect(() => {
    let isMounted = true;
    async function fetchAll() {
      setLoading(true);
      setError('');
      const [metricsData, agentsData, knowledgeData] = await Promise.all([
        apiFetch('/api/metrics'),
        apiFetch('/api/agents'),
        apiFetch('/api/knowledge')
      ]);
      if (!isMounted) return;
      setMetrics(Array.isArray(metricsData) ? metricsData : (metricsData?.items ?? []));
      setAgents(Array.isArray(agentsData) ? agentsData : (agentsData?.items ?? []));
      setKnowledge(Array.isArray(knowledgeData) ? knowledgeData : (knowledgeData?.items ?? []));
      setLoading(false);
      if (!metricsData && !agentsData && !knowledgeData) setError('Unable to load data — check your connection.');
    }
    fetchAll();
    return () => { isMounted = false; };
  }, []);

  const createAgent = async (e) => {
    e.preventDefault();
    if (!newAgent.name.trim()) return;
    const created = await apiFetch('/api/agents', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: newAgent.name, type: newAgent.type })
    });
    if (created) {
      const fresh = await apiFetch('/api/agents');
      setAgents(Array.isArray(fresh) ? fresh : (fresh?.items ?? []));
      setShowCreate(false);
      setNewAgent({ name: '', type: 'general' });
    }
  };

  const toggleDeploy = async (agent) => {
    if (agent.status !== 'deployed') {
      await apiFetch('/api/deployments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ agentId: agent.id })
      });
      const fresh = await apiFetch('/api/agents');
      setAgents(Array.isArray(fresh) ? fresh : (fresh?.items ?? []));
    }
  };

  const selectAgent = async (agent) => {
    if (selected !== agent.id) {
      setSelected(agent.id);
      const detail = await apiFetch(`/api/agents/${agent.id}`);
      if (detail) setAgentDetail(detail);
    } else {
      setSelected(null);
      setAgentDetail(null);
    }
  };

  const [selected, setSelected] = useState(null);
  const [agentDetail, setAgentDetail] = useState(null);

  return (
    <section className="p-6 space-y-6">
      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700 flex items-center justify-between">
          <span>{error}</span>
          <button onClick={() => window.location.reload()} className="text-red-600 hover:text-red-800 font-medium text-sm">Retry</button>
        </div>
      )}

      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h2 className="text-2xl font-bold text-[#0A1F44]">Highly Tailored Agents</h2>
          <p className="text-[#0A1F44]/60 mt-1">Mission-focused deployment with specialized knowledge and custom tools</p>
        </div>
        <button
          onClick={() => setShowCreate(!showCreate)}
          className="bg-[#00B4D8] hover:bg-[#00B4D8]/90 text-white px-4 py-2 rounded-lg transition-colors duration-200 flex items-center gap-2"
        >
          {showCreate ? 'Cancel' : <><Plus size={16} /> New Agent</>}
        </button>
      </div>

      {showCreate && (
        <form onSubmit={createAgent} className="bg-[#0A1F44]/5 border border-[#0A1F44]/10 rounded-lg p-4 flex flex-col md:flex-row gap-3">
          <input
            value={newAgent.name}
            onChange={(e) => setNewAgent({ ...newAgent, name: e.target.value })}
            placeholder="Agent name (e.g. Executive Analysis Agent)"
            className="flex-1 px-3 py-2 rounded-lg border border-[#0A1F44]/20 bg-white focus:outline-none focus:ring-2 focus:ring-[#00B4D8]"
          />
          <select
            value={newAgent.type}
            onChange={(e) => setNewAgent({ ...newAgent, type: e.target.value })}
            className="px-3 py-2 rounded-lg border border-[#0A1F44]/20 bg-white focus:outline-none focus:ring-2 focus:ring-[#00B4D8]"
          >
            <option value="general">General</option>
            <option value="analytics">Analytics</option>
            <option value="research">Research</option>
            <option value="ops">Operations</option>
          </select>
          <button type="submit" className="bg-[#0A1F44] hover:bg-[#0A1F44]/90 text-white px-4 py-2 rounded-lg transition-colors duration-200">Create</button>
        </form>
      )}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {(metrics || []).map((m, i) => (
          <div key={i} className="bg-white border border-[#0A1F44]/10 rounded-lg p-4">
            <div className="text-sm text-[#0A1F44]/60">Deployments: {(m?.deployments ?? 0).toLocaleString()}</div>
            <div className="text-sm text-[#0A1F44]/60 mt-1">Time Saved: {m?.timeSaved ?? '—'}</div>
            <div className="text-sm text-[#0A1F44]/60 mt-1">Usage: {m?.usage ?? '—'}</div>
          </div>
        ))}
      </div>

      <div className="bg-white border border-[#0A1F44]/10 rounded-lg overflow-hidden">
        {loading ? (
          <div className="p-8 text-center text-[#0A1F44]/40">Loading agents…</div>
        ) : (agents || []).length === 0 ? (
          <div className="p-8 text-center text-[#0A1F44]/40">
            No agents deployed yet. Create your first tailored agent to begin.
          </div>
        ) : (
          <div className="divide-y divide-[#0A1F44]/5">
            {(agents || []).map((agent) => {
              const isSelected = selected === agent.id;
              return (
                <div key={agent.id} className="p-4 hover:bg-[#0A1F44]/[0.03] transition-colors">
                  <div className="flex items-center justify-between gap-4">
                    <button onClick={() => selectAgent(agent)} className="flex-1 text-left">
                      <div className="flex items-center gap-3">
                        <span className="font-medium text-[#0A1F44]">{agent.name}</span>
                        <span className={`px-2 py-0.5 rounded-full text-xs ${agent.status === 'deployed' ? 'bg-green-50 text-green-700' : agent.status === 'training' ? 'bg-yellow-50 text-yellow-700' : 'bg-gray-50 text-gray-600'}`}>
                          {agent.status}
                        </span>
                        <span className="text-sm text-[#0A1F44]/50">{agent.type}</span>
                      </div>
                      <div className="text-sm text-[#0A1F44]/40 mt-1">Last deployed: {agent.lastDeployed || 'Never'}</div>
                    </button>
                    <div className="flex items-center gap-2">
                      {agent.status !== 'deployed' && (
                        <button onClick={() => toggleDeploy(agent)} className="bg-[#00B4D8]/10 hover:bg-[#00B4D8]/20 text-[#00B4D8] px-3 py-1.5 rounded-lg text-sm font-medium transition-colors">
                          Deploy
                        </button>
                      )}
                      {isSelected && <ChevronDown size={16} className="text-[#0A1F44]/40" />}
                    </div>
                  </div>
                  {isSelected && agentDetail && (
                    <div className="mt-4 pt-4 border-t border-[#0A1F44]/5">
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                        <div>
                          <div className="font-medium text-[#0A1F44] mb-2">Knowledge Sources</div>
                          <div className="space-y-2">
                            {(knowledge || []).filter(k => (agentDetail?.knowledge || []).includes(k.id)).length === 0 ? (
                              <div className="text-[#0A1F44]/40">No knowledge sources connected</div>
                            ) : (
                              (knowledge || []).filter(k => (agentDetail?.knowledge || []).includes(k.id)).map(k => (
                                <div key={k.id} className="flex items-center justify-between bg-[#0A1F44]/5 rounded px-3 py-2">
                                  <span>{k.source}</span>
                                  <span className="text-xs text-[#0A1F44]/50">{k.type}</span>
                                </div>
                              ))
                            )}
                          </div>
                        </div>
                        <div>
                          <div className="font-medium text-[#0A1F44] mb-2">Custom Tools</div>
                          <div className="space-y-2">
                            {(agentDetail?.tools || []).map((tool, idx) => (
                              <div key={idx} className="bg-[#00B4D8]/10 text-[#0A1F44] rounded px-3 py-2">{tool}</div>
                            ))}
                          </div>
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </div>
    </section>
  );
}

function SpecializedKnowledgeIntegrationSection({ user }) {
  const [agents, setAgents] = useState([]);
  const [knowledge, setKnowledge] = useState([]);
  const [metrics, setMetrics] = useState([]);
  const [selectedAgent, setSelectedAgent] = useState(null);
  const [showCreate, setShowCreate] = useState(false);
  const [newAgent, setNewAgent] = useState({ name: '', type: 'industry' });
  const [toast, setToast] = useState(null);

  useEffect(() => {
    apiFetch('/api/agents').then(d => setAgents(Array.isArray(d) ? d : (d?.items ?? [])));
    apiFetch('/api/knowledge').then(d => setKnowledge(Array.isArray(d) ? d : (d?.items ?? [])));
    apiFetch('/api/metrics').then(d => setMetrics(Array.isArray(d) ? d : (d?.items ?? [])));
  }, []);

  useEffect(() => {
    if (!toast) return;
    const t = setTimeout(() => setToast(null), 3000);
    return () => clearTimeout(t);
  }, [toast]);

  const createAgent = async (e) => {
    e.preventDefault();
    if (!newAgent.name.trim()) {
      setToast({ type: 'error', msg: 'Agent name is required.' });
      return;
    }
    const d = await apiFetch('/api/agents', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newAgent)
    });
    if (d?.id) {
      setAgents(prev => [...(prev || []), d]);
      setShowCreate(false);
      setNewAgent({ name: '', type: 'industry' });
      setToast({ type: 'success', msg: `Agent "${d.name}" created.` });
    } else {
      setToast({ type: 'error', msg: 'Failed to create agent.' });
    }
  };

  const deleteAgent = async (id) => {
    const d = await apiFetch(`/api/agents/${id}`, { method: 'DELETE' });
    if (d?.deleted) {
      setAgents(prev => (prev || []).filter(a => a.id !== id));
      if (selectedAgent?.id === id) setSelectedAgent(null);
      setToast({ type: 'success', msg: 'Agent deleted.' });
    }
  };

  const showToast = () => {
    if (!toast) return null;
    return (
      <div style={{ position: 'fixed', top: 20, right: 20, zIndex: 1000, background: toast.type === 'success' ? '#0A1F44' : '#b91c1c', color: '#fff', padding: '14px 20px', borderRadius: 12, boxShadow: '0 10px 25px rgba(0,0,0,.2)', display: 'flex', alignItems: 'center', gap: 10, animation: 'slideIn .3s ease' }}>
        <span>{toast.msg}</span>
      </div>
    );
  };

  const sortedAgents = [...(agents || [])].sort((a, b) => (a.lastDeployed || '').localeCompare(b.lastDeployed || ''));

  return (
    <div style={{ padding: 24, maxWidth: 1400, margin: '0 auto', fontFamily: "'Inter', sans-serif" }}>
      {showToast()}
      
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 32, flexWrap: 'wrap', gap: 16 }}>
        <div>
          <h1 style={{ fontSize: 28, fontWeight: 800, color: '#0A1F44', margin: '0 0 4px' }}>Specialized Knowledge Integration</h1>
          <p style={{ color: '#6B7280', fontSize: 15, margin: 0 }}>Tailor agents with proprietary knowledge and custom tools</p>
        </div>
        <button
          onClick={() => setShowCreate(true)}
          style={{ background: '#00B4D8', color: '#fff', border: 'none', padding: '12px 24px', borderRadius: 10, fontWeight: 700, cursor: 'pointer', transition: 'all .2s', display: 'flex', alignItems: 'center', gap: 8, fontSize: 14, boxShadow: '0 4px 12px rgba(0,180,216,.25)' }}
          onMouseEnter={e => e.currentTarget.style.transform = 'translateY(-2px)'}
          onMouseLeave={e => e.currentTarget.style.transform = 'translateY(0)'}
        >
          <Plus size={16} /> Create Agent
        </button>
      </div>

      {/* Metrics row */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 16, marginBottom: 32 }}>
        {[
          { label: 'Active Deployments', value: metrics.reduce((s, m) => s + (m.deployments || 0), 0) || 0, icon: <Rocket size={20} /> },
          { label: 'Hours Saved', value: metrics.reduce((s, m) => s + (m.timeSaved || 0), 0) || 0, icon: <Clock size={20} /> },
          { label: 'Total Usage', value: metrics.reduce((s, m) => s + (m.usage || 0), 0) || 0, icon: <Activity size={20} /> }
        ].map(m => (
          <div key={m.label} style={{ background: '#fff', border: '1px solid #E5E7EB', borderRadius: 16, padding: 20, boxShadow: '0 2px 8px rgba(0,0,0,.04)', transition: 'box-shadow .2s', cursor: 'pointer' }}
            onMouseEnter={e => e.currentTarget.style.boxShadow = '0 8px 20px rgba(0,180,216,.12)'}
            onMouseLeave={e => e.currentTarget.style.boxShadow = '0 2px 8px rgba(0,0,0,.04)'}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, color: '#00B4D8', marginBottom: 8 }}>{m.icon}</div>
            <div style={{ fontSize: 28, fontWeight: 800, color: '#0A1F44' }}>{m.value.toLocaleString()}</div>
            <div style={{ fontSize: 13, color: '#6B7280' }}>{m.label}</div>
          </div>
        ))}
      </div>

      {/* Agents grid */}
      <div style={{ marginBottom: 32 }}>
        <h2 style={{ fontSize: 20, fontWeight: 700, color: '#0A1F44', margin: '0 0 16px' }}>Tailored Agents</h2>
        {agents.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '48px 24px', background: '#F9FAFB', borderRadius: 16, border: '2px dashed #D1D5DB' }}>
            <Brain size={40} color="#00B4D8" style={{ marginBottom: 16 }} />
            <h3 style={{ fontSize: 18, fontWeight: 600, color: '#0A1F44', margin: '0 0 8px' }}>No agents yet</h3>
            <p style={{ color: '#6B7280', margin: '0 0 20px' }}>Create your first tailored agent with specialized knowledge.</p>
            <button onClick={() => setShowCreate(true)} style={{ background: '#00B4D8', color: '#fff', border: 'none', padding: '10px 20px', borderRadius: 8, fontWeight: 600, cursor: 'pointer' }}>Create Agent</button>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 16 }}>
            {(agents || []).map(agent => (
              <div key={agent.id} style={{ background: '#fff', border: selectedAgent?.id === agent.id ? '2px solid #00B4D8' : '1px solid #E5E7EB', borderRadius: 16, padding: 20, transition: 'all .2s', cursor: 'pointer', boxShadow: '0 2px 8px rgba(0,0,0,.04)' }}
                onMouseEnter={e => e.currentTarget.style.transform = 'translateY(-4px)'}
                onMouseLeave={e => e.currentTarget.style.transform = 'translateY(0)'}
                onClick={() => setSelectedAgent(agent)}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 12 }}>
                  <div style={{ width: 40, height: 40, borderRadius: 12, background: '#EBF5FF', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <Bot size={20} color="#0A1F44" />
                  </div>
                  <span style={{ padding: '4px 12px', borderRadius: 20, fontSize: 11, fontWeight: 600, textTransform: 'capitalize', background: agent.status === 'active' ? '#ECFDF5' : '#FEF3C7', color: agent.status === 'active' ? '#059669' : '#D97706' }}>
                    {agent.status}
                  </span>
                </div>
                <h3 style={{ fontSize: 16, fontWeight: 600, color: '#0A1F44', margin: '0 0 4px' }}>{agent.name}</h3>
                <p style={{ fontSize: 13, color: '#6B7280', margin: '0 0 16px', textTransform: 'capitalize' }}>{agent.type} agent</p>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{ fontSize: 12, color: '#9CA3AF' }}>{agent.lastDeployed || 'Not deployed yet'}</span>
                  <button onClick={(e) => { e.stopPropagation(); deleteAgent(agent.id); }} style={{ background: 'transparent', border: 'none', color: '#9CA3AF', cursor: 'pointer', padding: 4, borderRadius: 6 }} >
                    <Trash2 size={16} />
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Knowledge sources */}
      <div>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
          <h2 style={{ fontSize: 20, fontWeight: 700, color: '#0A1F44', margin: 0 }}>Knowledge Sources</h2>
          <button style={{ color: '#00B4D8', fontSize: 14, fontWeight: 600, background: 'none', border: 'none', cursor: 'pointer' }}>
            View all
          </button>
        </div>
        {knowledge.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '32px 24px', background: '#F9FAFB', borderRadius: 16 }}>
            <FileText size={32} color="#00B4D8" style={{ marginBottom: 8 }} />
            <p style={{ color: '#6B7280', margin: 0 }}>No knowledge sources added yet</p>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 12 }}>
            {(knowledge || []).map(k => (
              <div key={k.id} style={{ display: 'flex', alignItems: 'center', gap: 12, background: '#fff', border: '1px solid #E5E7EB', borderRadius: 12, padding: '14px 16px', transition: 'all .2s', cursor: 'pointer' }}
                onMouseEnter={e => e.currentTarget.style.boxShadow = '0 4px 12px rgba(0,0,0,.08)'}
                onMouseLeave={e => e.currentTarget.style.boxShadow = 'none'}
              >
                <div style={{ width: 32, height: 32, borderRadius: 8, background: '#F0FDFA', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                  <BookOpen size={16} color="#00B4D8" />
                </div>
                <div style={{ flex: 1 }}>
                  <div style={{ fontSize: 14, fontWeight: 500, color: '#0A1F44' }}>{k.source}</div>
                  <div style={{ fontSize: 12, color: '#6B7280', textTransform: 'capitalize' }}>{k.type} · updated {k.lastUpdated}</div>
                </div>
                <button onClick={() => setToast({ type: 'success', msg: 'Knowledge source connected' })} style={{ background: 'transparent', border: 'none', color: '#00B4D8', cursor: 'pointer', padding: 4 }}>
                  <Link2 size={16} />
                </button>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Create modal */}
      {showCreate && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(10,31,68,.5)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100 }}>
          <form onSubmit={createAgent} onClick={e => e.stopPropagation()} style={{ background: '#fff', padding: 28, borderRadius: 20, width: 400, maxWidth: '90vw', border: '2px solid #00B4D8' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
              <h3 style={{ fontSize: 20, fontWeight: 700, color: '#0A1F44', margin: 0 }}>Create Tailored Agent</h3>
              <button type="button" onClick={() => setShowCreate(false)} style={{ background: 'transparent', border: 'none', color: '#6B7280', cursor: 'pointer', padding: 4 }}>
                <X size={20} />
              </button>
            </div>
            <div style={{ marginBottom: 16 }}>
              <label style={{ fontSize: 14, fontWeight: 600, color: '#0A1F44', marginBottom: 6, display: 'block' }}>Agent Name</label>
              <input
                value={newAgent.name}
                onChange={(e) => setNewAgent({ ...newAgent, name: e.target.value })}
                placeholder="e.g. Legal Research Assistant"
                style={{ width: '100%', boxSizing: 'border-box', padding: '12px 14px', borderRadius: 10, border: '1px solid #D1D5DB', fontSize: 14, outline: 'none', transition: 'border .2s' }}
                onFocus={e => e.currentTarget.style.borderColor = '#00B4D8'}
                onBlur={e => e.currentTarget.style.borderColor = '#D1D5DB'}
              />
            </div>
            <div style={{ marginBottom: 20 }}>
              <label style={{ fontSize: 14, fontWeight: 600, color: '#0A1F44', marginBottom: 6, display: 'block' }}>Agent Type</label>
              <select value={newAgent.type} onChange={(e) => setNewAgent({ ...newAgent, type: e.target.value })} style={{ width: '100%', boxSizing: 'border-box', padding: '12px 14px', borderRadius: 10, border: '1px solid #D1D5DB', fontSize: 14, outline: 'none', transition: 'border .2s' }}>
                <option value="industry">Industry</option>
                <option value="leadership">Leadership</option>
                <option value="research">Research</option>
                <option value="operations">Operations</option>
              </select>
            </div>
            <button type="submit" style={{ background: '#00B4D8', color: '#fff', border: 'none', padding: '14px 24px', borderRadius: 10, fontWeight: 700, cursor: 'pointer', width: '100%', fontSize: 15, transition: 'all .2s' }}
              onMouseEnter={e => e.currentTarget.style.opacity = .9}
              onMouseLeave={e => e.currentTarget.style.opacity = 1}
            >
              Create Agent
            </button>
          </form>
        </div>
      )}
    </div>
  );
}

function CustomToolsSection({ user }) {
  const [agents, setAgents] = useState([]);
  const [metrics, setMetrics] = useState([]);
  const [knowledge, setKnowledge] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showCreate, setShowCreate] = useState(false);
  const [newAgent, setNewAgent] = useState({ name: '', type: 'specialized' });

  useEffect(() => {
    Promise.all([
      apiFetch('/api/agents').then(d => Array.isArray(d) ? d : (d?.items ?? [])),
      apiFetch('/api/metrics').then(d => Array.isArray(d) ? d : (d?.items ?? [])),
      apiFetch('/api/knowledge').then(d => Array.isArray(d) ? d : (d?.items ?? []))
    ]).then(([a, m, k]) => {
      setAgents((a) ?? []);
      setMetrics((m) ?? []);
      setKnowledge((k) ?? []);
      setLoading(false);
    }).catch(() => {
      setError('Failed to load data');
      setLoading(false);
    });
  }, []);

  const createAgent = async (e) => {
    e.preventDefault();
    if (!newAgent.name.trim()) return;
    const res = await apiFetch('/api/agents', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: newAgent.name, status: 'draft', type: newAgent.type })
    });
    if (res) {
      setAgents(prev => [...(prev || []), res]);
      setShowCreate(false);
      setNewAgent({ name: '', type: 'specialized' });
    }
  };

  const deleteAgent = async (id) => {
    const res = await apiFetch(`/api/agents/${id}`, { method: 'DELETE' });
    if (res?.deleted) {
      setAgents(prev => (prev || []).filter(a => a.id !== id));
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center py-24">
        <div className="animate-spin rounded-full h-12 w-12 border-4 border-[#00B4D8] border-t-transparent"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 border border-red-200 rounded-xl p-6 text-center">
        <p className="text-red-600 mb-4">{error}</p>
        <button onClick={() => window.location.reload()} className="bg-[#0A1F44] text-white px-4 py-2 rounded-lg hover:opacity-90 transition-opacity">
          Retry
        </button>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Metrics Overview */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {(metrics || []).map((m, i) => (
          <div key={i} className="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
            <h3 className="text-sm text-gray-500 mb-2">{m.deployments ? 'Active Deployments' : m.timeSaved ? 'Hours Saved' : 'Usage Rate'}</h3>
            <p className="text-3xl font-bold text-[#0A1F44]">
              {m.deployments ?? m.timeSaved ?? m.usage ?? 0}
            </p>
          </div>
        ))}
      </div>

      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-[#0A1F44]">Custom Tools</h2>
          <p className="text-gray-500 mt-1">Tailored agents for specialized missions</p>
        </div>
        <button
          onClick={() => setShowCreate(true)}
          className="bg-[#00B4D8] text-white px-4 py-2 rounded-lg hover:bg-[#0096b5] transition-colors flex items-center gap-2"
        >
          <Plus className="w-4 h-4" /> New Agent
        </button>
      </div>

      {/* Create Modal */}
      {showCreate && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <form onSubmit={createAgent} className="bg-white rounded-xl p-6 w-full max-w-md">
            <h3 className="text-lg font-bold text-[#0A1F44] mb-4">Create Tailored Agent</h3>
            <input
              value={newAgent.name}
              onChange={e => setNewAgent({ ...newAgent, name: e.target.value })}
              placeholder="Agent name"
              className="w-full border border-gray-300 rounded-lg px-3 py-2 mb-3 focus:ring-2 focus:ring-[#00B4D8] focus:border-transparent outline-none"
            />
            <select
              value={newAgent.type}
              onChange={e => setNewAgent({ ...newAgent, type: e.target.value })}
              className="w-full border border-gray-300 rounded-lg px-3 py-2 mb-4 focus:ring-2 focus:ring-[#00B4D8] focus:border-transparent outline-none"
            >
              <option value="specialized">Specialized Knowledge</option>
              <option value="mission">Mission Focused</option>
              <option value="strategic">Strategic Advisory</option>
            </select>
            <div className="flex gap-2 justify-end">
              <button type="button" onClick={() => setShowCreate(false)} className="px-4 py-2 text-gray-500 hover:bg-gray-100 rounded-lg transition-colors">
                Cancel
              </button>
              <button type="submit" className="bg-[#0A1F44] text-white px-4 py-2 rounded-lg hover:opacity-90 transition-opacity">
                Create Agent
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Agents Grid */}
      {agents.length === 0 ? (
        <div className="bg-gray-50 rounded-xl py-16 text-center border-2 border-dashed border-gray-200">
          <Bot className="w-16 h-16 text-[#00B4D8] mx-auto mb-4" />
          <h3 className="text-xl font-semibold text-[#0A1F44] mb-2">No Custom Agents Yet</h3>
          <p className="text-gray-500 mb-6">Build your first tailored agent for a specialized mission.</p>
          <button onClick={() => setShowCreate(true)} className="bg-[#00B4D8] text-white px-6 py-2 rounded-lg hover:bg-[#0096b5] transition-colors">
            Create Your First Agent
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {(agents || []).map(agent => (
            <div key={agent.id} className="bg-white rounded-xl p-6 shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
              <div className="flex items-start justify-between mb-3">
                <div className="bg-[#0A1F44] text-white p-2 rounded-lg">
                  <Bot className="w-5 h-5" />
                </div>
                <span className={`text-xs px-2 py-1 rounded-full ${
                  agent.status === 'active' ? 'bg-green-100 text-green-700' : 'bg-gray-100 text-gray-600'
                }`}>
                  {agent.status}
                </span>
              </div>
              <h3 className="font-semibold text-lg text-[#0A1F44] mb-2">{agent.name}</h3>
              <p className="text-sm text-gray-600 mb-3">{agent.type}</p>
              <p className="text-xs text-gray-400 mb-4">Deployed: {agent.lastDeployed}</p>
              <div className="flex gap-2">
                <button className="flex-1 bg-[#00B4D8] text-white py-2 rounded-lg text-sm hover:bg-[#0096b5] transition-colors flex items-center justify-center gap-1">
                  <Rocket className="w-4 h-4" /> Deploy
                </button>
                <button onClick={() => deleteAgent(agent.id)} className="px-3 py-2 border border-red-200 text-red-600 rounded-lg text-sm hover:bg-red-50 transition-colors">
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Knowledge Sources */}
      <div className="mt-8">
        <h3 className="text-xl font-bold text-[#0A1F44] mb-4">Knowledge Sources</h3>
        {knowledge.length === 0 ? (
          <p className="text-gray-500 text-center py-8">No knowledge sources connected yet.</p>
        ) : (
          <div className="bg-white rounded-xl border border-gray-100 overflow-hidden">
            {(knowledge || []).map((k, i) => (
              <div key={k.id} className="flex items-center justify-between px-6 py-4 border-b border-gray-50 last:border-b-0 hover:bg-gray-50 transition-colors">
                <div className="flex items-center gap-3">
                  <Database className="w-4 h-4 text-[#00B4D8]" />
                  <span className="font-medium text-[#0A1F44]">{k.source}</span>
                </div>
                <div className="flex items-center gap-4">
                  <span className="text-sm text-gray-500">{k.type}</span>
                  <span className="text-xs text-gray-400">{k.lastUpdated}</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

function MissionfocusedDeploymentSection({ user }) {
  const [metrics, setMetrics] = useState([]);
  const [agents, setAgents] = useState([]);
  const [knowledge, setKnowledge] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [selectedAgent, setSelectedAgent] = useState(null);

  useEffect(() => {
    const BASE = window.__BACKEND_URL__ || '';
    const apiFetch = async (path, opts = {}) => {
      for (let i = 0; i < 5; i++) {
        try {
          const r = await fetch(BASE + path, opts);
          if (r.ok) return r.json();
        } catch (_) {}
        await new Promise(r => setTimeout(r, 1500));
      }
      return null;
    };
    Promise.all([
      apiFetch('/api/metrics'),
      apiFetch('/api/agents'),
      apiFetch('/api/knowledge')
    ]).then(([m, a, k]) => {
      setMetrics(Array.isArray(m) ? m : []);
      setAgents(Array.isArray(a) ? a : []);
      setKnowledge(Array.isArray(k) ? k : []);
      setLoading(false);
      setError(false);
    }).catch(() => {
      setLoading(false);
      setError(true);
    });
  }, []);

  const totalDeployments = (metrics || []).reduce((s, m) => s + (m.deployments || 0), 0);
  const totalTimeSaved = (metrics || []).reduce((s, m) => s + (m.timeSaved || 0), 0);
  const avgUsage = (metrics || []).length ? Math.round((metrics || []).reduce((s, m) => s + (m.usage || 0), 0) / metrics.length) : 0;

  const deployAgent = async (agentId) => {
    const BASE = window.__BACKEND_URL__ || '';
    const r = await fetch(`${BASE}/api/deployments`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ agentId })
    });
    if (r.ok) {
      const d = await r.json();
      setAgents(prev => (prev || []).map(a => a.id === agentId ? { ...a, status: d.status || 'deployed', lastDeployed: new Date().toISOString() } : a));
    }
  };

  if (loading) {
    return (
      <div className="p-6 space-y-6">
        <div className="animate-pulse space-y-4">
          <div className="h-8 bg-[#0A1F44]/10 rounded w-64"></div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {[1, 2, 3].map(i => <div key={i} className="h-24 bg-[#0A1F44]/5 rounded-xl"></div>)}
          </div>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
            <div className="h-64 bg-[#0A1F44]/5 rounded-xl"></div>
            <div className="h-64 bg-[#0A1F44]/5 rounded-xl"></div>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center py-16">
        <p className="text-[#0A1F44] mb-4">Failed to load mission data</p>
        <button onClick={() => window.location.reload()} className="px-4 py-2 bg-[#00B4D8] text-white rounded-lg hover:bg-[#0A1F44] transition-colors">Retry</button>
      </div>
    );
  }

  return (
    <div className="space-y-8 p-6">
      <div>
        <h2 className="text-2xl font-bold text-[#0A1F44]">Mission-Focused Deployment</h2>
        <p className="text-gray-600 mt-1">Tailored agents deployed for your organization's specific missions</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white rounded-xl border border-[#0A1F44]/10 p-6 shadow-sm">
          <div className="flex items-center gap-2 text-[#00B4D8] mb-2">
            <Rocket className="w-4 h-4" />
            <span className="text-sm font-medium">Total Deployments</span>
          </div>
          <p className="text-3xl font-bold text-[#0A1F44]">{totalDeployments}</p>
        </div>

        <div className="bg-white rounded-xl border border-[#0A1F44]/10 p-6 shadow-sm">
          <div className="flex items-center gap-2 text-[#00B4D8] mb-2">
            <Clock className="w-4 h-4" />
            <span className="text-sm font-medium">Hours Saved</span>
          </div>
          <p className="text-3xl font-bold text-[#0A1F44]">{totalTimeSaved}hrs</p>
        </div>

        <div className="bg-white rounded-xl border border-[#0A1F44]/10 p-6 shadow-sm">
          <div className="flex items-center gap-2 text-[#00B4D8] mb-2">
            <Users className="w-4 h-4" />
            <span className="text-sm font-medium">Avg Usage</span>
          </div>
          <p className="text-3xl font-bold text-[#0A1F44]">{avgUsage}%</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white rounded-xl border border-[#0A1F44]/10 overflow-hidden shadow-sm">
          <div className="px-6 py-4 border-b border-[#0A1F44]/10 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Bot className="w-5 h-5 text-[#00B4D8]" />
              <h3 className="font-semibold text-[#0A1F44]">Deployed Agents</h3>
            </div>
            <button
              onClick={() => setSelectedAgent(null)}
              className="text-sm text-[#00B4D8] hover:text-[#0A1F44] transition-colors"
            >+ New Agent</button>
          </div>

          <div className="divide-y divide-[#0A1F44]/5">
            {(agents || []).length === 0 && (
              <div className="px-6 py-10 text-center">
                <Bot className="w-10 h-10 text-[#0A1F44]/20 mx-auto mb-3" />
                <p className="text-gray-500 text-sm">No agents deployed yet</p>
                <p className="text-[#00B4D8] text-sm mt-1 cursor-pointer hover:text-[#0A1F44]">Create your first tailored agent</p>
              </div>
            )}

            {(agents || []).slice(0, 4).map(agent => (
              <div key={agent.id} className="px-6 py-4 hover:bg-[#00B4D8]/5 transition-colors">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="font-medium text-[#0A1F44]">{agent.name}</p>
                    <p className="text-xs text-gray-500">{agent.type}</p>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                      agent.status === 'active'
                        ? 'bg-[#00B4D8]/10 text-[#00B4D8]'
                        : 'bg-[#0A1F44]/10 text-[#0A1F44]'
                    }`}>
                      {agent.status === 'active' ? 'Active' : 'Standby'}
                    </span>
                    <button
                      onClick={() => deployAgent(agent.id)}
                      className="text-[#00B4D8] hover:text-[#0A1F44] transition-colors"
                    >
                      <Send className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white rounded-xl border border-[#0A1F44]/10 p-6 shadow-sm">
          <div className="flex items-center gap-2 mb-6">
            <Database className="w-5 h-5 text-[#00B4D8]" />
            <h3 className="font-semibold text-[#0A1F44]">Knowledge Sources</h3>
          </div>

          <div className="space-y-3">
            {(knowledge || []).map(k => (
              <div key={k.id} className="flex items-center justify-between p-3 rounded-lg bg-[#0A1F44]/3">
                <div className="flex items-center gap-3 min-w-0">
                  <BookOpen className="w-4 h-4 text-[#00B4D8]" />
                  <div className="min-w-0">
                    <p className="font-medium text-[#0A1F44] text-sm truncate">{k.source}</p>
                    <p className="text-xs text-gray-500">{k.type}</p>
                  </div>
                </div>
                <span className="text-xs text-gray-400 ml-2">Updated {new Date(k.lastUpdated).toLocaleDateString()}</span>
              </div>
            ))}

            {(knowledge || []).length === 0 && (
              <div className="flex flex-col items-center py-10 text-center">
                <BookOpen className="w-10 h-10 text-[#0A1F44]/20 mx-auto mb-3" />
                <p className="text-gray-500 text-sm">No knowledge sources linked</p>
                <p className="text-[#00B4D8] text-sm mt-1">Add specialized knowledge</p>
              </div>
            )}
          </div>
        </div>
      </div>

      {(metrics || []).length > 0 && (
        <div className="bg-white rounded-xl border border-[#0A1F44]/10 overflow-hidden shadow-sm">
          <div className="px-6 py-4 border-b border-[#0A1F44]/10">
            <h3 className="font-semibold text-[#0A1F44]">Deployment Efficiency</h3>
          </div>
          <div className="p-6 space-y-4">
            {(metrics || []).map((m, i) => (
              <div key={i}>
                <div className="flex justify-between text-sm mb-1">
                  <span className="text-gray-600">Period {i + 1}</span>
                  <span className="font-medium text-[#0A1F44]">{m.deployments} deployments · {m.timeSaved}h saved</span>
                </div>
                <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-gradient-to-r from-[#0A1F44] to-[#00B4D8] rounded-full"
                    style={{ width: `${Math.min(100, m.usage || 0)}%` }}
                  ></div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}


function ProductApp({ user, onLogout }) {
  const [tab, setTab] = useState('HighlyTailoredAgents');
  const _nav = [{ id: 'HighlyTailoredAgents', label: 'Highly tailored agents' }, { id: 'SpecializedKnowledgeIntegration', label: 'Specialized knowledge integration' }, { id: 'CustomTools', label: 'Custom tools' }, { id: 'MissionfocusedDeployment', label: 'Missionfocused deployment' }];
  return (
    <div className="min-h-screen flex flex-col md:flex-row" style={{ background: '#0a0d18', color: '#e6eaf2', fontFamily: 'system-ui' }}>
      <aside className="hidden md:flex md:flex-col" style={{ width: 220, borderRight: '1px solid rgba(255,255,255,.08)', padding: 18, gap: 6 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, fontWeight: 800, fontSize: 18, marginBottom: 16 }}>
          <img src={LOGO} alt="QL Agents" style={{ width: 26, height: 26, borderRadius: 7 }} />
          QL Agents
        </div>
        {(_nav || []).map((n) => (
          <button key={n.id} onClick={() => setTab(n.id)} style={{ textAlign: 'left', padding: '9px 12px', borderRadius: 9, border: 'none', cursor: 'pointer', background: tab === n.id ? '#0A1F44' : 'transparent', color: tab === n.id ? '#fff' : '#9aa6bd', fontWeight: 600 }}>{n.label}</button>
        ))}
        <button onClick={onLogout} style={{ marginTop: 'auto', textAlign: 'left', padding: '9px 12px', borderRadius: 9, border: 'none', cursor: 'pointer', background: 'transparent', color: '#9aa6bd' }}>Log out</button>
      </aside>
      <div className="md:hidden" style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '10px 12px', overflowX: 'auto', borderBottom: '1px solid rgba(255,255,255,.08)' }}>
        <span style={{ display: 'flex', alignItems: 'center', gap: 8, fontWeight: 800, fontSize: 15, marginRight: 6, whiteSpace: 'nowrap' }}>
          <img src={LOGO} alt="QL Agents" style={{ width: 20, height: 20, borderRadius: 5 }} />
          QL Agents
        </span>
        {(_nav || []).map((n) => (
          <button key={n.id} onClick={() => setTab(n.id)} style={{ whiteSpace: 'nowrap', padding: '7px 12px', borderRadius: 999, border: 'none', cursor: 'pointer', fontSize: 13, background: tab === n.id ? '#0A1F44' : 'rgba(255,255,255,.06)', color: tab === n.id ? '#fff' : '#9aa6bd', fontWeight: 600 }}>{n.label}</button>
        ))}
        <button onClick={onLogout} style={{ marginLeft: 'auto', whiteSpace: 'nowrap', padding: '7px 10px', borderRadius: 999, border: '1px solid rgba(255,255,255,.14)', cursor: 'pointer', fontSize: 12, background: 'transparent', color: '#9aa6bd' }}>Log out</button>
      </div>
      <main className="flex-1" style={{ padding: 24, overflowY: 'auto' }}>
        <div style={{ marginBottom: 18, color: '#9aa6bd', fontSize: 14 }}>Welcome, {user?.name || 'there'} 👋</div>
        {tab === 'HighlyTailoredAgents' && <HighlyTailoredAgentsSection user={user} />}
          {tab === 'SpecializedKnowledgeIntegration' && <SpecializedKnowledgeIntegrationSection user={user} />}
          {tab === 'CustomTools' && <CustomToolsSection user={user} />}
          {tab === 'MissionfocusedDeployment' && <MissionfocusedDeploymentSection user={user} />}
          
      </main>
    </div>
  );
}

function AuthGate({ onAuth, onClose }) {
  const [mode, setMode] = useState('signup');
  const [form, setForm] = useState({ name: '', email: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const _ip = { width: '100%', padding: '11px 13px', margin: '6px 0', borderRadius: 9, border: '1px solid #2a3350', background: '#0b1020', color: '#e6eaf2', fontSize: 14, outline: 'none', boxSizing: 'border-box' };
  const submit = async (e) => {
    e.preventDefault();
    if (!form.email || !form.password) return;
    setLoading(true); setError('');
    const _b = window.__NC_BASE__ || ''; const _s = window.__COMPANY_SLUG__ || '';
    const body = JSON.stringify({ email: form.email, password: form.password, name: form.name });
    const _call = () => fetch(`${_b}/api/c/${_s}/auth/${mode}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body });
    try {
      let res; try { res = await _call(); } catch { await new Promise(r => setTimeout(r, 2500)); res = await _call(); }
      const json = await res.json();
      if (!json.ok) { setError(json.error || 'Authentication failed — please try again'); setLoading(false); return; }
      onAuth(json);
    } catch { setError('Connection error — please try again in a moment.'); setLoading(false); }
  };
  return (
    <div onClick={onClose} style={{ position: 'fixed', inset: 0, background: 'rgba(2,6,18,.7)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000 }}>
      <form onClick={(e) => e.stopPropagation()} onSubmit={submit} style={{ background: '#0f1424', border: '1px solid #232b45', padding: 28, borderRadius: 16, width: 360, maxWidth: '90vw', color: '#e6eaf2' }}>
        <h3 style={{ margin: '0 0 16px', fontSize: 20, fontWeight: 700 }}>{mode === 'signup' ? 'Create your account' : 'Welcome back'}</h3>
        {mode === 'signup' && <input value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} placeholder="Your name" style={_ip} />}
        <input value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} placeholder="Work email" type="email" required style={_ip} />
        <input value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} placeholder="Password (min 6 chars)" type="password" required style={_ip} />
        {error && <p style={{ color: '#f87171', fontSize: 13, margin: '6px 0 0' }}>{error}</p>}
        <button type="submit" disabled={loading} style={{ width: '100%', marginTop: 10, padding: '12px', borderRadius: 9, border: 'none', background: loading ? '#4b50b8' : '#6366f1', color: '#fff', fontWeight: 700, fontSize: 15, cursor: loading ? 'default' : 'pointer' }}>
          {loading ? '…' : mode === 'signup' ? 'Get started free' : 'Log in'}
        </button>
        <p onClick={() => { setMode(mode === 'signup' ? 'login' : 'signup'); setError(''); }} style={{ marginTop: 14, fontSize: 13, color: '#9aa6bd', cursor: 'pointer', textAlign: 'center' }}>
          {mode === 'signup' ? 'Already have an account? Log in' : 'New here? Create an account'}
        </p>
      </form>
    </div>
  );
}

function App() {
  const [auth, setAuth] = useState(() => {
    try {
      if (localStorage.getItem('nc_user') && !localStorage.getItem('nc_auth')) localStorage.removeItem('nc_user');
      const a = JSON.parse(localStorage.getItem('nc_auth') || 'null');
      return (a && a.token && a.user && typeof a.user.email === 'string') ? a : null;
    } catch { return null; }
  });
  const [showAuth, setShowAuth] = useState(false);
  useEffect(() => {
    if (!auth?.token) return;
    const _b = window.__NC_BASE__ || ''; const _s = window.__COMPANY_SLUG__ || '';
    fetch(`${_b}/api/c/${_s}/auth/me`, { headers: { Authorization: `Bearer ${auth.token}` } })
      .then(r => r.json()).then(d => { if (!d.ok) { localStorage.removeItem('nc_auth'); setAuth(null); } }).catch(() => {});
  }, []);
  const onAuth = (data) => { localStorage.setItem('nc_auth', JSON.stringify(data)); setAuth(data); setShowAuth(false); };
  const onLogout = () => { localStorage.removeItem('nc_auth'); setAuth(null); };
  if (auth?.user) return <ProductApp user={auth.user} token={auth.token} onLogout={onLogout} />;
  return (
    <>
      <LandingPage onGetStarted={() => setShowAuth(true)} onSignup={() => setShowAuth(true)} onLogin={() => setShowAuth(true)} />
      {/* Fallback entry point (bottom-right so it never overlaps the nav) — guarantees a
          working login even if the landing's own buttons aren't wired to the auth modal. */}
      <button onClick={() => setShowAuth(true)} style={{ position: 'fixed', bottom: 20, right: 20, zIndex: 999, background: '#6366f1', color: '#fff', border: 'none', padding: '10px 18px', borderRadius: 999, fontWeight: 600, fontSize: 14, cursor: 'pointer', boxShadow: '0 6px 20px rgba(99,102,241,.45)' }}>Sign in</button>
      {showAuth && <AuthGate onAuth={onAuth} onClose={() => setShowAuth(false)} />}
    </>
  );
}

export default App;
