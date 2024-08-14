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

st.markdown('---')
st.subheader('Draw histogram for total bill and color by (sex, smoker, day, time)')
select = st.selectbox('Select the category to color', ('sex', 'smoker', 'day', 'time'))
fig = px.histogram(data_frame=data, x='total_bill', color=select)
st.plotly_chart(fig)

# 4. Draw Scatter plot between total_bill and tips and color by 

st.markdown('---')
st.subheader("Draw Scatter plot between total_bill and tips and color by ('sex', 'smoker', 'day', 'time')")
color_option = st.selectbox('Select a category to color', ('sex', 'smoker', 'day', 'time'))
fig = px.scatter(data_frame=data, x='total_bill', y='tip', color=color_option)
st.plotly_chart(fig)

# 5. Sunburst Chart on features ('sex','day','smoker','time')
st.markdown('---')
st.subheader("Sunburst Chart on features ('sex','day'pip,'smoker','time')")
path = st.multiselect('Select the categorical features path', ('sex','day','smoker','time'))
fig = px.sunburst(data_frame=data, path=path)
st.plotly_chart(fig)
