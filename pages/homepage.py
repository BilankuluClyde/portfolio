import streamlit as st

st.set_page_config(
    page_title="Clyde's Portfolio Dashboard",  # Browser tab title
    page_icon="🖥️"  # Optional: emoji or image
)
# st.title("My GitHub Portfolio ")
st.markdown(
    """
    <h1 style="display: flex; align-items: center;">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="40" style="margin-right:10px;">
        GitHub Projects [Updates coming soon]
    </h1>
    """,
    unsafe_allow_html=True
)
# Static example project data  will update 
projects = [
    {
        "name": "Project Alpha",
        "description": "A cool project about AI.",
        "language": "Python",
        "url": "https://github.com/BilankuluClyde/content_calendar"
    },
    {
        "name": "Project Beta",
        "description": "An awesome web app.",
        "language": "JavaScript",
        "url": "https://github.com/BilankuluClyde/weather_in_my_area"
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
