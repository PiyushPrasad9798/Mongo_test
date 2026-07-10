import streamlit as st
import pymongo
import base64
import time

# ---------------- DATABASE ---------------- #

conn = pymongo.MongoClient(
    "mongodb+srv://PiyushPdMongo:Piyush9798@mongotest.norvsxv.mongodb.net/?retryWrites=true&w=majority&appName=MongoTest"
)
mydb = conn["ojt"]
my = mydb["user_info"]

# ---------------- PAGE ---------------- #

st.set_page_config(page_title="Python Learning Portal",page_icon="🚀",layout="centered")

# ---------------- BACKGROUND ---------------- #

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("background.jpg")

st.markdown(f"""<style>.stApp{{background:linear-gradient(rgba(0,0,0,.78),rgba(0,0,0,.78)),url("data:image/jpg;base64,{img}");background-size:cover;background-position:center;background-repeat:no-repeat;}}.block-container{{padding-top:1rem;max-width:700px;}}</style>""",unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.markdown("""<h1 style='text-align:center;color:white;font-size:46px;margin-bottom:0;'>🚀 Basic Python Learning Portal</h1>""",unsafe_allow_html=True)

st.markdown("""<h4 style='text-align:center;color:#C8C8C8;margin-top:-8px;margin-bottom:30px;'>Practice • Learn • Build</h4>""",unsafe_allow_html=True)

# ---------------- IMAGE ---------------- #

col1,col2,col3=st.columns([1,2,1])

with col2:
    st.image("logo.jpg",width=180)

st.markdown("""<h2 style='text-align:center;margin-top:10px;margin-bottom:20px;'>👋 Welcome Back</h2>""",unsafe_allow_html=True)

# ---------------- LOGIN ---------------- #

t1=st.text_input("👤 Username",placeholder="Enter Username")

t2=st.text_input("🔒 Password",type="password",placeholder="Enter Password")

signin=st.button("🚀 Sign In",use_container_width=True)

col1,col2=st.columns(2)

with col1:

    signup=st.button("📝 Sign Up",use_container_width=True)

with col2:

    forgot=st.button("🔑 Forgot Password",use_container_width=True)

st.markdown("<br>",unsafe_allow_html=True)

st.markdown("""<p style='text-align:center;color:gray;font-size:14px;'>Made with ❤️ using Streamlit & MongoDB</p>""",unsafe_allow_html=True)

# ---------------- LOGIN ---------------- #

if signin:

    if t1 == "" and t2 == "":
        st.error("⚠️Please enter a Username and Password.⚠️")
        st.toast("⚠️Please enter a Username and Password.⚠️")

    elif t1 == "":
        st.error("⚠️Please enter a Username.⚠️")
        st.toast("⚠️Please enter a Username.⚠️")

    elif t2 == "":
        st.error("⚠️Please enter a Password.⚠️")
        st.toast("⚠️Please enter a Password.⚠️")

    else:

        with st.spinner("Checking Credentials..."):
            time.sleep(1)

            user = my.find_one({"uname": t1,"password": t2})

        if user:

            st.session_state["username"] = user["uname"]
            st.session_state["password"] = user["password"]

            st.toast(f"👋 Welcome {user['uname']}")

            st.success("Login Successful!")

            time.sleep(0.8)

            st.switch_page("pages/Welcome.py")

        else:

            st.error("⚠️Invalid Username or Password!⚠️")
            st.toast("⚠️Invalid Username or Password!⚠️")

# ---------------- SIGN UP ---------------- #

if signup:
    st.switch_page("pages/SignUP.py")

# ---------------- FORGOT PASSWORD ---------------- #

if forgot:
    st.switch_page("pages/Forgot Password.py")

# ---------------- SIGNUP SUCCESS MESSAGE ---------------- #

if st.session_state.get("msg"):

    st.toast("🎉 Sign Up Successful!")

    st.success("Account Created Successfully.\nPlease Login.")

    del st.session_state["msg"]

# ---------------- EXTRA ---------------- #

st.write("")

st.caption("Version 1.0 • Python Programming Learning Portal")

# ---------------- SHOW CODE ---------------- #

with st.expander("👀 Show Python Code"):
    with open(__file__, "r", encoding="utf-8") as f:
        st.code(f.read())
