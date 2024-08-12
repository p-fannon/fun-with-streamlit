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
