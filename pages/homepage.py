import streamlit as st
import pandas as pd

from navBar import next_page

st.set_page_config(
    page_title="Clyde's Portfolio Dashboard",  # Browser tab title
    page_icon="🖥️"  # Optional: emoji or image
)

st.markdown(
    """
    <h1 style="display: flex; align-items: center;">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="40" style="margin-right:10px;">
        GitHub Projects
    </h1>
    """,
    unsafe_allow_html=True
)

# Setup a hello message, Giving a brief bio about me and what i can do

st.write("""
         Hi there 🙋‍♂️, welcome to my ...

         """)
st.divider()


st.header("Github Repos")
st.button("Projects", on_click=next_page("projects"))

# Dynamically get a list of my top 5 recommended projects from BQ Table 
projects = pd.DataFrame().

for proj in projects:
    st.subheader(proj["name"])
    st.write(proj["description"])
    st.write(f"**Language:** {proj['language']}")
    st.markdown(f"[View on GitHub]({proj['url']})")
    st.markdown("---")

# show each project as a separate card 
# listing its name, Language, description, and link to Github
# For executable app, link their CR links