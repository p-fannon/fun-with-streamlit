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
