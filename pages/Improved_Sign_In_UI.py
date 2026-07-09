# Improved UI section for Sign_In.py
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<h1 style='text-align:center;color:white;font-size:48px;font-weight:bold;'>
🚀 Basic Python Learning Portal
</h1>
<h4 style='text-align:center;color:#C0C0C0;margin-top:-15px;'>
Practice • Learn • Build
</h4>
""", unsafe_allow_html=True)

left, center, right = st.columns([3,2,3])

with center:
    st.image("logo.jpg", width=180)
    st.markdown(
        "<h3 style='text-align:center;'>Welcome Back 👋</h3>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    username = st.text_input(
        "👤 Username",
        placeholder="Enter your username"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        placeholder="Enter your password"
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        signin = st.button("🚀 Sign In", use_container_width=True)

    with c2:
        signup = st.button("📝 Sign Up", use_container_width=True)

    with c3:
        forgot = st.button("🔑 Forgot", use_container_width=True)

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;color:gray;'>
Made with ❤️ using Streamlit & MongoDB
</div>
""",
unsafe_allow_html=True)

# Replace the variables (username, password, signin, signup, forgot)
# with your existing MongoDB login logic.
