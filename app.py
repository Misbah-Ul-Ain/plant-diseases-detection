import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the trained model
model = load_model('plant_diseases_detection_model.h5')

# Define the class names
class_names = ['Healthy', 'Powdery', 'Rust']

# Function to process the uploaded image
def process_image(img, target_size=(224, 224)):
    img = img.resize(target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize to [0, 1]
    return img_array

# Streamlit app
st.title("Plant Disease Detection")
st.write("Upload an image of a plant leaf to detect if it is healthy or affected by Powdery or Rust.")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    processed_img = process_image(img)
    pred = model.predict(processed_img)
    pred_class = np.argmax(pred)

    st.write(f"Prediction: {class_names[pred_class]}")

# No need to include st.run(), Streamlit automatically handles the running of the app.

