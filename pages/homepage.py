import streamlit as st

st.title("My GitHub Portfolio ")

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
    },
    {
        "name": "Valentine Message",
        "description": "A playful, interactive web app that asks "
        "the user to be a valentine. The 'No' button cleverly evades "
        "the cursor, creating a fun and persistent user experience "
        "that leaves only one option: 'Yes' ❤️. "
        "\nBuilt with HTML, CSS, and JavaScript.",
        "language": "JavaScript",
        "url": "https://bilankuluclyde.github.io/"
    }
]

for proj in projects:
    st.subheader(proj["name"])
    st.write(proj["description"])
    st.write(f"**Language:** {proj['language']}")
    st.markdown(f"[View on GitHub]({proj['url']})")
    st.markdown("---")
