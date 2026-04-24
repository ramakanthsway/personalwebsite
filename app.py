import streamlit as st
import streamlit.components.v1 as components
import os
import base64

st.set_page_config(
    page_title="Ramakanth Padala | Engineering Manager, Data & AI",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide all Streamlit chrome (header, footer, menu)
st.markdown("""
<style>
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    .stApp { margin: 0; padding: 0; }
    [data-testid="stToolbar"] { display: none; }
    [data-testid="collapsedControl"] { display: none; }
</style>
""", unsafe_allow_html=True)

# Load the HTML file
html_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Embed photo as base64 if photo.jpg exists in the same directory
photo_path = os.path.join(os.path.dirname(__file__), "photo.jpg")
if os.path.exists(photo_path):
    with open(photo_path, "rb") as img_file:
        photo_b64 = base64.b64encode(img_file.read()).decode("utf-8")
    html_content = html_content.replace("PHOTO_PLACEHOLDER", f"data:image/jpeg;base64,{photo_b64}")

# Render full-page HTML
components.html(html_content, height=9500, scrolling=False)
