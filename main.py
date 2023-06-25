import streamlit as st
from mysql_data_retrieval import *
from geotrail import *

def main():
    st.set_page_config(page_title="Abi's,PhonePe Pulse 2.0", page_icon=':telephone_receiver:',layout = 'wide')
    st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)
    
    with st.container():
        st.title("PhonePe pulse 2.0")
        st.write("An user friendly dashboard mimicking the Phonepe Pulse")

    tab1, tab2, tab3  = st.tabs(['Transaction', 'User', 'Geo'])
    with tab1:
        c1,c2 = st.columns(2)    
        with c1:
            trn_year = st.multiselect('Year',get_years())
            if trn_year:
                trn_year = '('+', '.join(str(value) for value in trn_year)+')'
        with c2:
            trn_quarter = st.multiselect('Quarter',(['Q1','Q2','Q3','Q4']))
            if trn_quarter:
                trn_quarter = [ int(i.replace("Q","")) for i in trn_quarter]
                trn_quarter = '('+', '.join(str(value) for value in trn_quarter)+')'

        transaction_Query_List = ['Drag to choose query','Details of top 10 districts based on total count of transactions',
                      'Total count of transactions in each payment category',
                      'Sum of total amount involved in each payment category',
                      'Payment category which has maximum transactions in each state',
                      'Payment Category which has high amount involved in transactions',
                      'Top 5 districts which has maximum number of transactions',
                      'District with least number of transactions',
                      'States which has huge amount involved in transactions',
                      'States to concentrate to increase transactions',
                      'Top 5 pincodes which has maximum number of transactions',
                      'Pincodes to concentrate to increase transactions']
        trn_query = st.selectbox('Select the Query',transaction_Query_List)
        if trn_year and trn_quarter:
            trn_query_df, trn_query_fig = get_Transaction_Query_Result(trn_query,trn_year,trn_quarter)
            if trn_query_df is not None and trn_query_fig is not None:
                col1, col2 = st.columns(2)
                with col1:
                    st.dataframe(trn_query_df)
                with col2:
                    st.plotly_chart(trn_query_fig)
        else:
            st.markdown(""":red[Please choose year/quarter]""")
    with tab2:
        c1,c2 = st.columns(2)
        with c1:
            usr_year = st.multiselect('Year ',get_years())
            if usr_year:
                usr_year = '('+', '.join(str(value) for value in usr_year)+')'
        with c2:
            usr_quarter = st.multiselect('Quarter ',(['Q1','Q2','Q3','Q4']))
            if usr_quarter:
                usr_quarter = [ int(i.replace("Q","")) for i in usr_quarter]
                usr_quarter = '('+', '.join(str(value) for value in usr_quarter)+')'

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
        usr_query = st.selectbox('Select the Query ',user_Query_List)
        if usr_year and usr_quarter:
            usr_query_df = get_User_Query_Result(usr_query,usr_year,usr_quarter)
            if usr_query_df is not None:
                st.dataframe(usr_query_df)
        else:
            st.markdown(""":red[Please choose year/quarter]""")    

    with tab3:
        st.write("Geo visualization of Phone pe Pulse data across years and quarters")
        c1, c2 = st.columns(2)
        with c1:
            year = st.multiselect(' Year ',get_years())
            if year:
                year = '('+', '.join(str(value) for value in year)+')'
        with c2:    
            quarter = st.multiselect(' Quarter ',(['Q1','Q2','Q3','Q4']))
            if quarter:
                quarter = [ int(i.replace("Q","")) for i in quarter]
                quarter = '('+', '.join(str(value) for value in quarter)+')'

        query_List = ['Drag to choose query','State and Total count of Phonepe Transactions',
                      'States - Total Amount of Phone Pe Transactions',
                      'States - Total count of Users',
                      'States - Percentage of Users',
                      'States - Registered Users',
                      'States - App Opens']
        query = st.selectbox('Select the Query ',query_List)
        if year and quarter:
            df,fig = get_Geo_Json_Result(query,year,quarter)
            if df is not None and fig is not None:
                col1,col2 = st.columns(2)
                with col1:
                    st.dataframe(df)
                with col2:
                    st.plotly_chart(fig)
        else:
            st.markdown(""":red[Please choose year/quarter]""")    

if __name__ == "__main__":
    main()