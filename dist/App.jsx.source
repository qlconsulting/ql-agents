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

function ProductApp({ user, onLogout }) {
  /* NC_PLACEHOLDER_DASHBOARD — replaced by the real dashboard in Phase 2 */
  return (
    <div style={{ minHeight: '100vh', background: '#0a0d18', color: '#e6eaf2', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 16, padding: 24, textAlign: 'center' }}>
      <img src={LOGO} alt="QL Agents" style={{ width: 56, height: 56, borderRadius: 12, marginBottom: 4 }} />
      <h1 style={{ fontSize: 28, fontWeight: 800, margin: 0 }}>Welcome, {user?.name || user?.email || 'there'} 👋</h1>
      <p style={{ color: '#9aa6bd', maxWidth: 460, lineHeight: 1.5, margin: 0 }}>Your account is ready. Your dashboard is being set up and will appear here shortly.</p>
      <button onClick={onLogout} style={{ marginTop: 8, padding: '10px 18px', borderRadius: 10, border: '1px solid #2a3350', background: 'transparent', color: '#e6eaf2', fontWeight: 600, cursor: 'pointer' }}>Log out</button>
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
      <button onClick={() => setShowAuth(true)} style={{ position: 'fixed', bottom: 20, right: 20, zIndex: 999, background: COLORS.primary, color: COLORS.navy, border: 'none', padding: '10px 18px', borderRadius: 999, fontWeight: 600, fontSize: 14, cursor: 'pointer', boxShadow: `0 6px 20px ${COLORS.primaryBorder}` }}>Sign in</button>
      {showAuth && <AuthGate onAuth={onAuth} onClose={() => setShowAuth(false)} />}
    </>
  );
}

export default App;
