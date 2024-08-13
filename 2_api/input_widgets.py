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

# checkbox
st.markdown('---')
st.subheader('st.checkbox')
agree = st.checkbox('I agree to T&C') # returns boolean value
st.write('checkbox status = ', agree)

# multiple checkbox
with st.container():
    st.info('What tech you know')

    python = st.checkbox('Python')
    data_science = st.checkbox('Data Science')
    ai_ml = st.checkbox('AI/ML')
    android = st.checkbox('Android')
    react = st.checkbox('React')
    java = st.checkbox('Java')
    javascript = st.checkbox('Javascript')
    tech_button = st.button('Submit')
    if tech_button:
        tech_dict = {
            'Python': python,
            'Data Science': data_science,
            'AI/ML': ai_ml,
            'Android': android,
            'React': react,
            'Java': java,
            'Javascript': javascript
        }
        st.json(tech_dict)

# radio button
st.markdown('---')
st.subheader('st.radio')

radio_button = st.radio('Your favorite color?',
                        ('white', 'black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple'))

st.write('Your favorite color is ', radio_button)

# selectbox
st.markdown('---')
st.subheader('st.selectbox')

select_box = st.selectbox('What skill do you want to learn most?',
                          ('Java', 'C', 'C++', 'Javascript', 'HTML', 'Other'))

st.write('You selected ', select_box)