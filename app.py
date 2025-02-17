import streamlit as st
import requests

BACKEND_URL = "https://yourapp.up.railway.app"

st.title("Image Resizer & X Poster")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Resize & Upload"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(f"{BACKEND_URL}/upload/", files=files)

        if response.status_code == 200:
            st.success("Image resized successfully!")
        else:
            st.error("Error resizing image.")
