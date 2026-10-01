# 🔫 Weapon Detection using YOLOv11 (X-Ray Images)

A simple web app that finds weapons in X-ray baggage images using a YOLOv11 model.

You upload an X-ray image. The app looks at it and shows where the weapon is.

👉 [Live Demo](https://weapon-detection-x-ray-images-yolo.streamlit.app/)

---

## ⚠️ Important Note

This project is for **learning and study only**.
It is **not a real security system**. Do not use it for real airport or border checks.

---

## What It Does

- Lets you upload an X-ray image
- Shows the image you uploaded
- Runs the YOLOv11 model on it
- Shows the result with boxes around the detected weapons

---

## Tools Used

- **Python**
- **YOLOv11** (Ultralytics) for detection
- **Streamlit** for the web app
- **OpenCV** and **Pillow** for working with images
- **PyTorch** to run the model

---

## Dataset

The model was trained on a labeled X-ray baggage dataset from **Roboflow Universe**.
Add the dataset name and link here.

X-Ray Baggage Computer Vision Model [Link](https://universe.roboflow.com/vladutc/x-ray-baggage/dataset/3)
---

## Files in This Project

| File | What it is |
|------|------------|
| `weapon_app.py` | The main Streamlit app |
| `best.pt` | The trained YOLOv11 model |
| `requirements.txt` | Python libraries the app needs |
| `packages.txt` | System packages needed for OpenCV on Streamlit Cloud |

---

## Author

Made by **Azizullah Asad**
