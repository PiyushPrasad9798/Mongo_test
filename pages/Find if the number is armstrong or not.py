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
    <h1 style='text-align:center;'>💪 Armstrong Number Checker</h1>
    <h4 style='text-align:center;color:gray;'>
        Check whether a Number is Armstrong or Not
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
        153
    )

    if st.button("🔍 Check Armstrong", use_container_width=True):

        temp = number
        total = 0

        while temp > 0:
            digit = temp % 10
            total += digit ** 3
            temp //= 10

        if total == number:
            st.success(f"✅ {number} is an Armstrong Number")
        else:
            st.error(f"❌ {number} is NOT an Armstrong Number")

    st.divider()

    st.subheader("📄 Python Code")

    code = '''
number = int(input("Enter Number : "))

temp = number
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

if total == number:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
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