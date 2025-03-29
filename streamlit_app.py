import streamlit as st

st.set_page_config(
    page_title="AI Assist",
    page_icon="sanctum_t_l.png",
    layout="wide"
)

st.logo("sanctum_t_l.png", size="large")

send_email = st.Page("task_email.py", title="Send Email", icon="📨")
view_email = st.Page("view_email.py", title="Email List", icon="🔍")

home = st.Page("landing.py", title="Home", icon=":material/home:")


pg = st.navigation(
        {
            "🏠Home": [home],
            "✅Task": [send_email],
            "👁View": [view_email]
        }
    )

pg.run()
