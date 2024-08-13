import streamlit as st
import pandas as pd
import numpy as np
import os

# load data
data = pd.read_csv('tips.csv')

def display_data_random(df):
    sample = df.sample(5)
    return sample

# Button widget
st.subheader('Displaying random 5 rows')
st.caption('Click to view')
button = st.button('Display random 5 rows')
if button:
    sample = display_data_random(data)
    st.dataframe(sample)