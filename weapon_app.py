import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.title("Weapon_X-Ray_Detection")

model = YOLO("best.pt")

uplaoded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "pnh"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", width=300)
    
    if st.button("Submit"):
        with st.spinner("Detecting..."):
            results = model.predict(img)
        st.image(results[0].plot()[...,::-1], caption="Detection Result")