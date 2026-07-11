import streamlit as st
import time
import pymongo

from datetime import date

from background import set_bg

# ------------------ Background ------------------
set_bg()

# ------------------ MongoDB ------------------
conn = pymongo.MongoClient(
    "mongodb+srv://PiyushPdMongo:Piyush9798@mongotest.norvsxv.mongodb.net/?retryWrites=true&w=majority&appName=MongoTest"
)
mydb = conn["ojt"]
my = mydb["user_info"]

# ------------------ Page ------------------
st.markdown(
    """
    <h1 style='text-align:center;'>📝 Create Your Account</h1>
    <h4 style='text-align:center;color:gray;'>
        Join the Python Learning Portal
    </h4>
    <hr>
    """,
    unsafe_allow_html=True,
)

# ------------------ Form ------------------

username = st.text_input("👤 Username")

password = st.text_input(
    "🔒 Password",
    type="password"
)

col1, col2 = st.columns(2)

with col1:
    mobile = st.text_input("📱 Mobile Number")

with col2:
    email = st.text_input("📧 Email Address")

# dob = st.date_input("🎂 Date of Birth")
dob=st.date_input("🎂 Date of Birth",value=date.today(),min_value=date(1900,1,1),max_value=date.today())

st.write("")

col1, col2 = st.columns(2)

with col1:
    signup = st.button(
        "📝 Create Account",
        use_container_width=True
    )

with col2:
    signin = st.button(
        "⬅ Back to Sign In",
        use_container_width=True
    )

# ------------------ Back Button ------------------

if signin:
    st.switch_page("Sign_In.py")

# ------------------ Signup ------------------

if signup:

    if not username or not password or not mobile or not email:

        st.error("Please fill all fields.")

    elif len(password) < 6:

        st.error("Password should contain at least 6 characters.")

    elif not mobile.isdigit() or len(mobile) != 10:

        st.error("Enter a valid 10 digit mobile number.")

    elif "@" not in email or "." not in email:

        st.error("Enter a valid Email Address.")

    else:

        user = my.find_one({"uname": username})

        if user:

            st.error("Username already exists.")

        else:

            my.insert_one({
                "uname": username,
                "password": password,
                "mobile": mobile,
                "email": email,
                "dob": str(dob)
            })

            st.success("🎉 Account Created Successfully!")

            st.balloons()

            with st.spinner("Redirecting to Sign In..."):

                time.sleep(2)

            st.switch_page("Sign_In.py")
