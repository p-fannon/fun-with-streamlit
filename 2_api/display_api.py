import streamlit as st
import pandas as pd
import numpy as np

st.write('Hello world')

st.write('Welcome to Streamlit App APIs')

st.write(1234)

df = pd.DataFrame({
    'first_column': [1,2,3,4],
    'second_column': [10, 20, 30, 40]
})

st.write(df)

# display numpy array
st.write(np.array([2,4,6,8]))

st.write("Magic commands")

df1 = pd.DataFrame({
    'column_1': [1,2,3,4]
})

df1
x = 10
x
x = 20
x