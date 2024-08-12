import streamlit as st
import time

## progress bar
st.header('st.progress')
st.caption('Display a progress bar')

def progress_bar():
    for pct_complete in range(1, 121, 20):
        time.sleep(0.5)
        pct_complete = min(pct_complete, 100)
        my_bar.progress(pct_complete)

## spinner
with st.spinner('Waiting for data'):
    my_bar = st.progress(0)
    progress_bar()

# info
st.subheader('st.info')
st.info('Info about the app status')

st.subheader('st.success')
st.success('This is a success')

st.subheader('st.warning')
st.warning('Watch out!')

st.subheader('st.error')
st.error('Uh oh!')

time.sleep(2)
st.balloons()