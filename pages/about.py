import streamlit as st

st.set_page_config(page_title="About | Clyde's Portfolio", page_icon="👤", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');
html, body, [class*="css"] { font-family: 'Syne', sans-serif; background-color: #0d0d0d; color: #f0ece2; }
.section-label { font-family:'Space Mono',monospace; font-size:0.7rem; letter-spacing:4px; text-transform:uppercase; color:#c8b97a; }
.skill-bar-bg { background:#1a1a1a; border-radius:100px; height:6px; margin:6px 0 16px; }
.skill-bar-fill { background: linear-gradient(90deg,#c8b97a,#f0ece2); border-radius:100px; height:6px; }
.hobby-card { background:#141414; border:1px solid #2a2a2a; border-radius:12px; padding:1.5rem; text-align:center; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="section-label">Who I am</p>', unsafe_allow_html=True)
st.markdown("# About Me")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("""
    I'm a software engineer and data enthusiast based in **Cape Town, South Africa**.
    I specialise in building end-to-end data solutions — from ingestion pipelines and
    warehouse modelling, to dashboards and automation tools that save people hours every week.

    My background spans backend Python development, cloud data infrastructure on GCP,
    and a healthy obsession with clean, well-documented code. I believe the best systems
    are the ones nobody notices because they just *work*.

    I'm currently open to **freelance projects** and **full-time opportunities** — feel free
    to reach out on LinkedIn or via email.
    """)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="section-label">Education</p>', unsafe_allow_html=True)
    st.markdown("""
    - 🎓 **BSc Computer Science** — University of Cape Town *(or your degree)*
    - 📜 **Google Data Analytics Certificate**
    - 📜 **dbt Fundamentals**
    """)

with col2:
    st.markdown('<p class="section-label">Contact</p>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Space Mono',monospace; font-size:0.85rem; line-height:2.2; color:#888;">
    📧 your.email@example.com<br>
    🌍 Cape Town, South Africa<br>
    💼 Open to work
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>")
st.divider()

# ── Skills ────────────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">Skills</p>', unsafe_allow_html=True)
st.markdown("### Technical Stack")
st.markdown("<br>", unsafe_allow_html=True)

skills = {
    "Python": 90,
    "SQL / BigQuery": 85,
    "Google Cloud Platform": 75,
    "Streamlit": 80,
    "dbt": 65,
    "Git & CI/CD": 70,
}

col1, col2 = st.columns(2)
items = list(skills.items())
for i, (skill, pct) in enumerate(items):
    col = col1 if i % 2 == 0 else col2
    with col:
        st.markdown(f"""
        <div style="display:flex; justify-content:space-between; font-size:0.9rem;">
            <span>{skill}</span>
            <span style="font-family:'Space Mono',monospace; color:#c8b97a; font-size:0.8rem;">{pct}%</span>
        </div>
        <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:{pct}%"></div></div>
        """, unsafe_allow_html=True)

st.markdown("<br>")
st.divider()

# ── Hobbies ───────────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">Beyond the keyboard</p>', unsafe_allow_html=True)
st.markdown("### Hobbies & Interests")
st.markdown("<br>", unsafe_allow_html=True)

hobbies = [
    ("🏄", "Surfing", "Cape Town has world-class waves — I'm out there when I can be."),
    ("📚", "Reading", "Tech blogs, sci-fi, and the occasional business book."),
    ("🎸", "Music", "Guitar player, mostly blues and rock."),
    ("🤖", "Open Source", "Contributing to tools I use and building things for fun."),
]

cols = st.columns(len(hobbies))
for col, (icon, title, desc) in zip(cols, hobbies):
    with col:
        st.markdown(f"""
        <div class="hobby-card">
            <div style="font-size:2.5rem">{icon}</div>
            <div style="font-weight:700; margin:.6rem 0 .4rem">{title}</div>
            <div style="color:#666; font-size:0.85rem">{desc}</div>
        </div>
        """, unsafe_allow_html=True)