import streamlit as st
import pandas as pd
import numpy as np
# static
import matplotlib.pyplot as plt
import seaborn as sns

st.header('matplotlib and seaborn visualization in streamlit')

# load the data
df = pd.read_csv('tips.csv')
st.dataframe(df.head())

# questions
# 1. Find number of male and female distribution (pie and bar)
# 2. Find distribution of male and female spent (boxplot or kdeplot)
# 3. Find distribution of average total_bill across each day by male and female
# 4. Find the relation between total_bill and tip on time (scatter plot)

st.markdown('---')
with st.container():
    st.write('1. Find number of male and female distribution (pie and bar)')

    value_counts = df['sex'].value_counts()
    col1, col2 = st.columns(2)

    with col1:
        # draw pie chart
        st.subheader('Pie chart')
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct="%0.2f%%", labels=["Male", "Female"])
        st.pyplot(fig)

    with col2:
        # draw bar plot
        st.subheader('Bar chart')
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts)
        st.pyplot(fig)

    with st.expander('Click here to display value counts'):
        st.dataframe(value_counts)

# streamlit widgets and charts

data_types = df.dtypes
cat_cols = tuple(data_types[data_types == 'object'].index)
st.markdown('---')
with st.container():
    feature = st.selectbox('Select the feature',
                           cat_cols)

    value_counts = df[feature].value_counts()
    col1, col2 = st.columns(2)

    with col1:
        # draw pie chart
        st.subheader('Pie chart')
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct="%0.2f%%", labels=value_counts.index)
        st.pyplot(fig)

    with col2:
        # draw bar plot
        st.subheader('Bar chart')
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts)
        st.pyplot(fig)

    with st.expander('Click here to display value counts'):
        st.dataframe(value_counts)

# 2. Find distribution of male and female spent (boxplot or kdeplot)
st.markdown('---')
with st.container():
    st.write('Find distribution of male and female spent')
    # box, violin, kdeplot, histogram
    chart = ("box", "violin", "kdeplot", "histogram")
    chart_selection = st.selectbox('Select the chart type', chart)
    fig, ax = plt.subplots()
    if chart_selection == 'box':
        sns.boxplot(x = 'sex', y='total_bill', data=df, ax=ax)
    elif chart_selection == 'violin':
        sns.violinplot(x = 'sex', y='total_bill', data=df, ax=ax)
    elif chart_selection == 'kdeplot':
        sns.kdeplot(x=df['total_bill'], hue=df['sex'], ax=ax, shade=True)
    else:
        sns.histplot(x='total_bill', hue='sex', data=df, ax=ax)

    st.pyplot(fig)
