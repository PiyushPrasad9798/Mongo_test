import streamlit as st
import pymongo
import time

from background import set_bg

# ---------------- Background ---------------- #

set_bg()

# ---------------- MongoDB ---------------- #

conn = pymongo.MongoClient("mongodb+srv://PiyushPdMongo:Piyush@123@mongotest.norvsxv.mongodb.net/?appName=MongoTest")
mydb = conn["ojt"]
my = mydb["user_info"]

# ---------------- Session State ---------------- #

if "show_reset" not in st.session_state:
    st.session_state.show_reset = False

# ---------------- Header ---------------- #

st.markdown("""<h1 style='text-align:center;'>🔐 Forgot Password</h1> <h4 style='text-align:center;color:gray;'> Reset your account password </h4> <hr>""", unsafe_allow_html=True,)

left, center, right = st.columns([1, 2, 1])
with center:

    username = st.text_input("👤 Username", placeholder="Enter your username")
    st.write("")

    # ---------------- Check Username ---------------- #

    if st.button("🔍 Verify Username", use_container_width=True):

        if username == "":
            st.error("Please enter your username.⚠️")

        else:

            user = my.find_one({"uname": username})

            if user is None:
                st.error("Username not found.⚠️")

            else:
                st.success("Username Verified ✅")
                st.session_state.show_reset = True

    # ---------------- Reset Password ---------------- #

    if st.session_state.show_reset:

        st.divider()

        new_password = st.text_input("🔒 New Password",type="password")

        confirm_password = st.text_input("🔒 Confirm Password",type="password")

        if st.button("✅ Update Password", use_container_width=True):

            if new_password == "" or confirm_password == "":
                st.error("Please fill all fields.⚠️")

            elif new_password != confirm_password:
                st.error("Passwords do not match.⚠️")

            else:

                result = my.update_one({"uname": username},{"$set": {"password": new_password}})

                if result.modified_count == 1:

                    st.success("🎉 Password Updated Successfully!")

                    with st.spinner("🚀Redirecting to Sign In..."):
                        time.sleep(2)

                    st.session_state.show_reset = False
                    st.switch_page("Sign_In.py")

                else:
                    st.warning("New password is the same as the old password.")

    st.write("")
    st.divider()

    if st.button("⬅ Back to Sign In", use_container_width=True):
        st.switch_page("Sign_In.py")


with st.expander("👀 Show Python Code"):
    with open(__file__, "r", encoding="utf-8") as f:
        st.code(f.read())
