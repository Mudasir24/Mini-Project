import streamlit as st

# Set dark theme
st.set_page_config(page_title="Bidirectional Sign Language Communication System", page_icon="🖐️", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }
        .subtitle {
            font-size: 22px;
            text-align: center;
        }
        .section {
            padding: 20px;
            border-radius: 10px;
            background-color: #1E1E1E;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Homepage Content

st.markdown("<h1 class='title'>Bidirectional Sign Language Communication System</h1>", unsafe_allow_html=True)
st.markdown("<h5 class='subtitle'>Breaking Barriers Between Sign Language Users and Non-Signers</h5>", unsafe_allow_html=True)

    # # Placeholder for logo/image
    # st.image("your_logo.png", use_column_width=True)  # Replace with actual file path

# Introduction Section
st.markdown("<div class='section'><h3>🔹 Introduction</h3><p>This system enables real-time bidirectional communication between sign language users and non-signers by translating hand gestures into text and speech, and vice versa.</p></div>", unsafe_allow_html=True)

# How It Works
st.markdown("<div class='section'><h3>⚙️ How It Works</h3><ul><li>Signers can gesture, and the system will translate them into text and speech.</li><li>Non-signers can speak, and the system will generate the corresponding sign visuals.</li></ul></div>", unsafe_allow_html=True)

# How to Use
st.markdown("<div class='section'><h3>📌 How to Use</h3><ol><li>Select 'Live Gesture Recognition' to translate sign language.</li><li>Select 'Speech-to-Sign Translation' to convert speech into signs.</li><li>Adjust settings for better accuracy.</li></ol></div>", unsafe_allow_html=True)

# Model & Technology
st.markdown("<div class='section'><h3>🧠 Model & Technology</h3><p>This system leverages machine learning models trained on hand landmarks and CNN-based recognition for accurate interpretation.</p></div>", unsafe_allow_html=True)

# Contact & Credits
st.markdown("<div class='section'><h3>Credits</h3><p> <h5>Team Name: <b>TECH MAVERICKS</b></h5> <h5>Team Members</h5><ul><li>Mohammed Mudasir Ahmed</li><li>Ozair Ali</li> <li>Syed Ibrahim Ali</li></ul><br> </p></div>", unsafe_allow_html=True)
