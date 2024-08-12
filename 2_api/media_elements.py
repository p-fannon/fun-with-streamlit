import streamlit as st

st.header('Display image using st.image')
st.image('./media/image.jpg', caption='Such wow, many ahh', width=250)

st.header('Display video')
video_file = open('./media/waterfalls.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.header('Play audio')
audio_file = open('./media/audio.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')