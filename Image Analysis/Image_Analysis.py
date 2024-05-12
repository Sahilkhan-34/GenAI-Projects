import streamlit as st 
import google.generativeai as genai
from PIL import Image
import matplotlib.pyplot as plt


key = "AIzaSyALIvB-IxfKhe0Zxzdii2TEqTmefMxPk5"
genai.configure(api_key=key)


# st.title("Application")
# st.text("Streamlit App")
# st.write("Hello this is Stramlit app")
# st.text_input("Name", "")
# st.button("Click")

st.header("Image Analytics")
img = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if img:
    st.image(Image.open(img))


prompt = st.text_input("Enter the Prompt")

if st.button("Get Response"):
    img = Image.open(img)
    model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
    response = model.generate_content([prompt,img])
    st.markdown(response.text)

# img = Image.open(r'C:\Users\sahil\OneDrive\Naresh IT Class\Grooming Class\GenAI Projets\Image Analysis\sneaker.jpg')
# st.write(plt.imshow(img))

