import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')

# st.dataframe for displaying dataframes

st.header('st.dataframe')
st.caption('Display a dataframe as an interactive table')

st.dataframe(data=df, height=500, width=750)

# st.static
st.header('st.table')
st.caption('Display a static table')

st.table(data=df.head(5))

# st.json
st.header('st.json')
st.caption('Display object or string as a pretty-printed JSON string')

json_values = df.head(3).to_dict()
st.json(json_values)