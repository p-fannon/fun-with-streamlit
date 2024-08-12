import streamlit as st
import pandas as pd
import time

side_bar = st.sidebar

side_bar.header('The sidebar')
side_bar.caption('elements added to sidebar are pinned to the left')

# Load tips.csv
df = pd.read_csv('tips.csv')

columns = tuple(df.columns)
st.write(columns)

# create widget selectbox
select_column = side_bar.selectbox(
    "Select the column you want to display", columns
)

side_bar.write(f'You selected the column name = {select_column}')

# Display the data frame
st.dataframe(df[[select_column]])

# Layout columns
st.header('Columns: st.columns')
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('Column 1')
    st.image('./media/image.jpg')

with col2:
    st.subheader('Column 2')
    st.dataframe(df)

with col3:
    st.subheader('Column 3')
    st.dataframe(df[[select_column]])

# expander
st.subheader('Expander: st.expander')
with st.expander('My expander'):
    st.write("""
    I'm a little teapot, short and stout
    """)
    st.code('print("Here is my handle, here is my sprout")', language='python')

# container
st.subheader('Container st.container')
with st.container():
    st.write('when I get all steamed up, hear me shout')

# Empty
st.subheader('Empty: st.empty')
placeholder = st.empty()

for i in range(10, 0, -1):
    placeholder.write(f'TIP ME OVER AND POUR ME OUT IN THE NEXT {i} SECONDS')
    time.sleep(1)

placeholder.empty()
