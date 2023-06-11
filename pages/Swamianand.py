import time
import streamlit as st
from streamlit.components.v1 import html
import os
import requests
import re
from PIL import Image
import base64
import io
import openai
import json

openai.api_key = ""

# Change the color of the sidebar
st.markdown(
    """
    <style>
    .css-1aumxhk {
        background-color: #f0f0f0;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    </style>
    """,
    unsafe_allow_html=True,
    )
def get_answer(query):
    messages = [
        {"role": "system", "content": "You're Swami Anand, an AI bot representing an 80-year-old monk, here to impart brief but insightful wisdom and life advice rooted in Indian culture. Answer in 2 sentences."},
          ]
    if query:
      messages.append(
              {"role": "user", "content": query},
      )

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )  
    return chat_completion.choices[0].message.content


def page5(ans):
    


    url = "https://api.d-id.com/talks"

    payload = {
        "script": {
            "type": "text",
            "subtitles": "false",
            "provider": {
                "type": "amazon",
                "voice_id": "Matthew"
            },
            "ssml": "false",
            "input": ans
        },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0"
        },
        "source_url": "https://res.cloudinary.com/dz1lt2wwz/image/upload/v1686463593/Narayan_200_200_px_250_250_px_3_r2t0bx.png"
    }


    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoidGFsa3MiLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmQtaWQuY29tLyIsInN1YiI6ImF1dGgwfDY0ODU1YmJlZmIzMmJhZjNjNmI2OGFhZiIsImF1ZCI6WyJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY4NjQ2MTQ0NywiZXhwIjoxNjg2NTQ3ODQ3LCJhenAiOiJHenJOSTFPcmU5Rk0zRWVEUmYzbTN6M1RTdzBKbFJZcSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgcmVhZDpjdXJyZW50X3VzZXIgdXBkYXRlOmN1cnJlbnRfdXNlcl9tZXRhZGF0YSBvZmZsaW5lX2FjY2VzcyJ9.NqlueVxQRkBy8VxpbGBhCLQDMmSWBPWE5bGDIvcT5WBruhuBq3xguTZTm0m7ucz_U2-pCV-JX2Dih2cFHKKSeow__ttosRtPZK7oo2eyZvVegXapgMmz4x0t4rOm1kAdteBmXz0254mkl1HgdiDppEVH8rZ7bJ9klSEMqgoJnXas1VgisyNpNLdsRdemj_bHPH-13kqtHBsv7F0l96Zvrn1B7a0bpefFFi8tKzKX-DJ5X7dwQOuKpbI_tYJsfbMSCFtvQHzFiT8eLdb8QLnko1k485mEk4SnLBzMjvEZfWt8lTT3Re2D5uOTNDwz_D13MeaB6PunqkY-9IOTRZtnUg"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    dict_data = json.loads(response.text)
    d_id = dict_data['id']

    #print(response.text)
    #st.write(response.text)
    #d_id = "tlk_t2bTA55WHDaBVExHbSGbi"
    #st.write(response.text)
    print(d_id)

    time.sleep(10)

    url = f"https://api.d-id.com/talks/{d_id}"
    print(url)

    headers = {
        "accept": "application/json",
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoidGFsa3MiLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmQtaWQuY29tLyIsInN1YiI6ImF1dGgwfDY0ODU1YmJlZmIzMmJhZjNjNmI2OGFhZiIsImF1ZCI6WyJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY4NjQ2MTQ0NywiZXhwIjoxNjg2NTQ3ODQ3LCJhenAiOiJHenJOSTFPcmU5Rk0zRWVEUmYzbTN6M1RTdzBKbFJZcSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgcmVhZDpjdXJyZW50X3VzZXIgdXBkYXRlOmN1cnJlbnRfdXNlcl9tZXRhZGF0YSBvZmZsaW5lX2FjY2VzcyJ9.NqlueVxQRkBy8VxpbGBhCLQDMmSWBPWE5bGDIvcT5WBruhuBq3xguTZTm0m7ucz_U2-pCV-JX2Dih2cFHKKSeow__ttosRtPZK7oo2eyZvVegXapgMmz4x0t4rOm1kAdteBmXz0254mkl1HgdiDppEVH8rZ7bJ9klSEMqgoJnXas1VgisyNpNLdsRdemj_bHPH-13kqtHBsv7F0l96Zvrn1B7a0bpefFFi8tKzKX-DJ5X7dwQOuKpbI_tYJsfbMSCFtvQHzFiT8eLdb8QLnko1k485mEk4SnLBzMjvEZfWt8lTT3Re2D5uOTNDwz_D13MeaB6PunqkY-9IOTRZtnUg"
    }

    response = requests.get(url, headers=headers)
    print(response.text)
    dict_data = json.loads(response.text)
    output_url = dict_data['result_url']
    print(output_url)
    col1, col2, col3 = st.beta_columns([1,6,1])

    # Play the video in the middle column
    col2.video(output_url)


