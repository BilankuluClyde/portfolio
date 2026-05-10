import streamlit as st

st.set_page_config(page_title="Resume | Clyde's Portfolio", page_icon="📄", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');
html, body, [class*="css"] { font-family: 'Syne', sans-serif; background-color: #0d0d0d; color: #f0ece2; }
.section-label { font-family:'Space Mono',monospace; font-size:0.7rem; letter-spacing:4px; text-transform:uppercase; color:#c8b97a; }
.timeline-item { border-left: 2px solid #2a2a2a; padding-left: 1.5rem; margin-bottom: 2rem; position:relative; }
.timeline-item::before { content:''; position:absolute; left:-5px; top:6px; width:8px; height:8px; background:#c8b97a; border-radius:50%; }
.role-title { font-size: 1.1rem; font-weight: 700; }
.role-company { color: #c8b97a; font-family:'Space Mono',monospace; font-size:0.85rem; }
.role-dates { color: #555; font-family:'Space Mono',monospace; font-size:0.75rem; float:right; }
.role-desc { color: #888; font-size:0.9rem; margin-top:0.6rem; line-height:1.7; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="section-label">Career</p>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("# Resume")
with col2:
    # Replace with your actual CV file
    # with open("assets/CV_Clyde.pdf", "rb") as f:
    #     st.download_button("Download CV ↓", f, file_name="Clyde_CV.pdf", mime="application/pdf", use_container_width=True)
    st.info("Upload your PDF to `assets/CV_Clyde.pdf` to enable the download button.")

st.markdown("<br>")

# ── Experience ────────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">Experience</p>', unsafe_allow_html=True)
st.markdown("### Work History")
st.markdown("<br>", unsafe_allow_html=True)

experience = [
    {
        "role": "Data Engineer",
        "company": "Company Name",
        "dates": "Jan 2023 – Present",
        "bullets": [
            "Built and maintained BigQuery pipelines processing 10M+ rows daily.",
            "Reduced report load times by 60% through query optimisation and materialised views.",
            "Introduced dbt for SQL transformation layer, improving team collaboration.",
        ],
    },
    {
        "role": "Junior Software Developer",
        "company": "Previous Company",
        "dates": "Jun 2021 – Dec 2022",
        "bullets": [
            "Developed Python automation scripts saving 15+ hours of manual work per week.",
            "Maintained REST API integrations with third-party data providers.",
            "Contributed to internal dashboards using Streamlit and Plotly.",
        ],
    },
]

for exp in experience:
    bullets_html = "".join(f"<li>{b}</li>" for b in exp["bullets"])
    st.markdown(f"""
    <div class="timeline-item">
        <span class="role-dates">{exp['dates']}</span>
        <div class="role-title">{exp['role']}</div>
        <div class="role-company">{exp['company']}</div>
        <ul class="role-desc">{bullets_html}</ul>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ── Education ─────────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">Education</p>', unsafe_allow_html=True)
st.markdown("### Qualifications")
st.markdown("<br>", unsafe_allow_html=True)

education = [
    {"degree": "BSc Computer Science", "institution": "University of Cape Town", "year": "2021"},
    {"degree": "Google Data Analytics Certificate", "institution": "Google / Coursera", "year": "2022"},
    {"degree": "dbt Fundamentals", "institution": "dbt Labs", "year": "2023"},
]

for edu in education:
    st.markdown(f"""
    <div class="timeline-item">
        <span class="role-dates">{edu['year']}</span>
        <div class="role-title">{edu['degree']}</div>
        <div class="role-company">{edu['institution']}</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ── Certifications ────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">Certifications</p>', unsafe_allow_html=True)
cols = st.columns(3)
certs = [
    ("🏅", "Google Cloud Associate", "2023"),
    ("🏅", "dbt Fundamentals", "2023"),
    ("🏅", "AWS Cloud Practitioner", "2024"),
]
for col, (icon, name, year) in zip(cols, certs):
    with col:
        st.markdown(f"""
        <div style="background:#141414; border:1px solid #2a2a2a; border-radius:12px; padding:1.2rem; text-align:center;">
            <div style="font-size:2rem">{icon}</div>
            <div style="font-weight:700; margin:.5rem 0 .2rem; font-size:.95rem">{name}</div>
            <div style="font-family:'Space Mono',monospace; color:#555; font-size:.75rem">{year}</div>
        </div>
        """, unsafe_allow_html=True)