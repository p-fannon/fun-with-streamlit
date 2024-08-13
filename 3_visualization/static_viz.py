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

# 3. Find distribution of average total_bill across each day by male and female
# bar, area, line
st.markdown('---')
st.write('Find distribution of average total_bill across each day by male and female')

features_to_groupby = ['day', 'sex']
feature = ['total_bill']
select_cols = feature + features_to_groupby
avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()
avg_total_bill = avg_total_bill.unstack()

# Visualization
fig, ax = plt.subplots()
avg_total_bill.plot(kind='bar', ax=ax)
ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5))
st.pyplot(fig)

st.dataframe(avg_total_bill)
