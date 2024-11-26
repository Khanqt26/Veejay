import streamlit as st
import datetime

st.set_page_config(page_title="Veejay's Biography", layout="centered")

# ---- Initialize Session State ----
if 'toggle_state' not in st.session_state:
    st.session_state.toggle_state = False
if 'name' not in st.session_state:
    st.session_state.name = "Veejay C. Casupas"
if 'about_me' not in st.session_state:
    st.session_state.about_me = (
        "Hi, I'm Veeajay! I love playing online games, sleeping, and cleaning the house and also cooking."
    )
if 'mybirthday' not in st.session_state:
    st.session_state.mybirthday = datetime.date(2006, 10, 3)

def toggle_button():
    st.session_state.toggle_state = not st.session_state.toggle_state

# ---- App Header ----
st.markdown(
    """
    <div style="text-align: center; font-size: 35px; font-weight: bold;">
        Veejay's Biography
    </div>
    """,
    unsafe_allow_html=True,
)

# ---- Main Content ----
tab1, tab2, tab3, tab4 = st.tabs(["Personal Info", "Hobbies & Achievements", "Social Media", "Education & Family"])

# ---- Tab 1: Personal Information ----
with tab1:
    st.subheader("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Full Name", st.session_state.name, key="name")
        st.date_input("Date of Birth", st.session_state.mybirthday, key="mybirthday")
        st.text_input("Place of Birth", st.session_state.get("birthplace", "Mabini, Mainit, Surigao Del Norte"), key="birthplace")
        st.text_input("Current Address", st.session_state.get("current_address", "Purok Rosal, Brgy.Quezon, Mainit, Surigao del Norte"), key="current_address")
    with col2:
        st.write(f"Age: {(datetime.date.today() - st.session_state.mybirthday).days // 365} years old")
        st.radio("Gender", ["Male", "Female"], index=0 if st.session_state.get("gender", "Male") == "Male" else 1, key="gender")
        st.text_area("About Me", st.session_state.about_me, key="about_me", height=172)

# ---- Tab 2: Hobbies & Achievements ----
with tab2:
    st.subheader("Hobbies & Achievements")
    col3, col4 = st.columns(2)
    with col3:
        st.text_area("Hobbies", st.session_state.get("hobbies", "- I Play online games\n- Cooking"), key="hobbies", height=100)
    with col4:
        if st.button("Toggle Achievements"):
            toggle_button()
        if st.session_state.toggle_state:
            st.text_area("Achievements", "- With Honors and NC II Holder of Computer System Servicing", height=100)
            st.text_area("Game Achievements",
                         "- Reached Mythical Immortal in Mobile Legends\n"
                         "- Champion in Intrums of Mobile Legends\n"
                         "- Obtained Hayabusa Shura\n"
                         "- Top 4 Surigao del Norte Fredrinn\n"
                         "- Top 1 Surigao del Norte with Hayabusa",
                         height=150)

# ---- Tab 3: Social Media ----
with tab3:
    st.subheader("Social Media")
    st.markdown(
        """
        <div style="text-align: center;">
            <a href="https://www.facebook.com/plyr.supervee?mibextid=ZbWKwL" target="_blank" style="margin-right: 20px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook" width="40" />
            </a>
            <a href="https://www.instagram.com/plyr_supervee/profilecard/?igsh=ZGdlNml6b3pvZWsx" target="_blank" style="margin-right: 20px;">
                <img src="https://cdn-icons-png.flaticon.com/128/174/174855.png" alt="Instagram" width="40" />
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---- Tab 4: Education & Family ----
with tab4:
    st.subheader("Education & Family")
    col5, col6 = st.columns(2)
    with col5:
        st.text_input("High School", st.session_state.get("high_school", "Mainit National High School"), key="high_school")
        st.text_input("Senior High School", st.session_state.get("senior_high_school", "Mainit National High School"), key="senior_high_school")
        st.text_input("College", st.session_state.get("college", "Surigao del Norte State University"), key="college")
    with col6:
        st.text_input("Mother's Name", st.session_state.get("mother_name", "Mirasol C. Casupas"), key="mother_name")
        st.date_input("Mother's Birthday", st.session_state.get("mother_bday", datetime.date(1984, 8, 26)), key="mother_bday")
        st.text_input("Father's Name", st.session_state.get("father_name", "Ermie P. Cajefe"), key="father_name")
        st.date_input("Father's Birthday", st.session_state.get("father_bday", datetime.date(1982, 2, 2)), key="father_bday")
