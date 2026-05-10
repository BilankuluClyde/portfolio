import streamlit as st

st.set_page_config(page_title="Projects | Clyde's Portfolio", page_icon="📁", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');
html, body, [class*="css"] { font-family: 'Syne', sans-serif; background-color: #0d0d0d; color: #f0ece2; }

.section-label {
    font-family: 'Space Mono', monospace; font-size: 0.7rem;
    letter-spacing: 4px; text-transform: uppercase; color: #c8b97a; margin-bottom: 0.5rem;
}
.project-card {
    background: #141414; border: 1px solid #2a2a2a;
    border-radius: 14px; padding: 1.8rem; margin-bottom: 1.2rem;
    transition: border-color 0.2s;
}
.project-card:hover { border-color: #c8b97a55; }
.project-title { font-size: 1.3rem; font-weight: 700; margin-bottom: 0.3rem; }
.project-desc { color: #888; font-size: 0.95rem; line-height: 1.7; margin-bottom: 1rem; }
.tag-pill {
    display: inline-block; background: #1e1e1e; border: 1px solid #c8b97a44;
    color: #c8b97a; font-family: 'Space Mono', monospace; font-size: 0.7rem;
    padding: 3px 12px; border-radius: 100px; margin: 3px 3px 3px 0;
}
.status-dot-green { display:inline-block; width:8px; height:8px; background:#4caf50; border-radius:50%; margin-right:6px; }
.status-dot-yellow { display:inline-block; width:8px; height:8px; background:#c8b97a; border-radius:50%; margin-right:6px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="section-label">Portfolio</p>', unsafe_allow_html=True)
st.markdown("# Projects")
st.markdown('<p style="color:#666; font-family:\'Space Mono\',monospace; font-size:0.8rem;">Things I\'ve built, broken, and rebuilt.</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Filter bar ───────────────────────────────────────────────────────────────
all_tags = ["All", "Python", "SQL", "BigQuery", "GCP", "Streamlit", "Automation", "Data Engineering"]
selected = st.selectbox("Filter by tech", all_tags, label_visibility="collapsed")

st.markdown("---")

# ── Project data — replace with your real projects ───────────────────────────
projects = [
    {
        "title": "Portfolio Dashboard",
        "desc": "This very site — a multi-page Streamlit app showcasing projects, skills, and resume. Deployed on Streamlit Community Cloud.",
        "tags": ["Python", "Streamlit"],
        "github": "https://github.com/YOUR_USERNAME/portfolio",
        "status": "live",
        "highlight": True,
    },
    {
        "title": "GitHub Repo Tracker",
        "desc": "Pulls repo metadata from the GitHub API and stores it in BigQuery for trend analysis across languages, stars, and commit activity.",
        "tags": ["Python", "BigQuery", "GCP", "SQL"],
        "github": "https://github.com/YOUR_USERNAME/repo-tracker",
        "status": "live",
        "highlight": False,
    },
    {
        "title": "Sales Pipeline Automation",
        "desc": "End-to-end ETL pipeline that ingests CRM exports, transforms them with dbt, and surfaces KPIs in a Looker Studio dashboard.",
        "tags": ["SQL", "BigQuery", "Automation", "Data Engineering"],
        "github": "https://github.com/YOUR_USERNAME/sales-pipeline",
        "status": "wip",
        "highlight": False,
    },
    # ── Add your real projects below this line ───────────────────────────────
]

for proj in projects:
    if selected != "All" and selected not in proj["tags"]:
        continue

    border_style = "border-color: #c8b97a55;" if proj.get("highlight") else ""
    dot = '<span class="status-dot-green"></span> Live' if proj["status"] == "live" else '<span class="status-dot-yellow"></span> In Progress'

    tag_html = "".join(f'<span class="tag-pill">{t}</span>' for t in proj["tags"])

    st.markdown(f"""
    <div class="project-card" style="{border_style}">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap;">
            <div class="project-title">{proj["title"]}</div>
            <div style="font-family:'Space Mono',monospace; font-size:0.72rem; color:#666;">{dot}</div>
        </div>
        <div class="project-desc">{proj["desc"]}</div>
        <div>{tag_html}</div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(f"View {proj['title']} on GitHub ↗", proj["github"])
    st.markdown("<br>", unsafe_allow_html=True)