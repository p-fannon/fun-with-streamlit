import streamlit as st

st.title('Title')
st.caption('Using st.title() you can display the text in title format')

st.header('Header')
st.caption("The text inside header st.header() is in header format")

st.subheader('Subheader')
st.caption("My Subheader for my awesome app")

st.markdown('---')
st.subheader('Generate random program:')

body = """
    print('Hello world!')
    
    import numpy as np
    
    def generate_random(size):
        rand = np.random.random(size=size)
        return rand
    
    number = generate_random(10)
    """

st.code(body, language='python')

st.subheader('Latex')
formula = """
    a + ar + ar^2 + ar^3 + \cdots + ar^{n-1} = \sum_{k=0}^{n-1} ar^k
    """
st.latex(formula)