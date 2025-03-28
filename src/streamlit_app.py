import streamlit as st

st.set_page_config(
    page_title="AI Assist",
    page_icon="images/sanctum.jpg",
    layout="wide"
)
st.logo("images/sanctum.jpg", size="large")

send_email = st.Page("task_email.py", title="Send Email", icon=":material/post:")
view_email = st.Page("view_email.py", title="Email List", icon=":material/post:")

home = st.Page("landing.py", title="Home", icon=":material/home:")


pg = st.navigation(
        {
            "Home": [home],
            "Task": [send_email],
            "View": [view_email]
        }
    )

pg.run()
