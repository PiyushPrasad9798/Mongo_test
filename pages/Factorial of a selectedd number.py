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
    <h1 style='text-align:center;'>🧮 Factorial Calculator</h1>
    <h4 style='text-align:center;color:gray;'>
        Find the factorial of any number
    </h4>
    <hr>
    """,
    unsafe_allow_html=True,
)

# ---------------- Main Card ---------------- #

left, center, right = st.columns([1,2,1])

with center:

    n = st.slider(
        "Select a Number",
        min_value=1,
        max_value=100,
        value=5
    )

    if st.button("🧮 Calculate Factorial", use_container_width=True):

        fact = 1

        for i in range(1, n + 1):
            fact *= i

        st.success(f"🎉 Factorial of {n} = {fact:,}")

    st.divider()

    st.subheader("📄 Python Code")

    code = '''
n = int(input("Enter Number : "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)
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