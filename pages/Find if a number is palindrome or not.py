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
    <h1 style='text-align:center;'>🔄 Palindrome Number Checker</h1>
    <h4 style='text-align:center;color:gray;'>
        Check whether a number is Palindrome or Not
    </h4>
    <hr>
    """,
    unsafe_allow_html=True,
)

# ---------------- Main ---------------- #

left, center, right = st.columns([1,2,1])

with center:

    number = st.slider(
        "Select a Number",
        1,
        1000,
        1
    )

    if st.button("🔍 Check Palindrome", use_container_width=True):

        temp = number
        rev = 0

        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp = temp // 10

        if rev == number:
            st.success(f"✅ {number} is a Palindrome Number")
        else:
            st.error(f"❌ {number} is NOT a Palindrome Number")

    st.divider()

    st.subheader("📄 Python Code")

    code = '''
number = int(input("Enter Number : "))

temp = number
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if reverse == number:
    print("Palindrome")
else:
    print("Not Palindrome")
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