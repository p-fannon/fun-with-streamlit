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

# multiselect
st. markdown('---')
st.subheader('st.multiselect')

options = st.multiselect('What kind of movies do you like?',
               ['Horror', 'Comedy', 'Action', 'Drama', 'Sci-Fi'])

st.write('You selected ', options)

# slider
st. markdown('---')
st.subheader('st.slider')
loan = st.slider('What is loan amount you are applying for?', 0, 100000, 1000, 1000) # prompt, minimum, maximum, default, step
st.write('Loan amount = ', loan)

# text input
st. markdown('---')
st.subheader('st.text_input, st.number_input, st.date_input')

with st.container():
    name = st.text_input('Enter your name')
    age = st.number_input('Enter your age', min_value=0, max_value=150, value=25, step=1)
    describe = st.text_area('Describe yourself', height=150)
    dob = st.date_input('Select your birthday')

    submit_button = st.button('Submit button')
    if submit_button:
        person_dict = {
            "name": name,
            "age": age,
            "dob": dob,
            "about": describe
        }
        st.json(person_dict)

# file uploader
st. markdown('---')
st.subheader('st.file_uploader')

uploaded_file = st.file_uploader('Choose a file')
save_button = st.button('Save file')
if save_button:
    if uploaded_file is not None:
        with open(os.path.join('./save_folder', uploaded_file.name), mode='wb') as f:
            f.write(uploaded_file.getbuffer())

        st.success('File uploaded successfully')
    else:
        st.warning('No file selected')
