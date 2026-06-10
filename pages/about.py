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

st.markdown("# About Me")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("""
    I'm a **Data Engineer and Business Intelligence Developer** based in **Cape Town, South Africa** with over two years of experience designing and building cloud-based data solutions.

    My experience spans **data engineering, business intelligence, cloud migrations, analytics, and business analysis**. I've worked with technologies such as **Snowflake, Google Cloud Platform (GCP), BigQuery, Power BI, Looker Studio, Python, SQL, and Azure DevOps** to deliver scalable data platforms, ETL pipelines, reporting solutions, and analytics products.

    Currently, I'm helping lead an enterprise data warehouse migration at my current company. Previously at Incubeta, I delivered cloud migration projects, built real-time analytics pipelines, developed business intelligence dashboards, and partnered with stakeholders to translate business requirements into technical solutions.

    Beyond my professional work, I enjoy building personal projects that combine software engineering, cloud computing, and data analytics, including cloud-native applications, automation tools, and portfolio projects deployed on Google Cloud Platform / Azure.

    I'm always interested in opportunities involving **Data Engineering, Business Intelligence, Business Analysis, Cloud Engineering, and Software Development**.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<p class="section-label">Education & Certifications</p>',
        unsafe_allow_html=True
    )

    st.markdown("""
    - 🎓 **BCom Information Systems & Computer Science** — University of Cape Town
    - 🎓 **BSc Mathematics & Statistics** *(In Progress)* — University of South Africa
    - 📊 **Microsoft Certified: Power BI Data Analyst Associate**
    - 🏆 **1st Place - IITPSA SIGCyber Challenge**
    - 🏆 **Young Economist of the Year Finalist**
    """)

with col2:
    st.markdown(
        '<p class="section-label">Contact</p>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div style="font-family:'Space Mono',monospace; font-size:0.9rem; line-height:2.2; color:#888;">

    📧 clydebilam@gmail.com<br>
    🔗 <a href="https://www.linkedin.com/in/mpfuno-clyde-bilankulu" target="_blank">
    LinkedIn
    </a><br>
    🖥️ <a href="https://github.com/BilankuluClyde" target="_blank">
    GitHub
    </a><br>
    🚀 <a href="https://clydeporfolio-1071943451851.africa-south1.run.app" target="_blank">
    Portfolio Website
    </a>
    <br>🌍 Cape Town, South Africa<br>
    💼 Open to Data Engineering, BI, BA & Software Engineering Opportunities<br>
    </div>
    """, unsafe_allow_html=True)
st.divider()

# ── Skills ────────────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">Skills</p>', unsafe_allow_html=True)
st.markdown("### Technical Expertise")
st.markdown("<br>", unsafe_allow_html=True)

skills = {
    "SQL": 95,
    "Python": 90,
    "Java": 70,
    "C#": 70,
    "Power BI": 90,
    "Google BigQuery": 90,
    "Google Cloud Platform": 65,
    "Snowflake": 85,
    "Looker Studio": 95,
    "Data Warehousing": 85,
    "ETL / ELT": 85,
    "Azure DevOps": 70,
    "Git & CI/CD": 80,
    "Business Analysis": 80,
    "Streamlit": 80,
    "Google Analytics 4": 75,
    "Google Tag Manager": 75,
    "dbt": 70,
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
        <div class="skill-bar-bg">
            <div class="skill-bar-fill" style="width:{pct}%"></div>
        </div>
        """, unsafe_allow_html=True)


st.divider()

# ── Beyond the Keyboard ──────────────────────────────────────────────────────
st.markdown('<p class="section-label">Beyond the keyboard</p>', unsafe_allow_html=True)
st.markdown("### Interests & Passions")
st.markdown("<br>", unsafe_allow_html=True)

hobbies = [
    (
        "🚀",
        "Building Side Projects",
        "I enjoy turning ideas into working products, from cloud-native applications to data-driven tools."
    ),
    (
        "📊",
        "Data & Analytics",
        "Exploring patterns, solving business problems, and finding insights hidden in data."
    ),
    (
        "📚",
        "Continuous Learning",
        "Currently expanding my knowledge in cloud engineering, business analysis, and advanced data engineering."
    ),
    (
        "🤝",
        "Teaching & Mentorship",
        "Former UCT tutor who enjoys helping others understand technology and grow their careers."
    ),
]

cols = st.columns(len(hobbies))

for col, (icon, title, desc) in zip(cols, hobbies):
    with col:
        st.markdown(f"""
        <div class="hobby-card">
            <div style="font-size:2.5rem">{icon}</div>
            <div style="font-weight:700; margin:.6rem 0 .4rem">{title}</div>
            <div style="color:#666; font-size:0.85rem">{desc}</div>
        </div><br>
        """, unsafe_allow_html=True)