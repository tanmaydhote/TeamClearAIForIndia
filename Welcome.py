from PIL import Image
import streamlit as st
import requests

# Set the URLs for the images and their respective links
image_urls = ["https://res.cloudinary.com/dz1lt2wwz/image/upload/v1686458088/1_slnb4o.png", "https://res.cloudinary.com/dz1lt2wwz/image/upload/v1686458088/2_ftgttr.png", 
              "https://res.cloudinary.com/dz1lt2wwz/image/upload/v1686458088/3_wc8lif.png", "https://res.cloudinary.com/dz1lt2wwz/image/upload/v1686458088/4_wx7byl.png"]
links = ["http://localhost:8501/Kiran", "http://localhost:8501/Narayan", 
         "http://localhost:8501/Swamianand", "http://localhost:8501/Mary"]

# Create a column to display the images
cols = st.columns(4)

for i in range(4):
    # Download the image
    image = Image.open(requests.get(image_urls[i], stream=True).raw)
    
    # Display the image in the column as a clickable link
    cols[i].markdown(f'<a href="{links[i]}" target="_blank">![Image]({image_urls[i]})</a>', unsafe_allow_html=True)


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://res.cloudinary.com/dz1lt2wwz/image/upload/v1686459809/WhatsApp_Image_2023-06-11_at_10.32.45_AM_o1fusp.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 