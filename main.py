import streamlit as st
from mysql_data_retrieval import *

def main():
    st.set_page_config(page_title="Abi's,PhonePe Pulse 2.0", page_icon=':telephone_receiver:',layout = 'wide')

    with st.container():
        st.title("PhonePe pulse 2.0")
        st.write("An user friendly dashboard mimicking the Phonepe Pulse")


    tab1, tab2  = st.tabs(['Transaction', 'User'])
    print(tab1)

    with tab1:    
        year = st.multiselect('Year',get_years())
        year = tuple(year)
        print(year)
        #quarter = (st.radio('Quarter',(['Q1','Q2','Q3','Q4']),horizontal = True))[-1]
        quarter = st.multiselect('Quarter',(['Q1','Q2','Q3','Q4']))
        quarter = tuple([ int(i.replace("Q","")) for i in quarter])
        print(quarter)
        query_List = ['Drag to choose query','Details of top 10 districts based on total count of tansactions happened in a particular year in a particular Quarter']
        query = st.selectbox('select the Query',query_List)
        #query_df = get_Query_Result(query,year,quarter)
        
        #if query_df is not None:
        #   st.dataframe(query_df)

    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

if __name__ == "__main__":
    main()