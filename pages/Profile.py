import streamlit as st
import pymongo

from background import set_bg
set_bg()

# ---------------- MongoDB ----------------

conn = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb = conn["ojt"]
my = mydb["user_info"]

# ---------------- Login Check ----------------

username = st.session_state.get("username")

if not username:
    st.error("Please Sign In first to continue!")
    st.toast("Please Sign In first to continue!")

    if st.button("🔐 Go to Sign In"):
        st.switch_page("Sign_In.py")

    st.stop()

# ---------------- Get User ----------------

user = my.find_one({"uname": username})

if user is None:
    st.error("User not found.")
    st.stop()

# ---------------- Header ----------------

st.markdown(f"""<h2 style='text-align:center;'>👋 Welcome <span style='color:#4CAF50'>{username}</span></h2>""",unsafe_allow_html=True,)

st.write("")

st.markdown("<h1 style='text-align:center;'>👤 My Profile</h1>",unsafe_allow_html=True,)

st.write("")

# ---------------- Profile Card ----------------

with st.container(border=True):

    st.subheader("📋 Account Information")

    st.write(f"**👤 Username :** {user['uname']}")
    st.write(f"**🔒 Password :** {'*' * len(user['password'])}")
    st.write(f"**📱 Mobile :** {user['mobile']}")
    st.write(f"**📧 Email :** {user['email']}")
    st.write(f"**🎂 Date of Birth :** {user['dob']}")

st.write("")

# ---------------- Buttons ----------------

col1, col2 = st.columns(2)

with col1:
    if st.button("✏ Edit Profile", use_container_width=True):
        st.switch_page("pages/Edit Profile.py")

with col2:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("pages/Welcome.py")


# ---------------- Show Python Code ----------------
with st.expander("👀 Show Python Code"):
    with open(__file__, "r", encoding="utf-8") as f:
        st.code(f.read())