import streamlit as st
from mysql_data_retrieval import *

def main():
    st.set_page_config(page_title="Abi's,PhonePe Pulse 2.0", page_icon=':telephone_receiver:',layout = 'wide')

    with st.container():
        st.title("PhonePe pulse 2.0")
        st.write("An user friendly dashboard mimicking the Phonepe Pulse")

    tab1, tab2  = st.tabs(['Transaction', 'User'])
    with tab1:    
        trn_year = st.multiselect('Year',get_years())
        if trn_year:
            trn_year = '('+', '.join(str(value) for value in trn_year)+')'

        trn_quarter = st.multiselect('Quarter',(['Q1','Q2','Q3','Q4']))
        if trn_quarter:
            trn_quarter = [ int(i.replace("Q","")) for i in trn_quarter]
            trn_quarter = '('+', '.join(str(value) for value in trn_quarter)+')'

        transaction_Query_List = ['Drag to choose query','Details of top 10 districts based on total count of transactions',
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
        trn_query = st.selectbox('Select the Query',transaction_Query_List)
        if trn_year and trn_quarter:
            trn_query_df = get_Transaction_Query_Result(trn_query,trn_year,trn_quarter)
            if trn_query_df is not None:
                st.dataframe(trn_query_df)
        else:
            st.write("Please choose year/quarter")
    with tab2:
        year = st.multiselect('Year ',get_years())
        if year:
            year = '('+', '.join(str(value) for value in year)+')'

        quarter = st.multiselect('Quarter ',(['Q1','Q2','Q3','Q4']))
        if quarter:
            quarter = [ int(i.replace("Q","")) for i in quarter]
            quarter = '('+', '.join(str(value) for value in quarter)+')'

        user_Query_List = ['Drag to choose query','Total count of users with repect to user device',
                      'States and their percentage of phonepe users',
                      'State with more users with Apple',
                      'Bottom 10 States with Xiaomi users',
                      'Users count in year/quarter',
                      'High number of registered users among states',
                      'Count of app opens in a particular district',
                      'No of Registered users, app opens in a particular quarter and particular year',
                      'Districts with less number of Registed Users',
                      'Top 10 states which has less number customers',
                      'Pincodes with maximum registered users']
        query = st.selectbox('Select the Query ',user_Query_List)
        if year and quarter:
            query_df = get_User_Query_Result(query,year,quarter)
            if query_df is not None:
                st.dataframe(query_df)
        else:
            st.write("Please choose year/quarter")    

if __name__ == "__main__":
    main()