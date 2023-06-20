import streamlit as st
from mysql_data_retrieval import *

def main():
    st.set_page_config(page_title="Abi's,PhonePe Pulse 2.0", page_icon=':telephone_receiver:',layout = 'wide')
    with st.container():
        st.title("PhonePe pulse 2.0")
        st.write("An user friendly dashboard mimicking the Phonepe Pulse")
    type = st.sidebar.radio("All India",('Transaction', 'User'))
    year = int(st.sidebar.selectbox('Year',get_years()))
    quarter = int((st.sidebar.radio('Quarter',('Q1','Q2','Q3','Q4')))[-1])
    print(year)
    print(quarter)
    
    col1, col2 = st.columns(2)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

if __name__ == "__main__":
    main()