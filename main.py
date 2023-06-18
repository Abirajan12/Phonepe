import streamlit as st
from mysql_data_retrieval import *

def main():
    st.title("PhonePe pulse")
    st.sidebar.selectbox("All India",('Transaction', 'User'))
    st.sidebar.selectbox('Year',get_years())
    col1, col2 = st.columns(2)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

if __name__ == "__main__":
    main()