def page2(ans):
    video_file = open('test.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
    
    video_url = 'https://d-id-talks-prod.s3.us-west-2.amazonaws.com/google-oauth2%7C108103079505217377816/tlk_dAimNc6UTHvcsr-Ns8D1O/1686456673111.mp4?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1686543075&Signature=e4kgER3aJH8pDvjmlwP%2FUFuntjo%3D&X-Amzn-Trace-Id=Root%3D1-64854963-52be85ad1f93a09c4cc9aed9%3BParent%3D654792415d011920%3BSampled%3D1%3BLineage%3D6b931dd4%3A0'

    # Play the video
    st.video(video_url)

    
           
            
def page3():
    st.title("Answer")
    with st.spinner("Generating....."):
        if query != "":
            print(f"query: {query}")
            
            ans = get_answer(query) 
            st.write(ans)
            page5(ans)
            #page2(ans)
        
bg_color = "#0B4B6F"  # Change this to the desired hex code
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
    }}
    </style>
    """, unsafe_allow_html=True)
st.write("\n\n\n")
st.markdown(
    """
    <style>
    <link href='https://fonts.googleapis.com/css?family=Lexend' rel='stylesheet'>
    html, body, [class*="css"] {
    font-family: 'Lexend', sans-serif; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("""
        <style>
        .css-15zrgzn {display: none}
        </style>
        """, unsafe_allow_html=True)
CSS = """
<style>
    @media (max-width: 600px) {
        .row {
            flex-direction: column;
        }
        .col1 {
            margin-bottom: 20px;
        }
        .col2 {
            margin-left: 0;
        }
    }
    .col1 {
        flex: 1;
        margin-right: 20px;
    }
    .col2 {
        flex: 9;
        margin-left: 20px;
    }
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.small-font {
    font-size:10px !important;
}
</style>
""", unsafe_allow_html=True)
bg_color = "#3F378E"
st.markdown(f"""
    <style>
    div.stButton > button {{
        background-color: {bg_color};
        color: black;
    }}
    </style>
""", unsafe_allow_html=True)


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://res.cloudinary.com/dz1lt2wwz/image/upload/v1686461265/WhatsApp_Image_2023-06-11_at_10.56.41_AM_1_oeayyh.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


query = st.text_input(label="", value="",key='input-box',placeholder="Ask questions like - why do i constantly feel pain?", args=('input-box',))
if st.button('Ask!', use_container_width = True,key='page3_button'):
    page3()


with st.sidebar:
    sidebar_bg_color = "#2EB454"
    # Set theme style
    theme_style = f"""
        <style>
        .sidebar .sidebar-content {{
            background-color: {sidebar_bg_color};
        }}
        </style>
        """
    st.markdown(theme_style, unsafe_allow_html=True)
    st.markdown("""
        <style>
        body {
            color: #3F378E;
            background-color: #111;
        }
        </style>
    """, unsafe_allow_html=True)
    bg_color = "#2EB454"
    new_title = '<p style="font-family:sans-serif; color: #3F378E; font-size: 30px;">About Suvidha.ai</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('<p style="color: #3F378E" >Suvidha.ai is an AI-powered platform in India that democratizes knowledge and streamlines hiring. By delivering personalized learning and intelligently matching experts to tasks, it converts AI disruption into job creation opportunities, ensuring a rewarding experience for all users.</p>', unsafe_allow_html=True)
    css = '''
    <style>
        .sidebar .sidebar-content {
            background-color: {sidebar_bg_color};
        }
        button {
            background-color: #3F378E;
            color: white;
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 0.25rem;
            font-size: 1rem;
            display: inline-block;
            margin-left: 3rem;
        }
    </style>
    '''

    st.markdown(css, unsafe_allow_html=True)
