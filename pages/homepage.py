import path_setup as path_setup
import streamlit as st

st.set_page_config(
    page_title="Clyde's Portfolio",
    page_icon="🖥️",
    layout="wide"
)

home     = st.Page("home.py",     title="Home",     icon="🏠", default=True)
projects = st.Page("projects.py", title="Projects", icon="📁")
about    = st.Page("about.py",    title="About",    icon="👤")
resume   = st.Page("resume.py",   title="Resume",   icon="📄")

pg = st.navigation([home, projects, about, resume])
pg.run()