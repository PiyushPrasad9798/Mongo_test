import streamlit as st
import time
import pymongo
from background import set_bg

set_bg()

# ---------------- MongoDB Connection ----------------
conn = pymongo.MongoClient(
    "mongodb+srv://PiyushPdMongo:Piyush9798@mongotest.norvsxv.mongodb.net/?retryWrites=true&w=majority&appName=MongoTest"
)
mydb = conn["ojt"]
my = mydb["user_info"]

# ---------------- Check Login ----------------
username = st.session_state.get("username")

if not username:
    st.error("Please Sign in first to continue!!!!")
    st.toast("Please Sign in first to continue!!!!")

    if st.button("Get me to Sign In Page"):
        st.switch_page("Sign_In.py")

    st.stop()

# ---------------- Get User Data ----------------
user = my.find_one({"uname": username})

if user is None:
    st.error("User not found.")
    st.stop()

# ---------------- Page ----------------
st.subheader(f"Welcome {username}!!!!")
st.title("Edit Profile")

# Username (Read Only)
st.text_input("👤 Username",value=user["uname"],disabled=True)

# Editable Field
new_password = st.text_input("🔑 Password",value=user["password"],type="password")
new_mobile = st.text_input("📱 Mobile",value=user["mobile"])
new_email = st.text_input("📧 Email",value=user["email"])
new_dob = st.date_input("🎂 DOB",value=user["dob"],min_value=date(1900, 1, 1),max_value=date.today())
# ---------------- Save ----------------
if st.button("💾 Save Changes", use_container_width=True):

    if not new_password or not new_mobile or not new_email or not new_dob:
        st.error("Please fill all the fields.")
    else:
        my.update_one({"uname": username}, {"$set": {"password": new_password, "mobile": new_mobile, "email": new_email, "dob": str(new_dob)}})
        with st.spinner("Loading....."):
            st.success("Profile Updated Successfully!")
            st.toast("Changes Saved Successfully!")
            time.sleep(2)
        st.switch_page("pages/Profile.py")

# ---------------- Show Python Code ----------------#
with st.expander("👀 Show Python Code"):
    with open(__file__, "r", encoding="utf-8") as f:
        st.code(f.read())
