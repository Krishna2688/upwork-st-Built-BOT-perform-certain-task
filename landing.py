import streamlit as st
from streamlit_extras.bottom_container import bottom


# # Streamlit Landing Page

def main():
    st.logo("sanctum.jpg", size="large")

    # Header Section with Logo
    col1, col2 = st.columns([1, 12])
    with col1:
        st.image("logo.png", width=100)  # Replace 'path_to_logo.png' with the actual path to your logo image
    with col2:
        st.title("Welcome to Task Assist")
        # st.markdown("#### (Prototype Built for MINEMATICS Pvt Ltd.)")
        # st.markdown("### :orange[Your Task assistant Powered by AI!!!]")

    # Main Description with Bordered Box
    st.markdown(
        """
        <div style="border: 2px solid #4CAF50; padding: 15px; border-radius: 10px; background-color: #f0f0f0;">
            <p style="font-size: 16px;">Task Assist is your ultimate assistant for tasks. Leverage the power of our assist to automate your workflow and enhance productivity.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with bottom():
        st.write("**&copy; 2025 Sanctum Digital Solutions**")


main()