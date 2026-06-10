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
    #st.info("Upload your PDF to `assets/CV_Clyde.pdf` to enable the download button.")
    with open("./assets/Mpfuno_Clyde_Bilankulu_CV.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    st.download_button(
        label="DOwnload My CV",
        data=pdf_bytes,
        file_name="Mpfuno_Clyde_Bilankulu_CV.pdf",
        mime="application/pdf",
        icon="📄",
    )

st.markdown("---")

# ── Higlights ────────────────────────────────────────────────────────────────

st.subheader("Key Highlights")

col1, col2 = st.columns(2)

with col1:
    st.info("🏗️ 2+ years in Data Engineering & BI")
    st.info("❄️ Leading Snowflake Migration")
    st.info("☁️ GCP & BigQuery Specialist")
    st.info("📊 Microsoft Certified Power BI Analyst")

with col2:
    st.info("⚙️ ETL & Data Warehouse Development")
    st.info("🚀 CI/CD, Docker & Cloud Run Deployments")
    st.info("🤝 Requirements Gathering & Stakeholder Management")
    st.info("💻 Python, SQL, Java & C# Development")

st.markdown("<br>", unsafe_allow_html=True)

st.divider()

# ── Experience ────────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">Experience</p>', unsafe_allow_html=True)
st.markdown("### Work History")
st.markdown("<br>", unsafe_allow_html=True)

experience = [
    {
        "role": "Junior Business Intelligence Developer",
        "company": "PSG Asset Management",
        "dates": "Nov 2025 – Present",
        "bullets": [
            "Leading the end-to-end migration of the on-premises data warehouse to Snowflake.",
            "Designing and developing scalable ETL pipelines for financial data migration and transformation.",
            "Implementing data quality, governance, metadata, and lineage frameworks across cloud data infrastructure.",
            "Developing SQL and scripting solutions to validate, transform, and optimize data workflows.",
            "Managing sprint delivery, backlog refinement, and source control through Azure DevOps.",
            "Applying data warehousing best practices and query performance optimization techniques.",
        ],
    },
    {
        "role": "Junior Data Engineer",
        "company": "Incubeta",
        "dates": "Jan 2025 – Oct 2025",
        "bullets": [
            "Delivered multiple cloud migration projects from on-premises systems to Google Cloud Platform.",
            "Designed and optimized BigQuery data warehouse schemas using dimensional modelling and star-schema techniques.",
            "Built and maintained ETL pipelines supporting real-time marketing analytics and reporting solutions.",
            "Developed business intelligence dashboards in Looker Studio and Power BI.",
            "Gathered business requirements and translated stakeholder needs into technical specifications.",
            "Implemented GA4 and GTM tracking solutions integrated with GCP data platforms.",
            "Supported UAT, deployment, and post-release monitoring of analytics solutions.",
        ],
    },
    {
        "role": "Data & Analytics Intern",
        "company": "Incubeta",
        "dates": "Jan 2024 – Dec 2024",
        "bullets": [
            "Conducted requirements gathering workshops with business and technical stakeholders.",
            "Implemented and tested analytics tracking using Google Analytics 4 and Google Tag Manager.",
            "Created process documentation, data flow diagrams, and reporting specifications.",
            "Performed QA testing and validation of dashboards and analytics solutions.",
            "Presented insights and reports to internal teams and external clients.",
        ],
    },
    {
        "role": "Information Systems Tutor",
        "company": "University of Cape Town",
        "dates": "Jan 2023 – Dec 2023",
        "bullets": [
            "Tutored Commercial Programming and Systems Design & Development modules.",
            "Mentored students in Java, software engineering principles, and systems analysis.",
            "Provided academic support and facilitated practical problem-solving sessions.",
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
    {"degree": "BSc Computer Science", "institution": "University of Cape Town", "year": "2024"}
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
    ("🏅", "Microsoft Power BI Associate", "2025")
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