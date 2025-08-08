import streamlit as st

st.title("My GitHub Portfolio - Proof of Concept")

# Static example project data
projects = [
    {
        "name": "Project Alpha",
        "description": "A cool project about AI.",
        "language": "Python",
        "url": "https://github.com/yourusername/project-alpha"
    },
    {
        "name": "Project Beta",
        "description": "An awesome web app.",
        "language": "JavaScript",
        "url": "https://github.com/yourusername/project-beta"
    }
]

for proj in projects:
    st.subheader(proj["name"])
    st.write(proj["description"])
    st.write(f"**Language:** {proj['language']}")
    st.markdown(f"[View on GitHub]({proj['url']})")
    st.markdown("---")
