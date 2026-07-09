import streamlit as st
from background import set_bg

set_bg()

# ---------------- LOGIN CHECK ----------------

if "username" not in st.session_state:
    st.error("Please Login First!")
    if st.button("🔐 Go to Sign In", use_container_width=True):
        st.switch_page("Sign_In.py")
    st.stop()

username = st.session_state["username"]

# ---------------- HEADER ----------------

st.markdown(
    f"""
    <h1 style='text-align:center;color:white;'>
        👋 Welcome <span style='color:#00FFD5'>{username}</span>
    </h1>
    """,
    unsafe_allow_html=True
)

st.caption("🚀 Basic Python Programming using Streamlit")

st.markdown("---")

# ---------------- DASHBOARD ----------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("👤 User", username)

with c2:
    st.metric("📚 Programs", "10")

with c3:
    st.metric("🔥 Status", "Online")

st.markdown("---")

st.subheader("🧮 Python Programs")

# Row 1
c1, c2, c3 = st.columns(3)

with c1:
    st.info("🔢 Factorial")
    if st.button("Open", key="factorial", use_container_width=True):
        st.switch_page("pages/Factorial of a selectedd number.py")

with c2:
    st.info("🔍 Prime Number")
    if st.button("Open", key="prime", use_container_width=True):
        st.switch_page("pages/Find a number is Prime or not.py")

with c3:
    st.info("🔁 Palindrome")
    if st.button("Open", key="palindrome", use_container_width=True):
        st.switch_page("pages/Find if a number is palindrome or not.py")

# Row 2
c1, c2, c3 = st.columns(3)

with c1:
    st.info("📅 Leap Year")
    if st.button("Open", key="leap", use_container_width=True):
        st.switch_page("pages/Find if a year is leap year or not.py")

with c2:
    st.info("💪 Armstrong")
    if st.button("Open", key="armstrong", use_container_width=True):
        st.switch_page("pages/Find if the number is armstrong or not.py")

with c3:
    st.info("🥇 Greatest Among Three")
    if st.button("Open", key="great3", use_container_width=True):
        st.switch_page("pages/Find the greatest among three numbers.py")

# Row 3
c1, c2, c3 = st.columns(3)

with c1:
    st.info("🥈 Greatest Among Two")
    if st.button("Open", key="great2", use_container_width=True):
        st.switch_page("pages/Find the greatest among two numbers.py")

with c2:
    st.info("📋 Multiplication Table")
    if st.button("Open", key="table", use_container_width=True):
        st.switch_page("pages/Generate a table of selected number.py")

with c3:
    st.info("⚡ Odd / Even")
    if st.button("Open", key="odd", use_container_width=True):
        st.switch_page("pages/Number is Odd or Even.py")

# Row 4
c1, c2 = st.columns(2)

with c1:
    st.info("🔄 Reverse Number")
    if st.button("Open", key="reverse", use_container_width=True):
        st.switch_page("pages/Reverse of a number.py")

with c2:
    st.info("👤 My Profile")
    if st.button("Open", key="profile", use_container_width=True):
        st.switch_page("pages/Profile.py")

st.markdown("---")

st.subheader("⚙️ Account")

col1, col2 = st.columns(2)

with col1:
    if st.button("✏️ Edit Profile", use_container_width=True):
        st.switch_page("pages/Edit Profile.py")

with col2:
    if st.button("🚪 Logout", use_container_width=True):
        del st.session_state["username"]
        st.switch_page("Sign_In.py")
code='''
import streamlit as st
from background import set_bg

set_bg()

# ---------------- LOGIN CHECK ----------------

if "username" not in st.session_state:
    st.error("Please Login First!")
    if st.button("🔐 Go to Sign In", use_container_width=True):
        st.switch_page("Sign_In.py")
    st.stop()

username = st.session_state["username"]

# ---------------- HEADER ----------------

st.markdown(
    f"""
    <h1 style='text-align:center;color:white;'>
        👋 Welcome <span style='color:#00FFD5'>{username}</span>
    </h1>
    """,
    unsafe_allow_html=True
)

st.caption("🚀 Basic Python Programming using Streamlit")

st.markdown("---")

# ---------------- DASHBOARD ----------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("👤 User", username)

with c2:
    st.metric("📚 Programs", "10")

with c3:
    st.metric("🔥 Status", "Online")

st.markdown("---")

st.subheader("🧮 Python Programs")

# Row 1
c1, c2, c3 = st.columns(3)

with c1:
    st.info("🔢 Factorial")
    if st.button("Open", key="factorial", use_container_width=True):
        st.switch_page("pages/Factorial of a selectedd number.py")

with c2:
    st.info("🔍 Prime Number")
    if st.button("Open", key="prime", use_container_width=True):
        st.switch_page("pages/Find a number is Prime or not.py")

with c3:
    st.info("🔁 Palindrome")
    if st.button("Open", key="palindrome", use_container_width=True):
        st.switch_page("pages/Find if a number is palindrome or not.py")

# Row 2
c1, c2, c3 = st.columns(3)

with c1:
    st.info("📅 Leap Year")
    if st.button("Open", key="leap", use_container_width=True):
        st.switch_page("pages/Find if a year is leap year or not.py")

with c2:
    st.info("💪 Armstrong")
    if st.button("Open", key="armstrong", use_container_width=True):
        st.switch_page("pages/Find if the number is armstrong or not.py")

with c3:
    st.info("🥇 Greatest Among Three")
    if st.button("Open", key="great3", use_container_width=True):
        st.switch_page("pages/Find the greatest among three numbers.py")

# Row 3
c1, c2, c3 = st.columns(3)

with c1:
    st.info("🥈 Greatest Among Two")
    if st.button("Open", key="great2", use_container_width=True):
        st.switch_page("pages/Find the greatest among two numbers.py")

with c2:
    st.info("📋 Multiplication Table")
    if st.button("Open", key="table", use_container_width=True):
        st.switch_page("pages/Generate a table of selected number.py")

with c3:
    st.info("⚡ Odd / Even")
    if st.button("Open", key="odd", use_container_width=True):
        st.switch_page("pages/Number is Odd or Even.py")

# Row 4
c1, c2 = st.columns(2)

with c1:
    st.info("🔄 Reverse Number")
    if st.button("Open", key="reverse", use_container_width=True):
        st.switch_page("pages/Reverse of a number.py")

with c2:
    st.info("👤 My Profile")
    if st.button("Open", key="profile", use_container_width=True):
        st.switch_page("pages/Profile.py")

st.markdown("---")

st.subheader("⚙️ Account")

col1, col2 = st.columns(2)

with col1:
    if st.button("✏️ Edit Profile", use_container_width=True):
        st.switch_page("pages/Edit Profile.py")

with col2:
    if st.button("🚪 Logout", use_container_width=True):
        del st.session_state["username"]
        st.switch_page("Sign_In.py")
'''
with st.expander("Show Python Code"):
    st.code(code)
