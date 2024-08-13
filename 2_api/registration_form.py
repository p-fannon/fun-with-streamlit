import streamlit as st
import datetime

with st.form('myform'):
    st.subheader('Registration form')
    col1, col2, col3 = st.columns(3)

    with col1:
        select_title = st.selectbox('Title',
                                    ('Mr.', 'Mrs.', 'Ms.'))
    with col2:
        first_name = st.text_input('First Name')
    with col3:
        last_name = st.text_input('Last Name')

    select_occupation = st.selectbox('Occupation',
                                     ('Engineer', 'Project Manager', 'QA', 'Baker', 'Firefighter', 'Guardian of the Galaxy'))
    dob = st.date_input('Select your date of birth', min_value=datetime.datetime(1900, 1, 1))
    select_gender = st.radio('Select gender',
                             ('Male', 'Female', 'Prefer not to say'))
    age = st.slider('Age', 1, 100, 18)

    submit_button = st.form_submit_button('Submit')

    if submit_button:
        st.balloons()
        person_dict = {
            "name": f'{select_title} {first_name} {last_name}',
            "age": age,
            "gender": select_gender,
            "Date of birth": dob,
            "occupation": select_occupation
        }
        st.json(person_dict)