import streamlit as st

st.set_page_config(page_title="NeST Login", layout="centered")

logo_url = "https://learning.nestdigital.com/pluginfile.php/1/theme_edash/main_logo/1771222660/LogoNeST.png"

st.markdown("""
<style>
            
            /* Remove default Streamlit form border */
[data-testid="stForm"] {
    border: none !important;
    background: transparent !important;
}
/* Animated background */
.stApp {
    background: linear-gradient(-45deg, #1f3c88, #e63946, #3b82f6, #f1f1f1);
    background-size: 400% 400%;
    animation: gradientMove 12s ease infinite;
}

/* Animation */
@keyframes gradientMove {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}
            
label {
    color: white !important;
    font-weight: bold;
}           
            /* Error message styling */
.stAlert {
    background-color: rgba(255, 255, 255, 0.95) !important;
    border-left: 6px solid #e63946 !important;
    color: #b00020 !important;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# Center logo and heading
st.markdown(
    f"""
    <div style="text-align:center;">
        <img src="{logo_url}" width="300">
        <h2 style="color:white; margin-top:10px;">LOGIN PORTAL</h2>
    </div>
    """,
    unsafe_allow_html=True
)

USER_CREDENTIALS = {
    "admin": "1234",
    "user": "password"
}

st.markdown('<div class="login-box"><div class="login-inner">', unsafe_allow_html=True)



with st.form("login_form"):
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        username = st.text_input("Username/E-Mail")
        password = st.text_input("Password", type="password")

    # Center the login button
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,1,1,1,1,1,1])
    with col4:
        login_button = st.form_submit_button("LOGIN")

    st.markdown(
    "<p style='text-align:center; color:white;'>Don't have an account? "
    "<a href='/Sign_up' style='color:#ffd166; font-weight:bold;'>Sign up</a></p>",
    unsafe_allow_html=True
)

st.markdown('</div></div>', unsafe_allow_html=True)

if login_button:
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.success(f"Welcome {username}! Login Successful.")
    else:
        st.error("Invalid Username or Password")