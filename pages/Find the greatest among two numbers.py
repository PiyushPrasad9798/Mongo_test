import streamlit as st
from background import set_bg

set_bg()

# ---------------- Login Check ---------------- #

username = st.session_state.get("username")

if not username:
    st.error("Please Sign In first to continue!")
    st.toast("Please Sign In first to continue!")

    if st.button("🔐 Go to Sign In"):
        st.switch_page("Sign_In.py")

    st.stop()

# ---------------- Header ---------------- #

st.markdown(
    f"""
    <h3 style='text-align:center;'>
        👋 Welcome <span style='color:#4CAF50'>{username}</span>
    </h3>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 style='text-align:center;'>
        🏆 Greatest Among Two Numbers
    </h1>
    <h4 style='text-align:center;color:gray;'>
        Compare Two Numbers Instantly
    </h4>
    <hr>
    """,
    unsafe_allow_html=True,
)

# ---------------- Main ---------------- #

left, center, right = st.columns([1, 2, 1])

with center:

    num1 = st.number_input("Enter First Number", value=0.0)
    num2 = st.number_input("Enter Second Number", value=0.0)

    if st.button("🔍 Find Greatest", use_container_width=True):

        if num1 > num2:
            st.success(f"🏆 {num1} is Greater")

        elif num2 > num1:
            st.success(f"🏆 {num2} is Greater")

        else:
            st.info("🤝 Both numbers are equal.")

    st.divider()

    st.subheader("📄 Python Code")

    code = '''
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if num1 > num2:
    print(num1, "is greater")

elif num2 > num1:
    print(num2, "is greater")

else:
    print("Both numbers are equal.")
'''

    with st.expander("👀 Show Python Code"):
        st.code(code, language="python")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("pages/Welcome.py")

    with col2:
        if st.button("🚪 Logout", use_container_width=True):
            del st.session_state["username"]
            st.switch_page("Sign_In.py")