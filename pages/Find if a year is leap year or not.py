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
    <h1 style='text-align:center;'>📅 Leap Year Checker</h1>
    <h4 style='text-align:center;color:gray;'>
        Check whether a Year is Leap Year or Not
    </h4>
    <hr>
    """,
    unsafe_allow_html=True,
)

# ---------------- Main ---------------- #

left, center, right = st.columns([1,2,1])

with center:

    year = st.slider(
        "Select a Year",
        1,
        5000,
        2025
    )

    if st.button("🔍 Check Leap Year", use_container_width=True):

        if year % 400 == 0:
            st.success(f"✅ {year} is a Leap Year")

        elif year % 100 == 0:
            st.error(f"❌ {year} is NOT a Leap Year")

        elif year % 4 == 0:
            st.success(f"✅ {year} is a Leap Year")

        else:
            st.error(f"❌ {year} is NOT a Leap Year")

    st.divider()

    st.subheader("📄 Python Code")

    code = '''
year = int(input("Enter Year : "))

if year % 400 == 0:
    print("Leap Year")

elif year % 100 == 0:
    print("Not Leap Year")

elif year % 4 == 0:
    print("Leap Year")

else:
    print("Not Leap Year")
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