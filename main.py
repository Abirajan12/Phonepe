import streamlit as st
from mysql_data_retrieval import *

def main():
    st.set_page_config(page_title="Abi's,PhonePe Pulse 2.0", page_icon=':telephone_receiver:',layout = 'wide')

    with st.container():
        st.title("PhonePe pulse 2.0")
        st.write("An user friendly dashboard mimicking the Phonepe Pulse")

    tab1, tab2  = st.tabs(['Transaction', 'User'])
    with tab1:    
        year = st.multiselect('Year',get_years())
        if year:
            year = '('+', '.join(str(value) for value in year)+')'

        quarter = st.multiselect('Quarter',(['Q1','Q2','Q3','Q4']))
        if quarter:
            quarter = [ int(i.replace("Q","")) for i in quarter]
            quarter = '('+', '.join(str(value) for value in quarter)+')'

        query_List = ['Drag to choose query','Details of top 10 districts based on total count of transactions',
                      'Total count of transactions in each payment category',
                      'Total amount of transactions in each payment category',
                      'Payment category which has maximum transactions',
                      'Payment Category which has high amount involved in transactions',
                      'Top 5 districts which has maximum number of transactions',
                      'District with least number of transactions',
                      'States which has huge amount involved in transactions',
                      'States to concentrate to increase transactions',
                      'Top 5 pincodes which has maximum number of transactions',
                      'Pincodes to concentrate to increase transactions']
        query = st.selectbox('select the Query',query_List)
        if year and quarter:
            query_df = get_Query_Result(query,year,quarter)
            if query_df is not None:
                st.dataframe(query_df)
        else:
            st.write("Please choose year/quarter")
    with tab2:
        pass      

if __name__ == "__main__":
    main()