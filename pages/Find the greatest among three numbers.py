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
    <h1 style='text-align:center;'>🏆 Greatest Among Three Numbers</h1>
    <h4 style='text-align:center;color:gray;'>
        Compare Three Numbers and Find the Greatest
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
    num3 = st.number_input("Enter Third Number", value=0.0)

    if st.button("🔍 Find Greatest", use_container_width=True):

        # All numbers are equal
        if num1 == num2 == num3:
            st.info("🤝 All three numbers are equal.")

        # First and Second are equal & greatest
        elif num1 == num2 and num1 > num3:
            st.success(f"🏆 {num1} and {num2} are the Greatest Numbers")

        # First and Third are equal & greatest
        elif num1 == num3 and num1 > num2:
            st.success(f"🏆 {num1} and {num3} are the Greatest Numbers")

        # Second and Third are equal & greatest
        elif num2 == num3 and num2 > num1:
            st.success(f"🏆 {num2} and {num3} are the Greatest Numbers")

        # First is greatest
        elif num1 > num2 and num1 > num3:
            st.success(f"🏆 {num1} is the Greatest Number")

        # Second is greatest
        elif num2 > num1 and num2 > num3:
            st.success(f"🏆 {num2} is the Greatest Number")

        # Third is greatest
        else:
            st.success(f"🏆 {num3} is the Greatest Number")

    st.divider()

    st.subheader("📄 Python Code")

    code = '''
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
num3 = float(input("Enter Third Number: "))

if num1 == num2 == num3:
    print("All three numbers are equal.")

elif num1 == num2 and num1 > num3:
    print(num1, "and", num2, "are the greatest.")

elif num1 == num3 and num1 > num2:
    print(num1, "and", num3, "are the greatest.")

elif num2 == num3 and num2 > num1:
    print(num2, "and", num3, "are the greatest.")

elif num1 > num2 and num1 > num3:
    print(num1, "is the greatest.")

elif num2 > num1 and num2 > num3:
    print(num2, "is the greatest.")

else:
    print(num3, "is the greatest.")
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