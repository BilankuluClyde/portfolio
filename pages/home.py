import streamlit as st

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background-color: #0d0d0d;
    color: #f0ece2;
}

h1, h2, h3 { font-family: 'Syne', sans-serif; }

.hero-name {
    font-size: 5rem;
    font-weight: 800;
    letter-spacing: -2px;
    line-height: 1;
    background: linear-gradient(135deg, #f0ece2 40%, #c8b97a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    font-family: 'Space Mono', monospace;
    font-size: 1rem;
    color: #c8b97a;
    margin-top: 0.5rem;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.hero-bio {
    font-size: 1.1rem;
    color: #a09a8a;
    max-width: 550px;
    line-height: 1.8;
    margin-top: 1.5rem;
}

.tag-pill {
    display: inline-block;
    background: #1a1a1a;
    border: 1px solid #c8b97a44;
    color: #c8b97a;
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    padding: 4px 14px;
    border-radius: 100px;
    margin: 4px 4px 4px 0;
}

.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #c8b97a;
    margin-bottom: 0.5rem;
}

.stat-box {
    background: #141414;
    border: 1px solid #2a2a2a;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
}

.stat-num {
    font-size: 2.5rem;
    font-weight: 800;
    color: #c8b97a;
}

.stat-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    color: #666;
    letter-spacing: 2px;
    text-transform: uppercase;
}

hr { border-color: #1e1e1e !important; }

.stButton > button {
    background: transparent;
    border: 1px solid #c8b97a;
    color: white !important;
    text-decoration: none !important;
    font-family: 'Space Mono', monospace;
    font-size: 20.8rem;
    letter-spacing: 2px;
    padding: 0.6rem 1.8rem;
    border-radius: 100px;
    transition: all 0.2s;
}
.stButton > button:hover {
    background: #c8b97a;
    color: #0d0d0d;
}
</style>
""", unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────────────────────────
col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown('<p class="section-label">Clyde\'s Github Portfolio</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-name">Welcome</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">Software Engineer | Data Engineer | BI Developer </p>', unsafe_allow_html=True)
    st.markdown("""
        <p class="hero-bio">
            I build data pipelines, dashboards, and automation systems that turn
            raw data into decisions. Based in Cape Town 🇿🇦 — available worldwide.
        </p>
    """, unsafe_allow_html=True)

    # Tech tags
    tags = ["Python", "SQL", "Java", "C#", "Google Cloud Platforms", "Azure", "Streamlit", "dbt", "Git"]
    tag_html = "".join(f'<span class="tag-pill">{t}</span>' for t in tags)
    st.markdown(f'<div style="margin-top:1.5rem">{tag_html}</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("GitHub ↗", "https://github.com/BilankuluClyde/", use_container_width=True)
    with c2:
        st.link_button("LinkedIn ↗", "https://www.linkedin.com/in/mpfuno-clyde-bilankulu/", use_container_width=True)

with col2:
    # Stats panel
    st.markdown('<div class="stat-box"><div class="stat-num">12+</div><div class="stat-label">Projects Shipped</div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="stat-box"><div class="stat-num">3</div><div class="stat-label">Years of Experience</div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="stat-box"><div class="stat-num">∞</div><div class="stat-label">Problems to Solve</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# ── Featured quick-links ──────────────────────────────────────────────────────
st.markdown('<p class="section-label">Explore</p>', unsafe_allow_html=True)
st.markdown("### What would you like to see?")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
        <a href="/projects" class="stButton" target="_self"  style="text-decoration:none;">
            <div class="stat-box stButton" style="text-align:left; padding:2rem;">
            <div style="font-size:2rem">📁</div>
            <div style="font-weight:700; margin:.5rem 0">Projects</div>
            <div style="color:#666; font-size:.9rem">Browse my open-source repos and case studies.</div>
            </div>
        </a>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <a href="/about" class="stButton" target="_self"  style="text-decoration:none;">
        <div class="stat-box stButton" style="text-align:left; padding:2rem;">
            <div style="font-size:2rem">👤</div>
            <div style="font-weight:700; margin:.5rem 0">About</div>
            <div style="color:#666; font-size:.9rem">My background, skills, and what drives me.</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <a href="/resume" class="stButton" target="_self"  style="text-decoration:none;">
        <div class="stat-box" style="text-align:left; padding:2rem;">
            <div style="font-size:2rem">📄</div>
            <div style="font-weight:700; margin:.5rem 0">Resume</div>
            <div style="color:#666; font-size:.9rem">Download my CV or view it inline.</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
