import streamlit as st
import pandas as pd
import numpy as np

#plotly
import plotly.express as px

data = pd.read_csv('tips.csv')

# Reference URL: https://plotly.com/python/plotly-express/
# 1. Draw histogram for total bill

st.subheader('Draw histogram for total bill')

fig = px.histogram(data_frame=data, x='total_bill')
st.plotly_chart(fig)

# 2. Draw histogram for total bill and color by sex

st.markdown('---')
st.subheader('Draw histogram for total bill and color by sex')
fig = px.histogram(data_frame=data, x='total_bill', color='sex')
st.plotly_chart(fig)

# 3. Draw histogram for total bill and color by (sex, smoker, day, time)
# 4. Draw Scatter plot between total_bill and tips and color by 
