import streamlit as st
import base64

def set_bg():
    with open("background.jpg", "rb") as f:
        img = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
                linear-gradient(
                    rgba(0,0,0,0.8),
                    rgba(0,0,0,0.8)
                ),
                url("data:image/jpg;base64,{img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
