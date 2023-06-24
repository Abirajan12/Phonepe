import pandas as pd
from mysql_data_insertion import create_connection
import plotly.graph_objects as go

def get_years():
    with create_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT(year) FROM aggregated_transaction")
        year_list = [year[0] for year in cursor.fetchall()]
    return year_list

def get_Transaction_Query_Result(query, year, quarter):
    if query == 'Drag to choose query':
        return None, None

    elif query == 'Details of top 10 districts based on total count of transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f"SELECT * \
                    FROM map_transaction \
                    WHERE year IN {year} AND quarter in {quarter} \
                    ORDER BY total_count DESC LIMIT 10"
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            # Define custom colors for the bars
            colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#C0C0C0', '#808080', '#800000', '#008000']
            fig = go.Figure(data=go.Bar(x=df['district'], y=df['total_count'],marker=dict(color=colors)))
            fig.update_layout(title='District-wise Total Count', xaxis_title='District', yaxis_title='Total Count')  
        return df,fig
    
    elif query == 'Total count of transactions in each payment category':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT payment_category, sum(total_count) AS sum_of_total_count\
                    FROM aggregated_transaction WHERE year IN {year}  \
                    AND quarter IN {quarter} \
                    GROUP BY payment_category;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            colors = ['#DFFF00','#F08080','#DE3163','#40E0D0','#CCCCFF']
            fig = go.Figure(data=go.Bar(x=df['payment_category'], y=df['sum_of_total_count'],marker=dict(color=colors)))
            fig.update_layout(title='Payment Category Total Count', xaxis_title='Payment Category', yaxis_title='Sum of Total Count')
        return df,fig
    
    elif query == 'Sum of total amount involved in each payment category':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT payment_category, sum(total_amount) as sum_of_total_amount \
                    FROM aggregated_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY payment_category;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            colors = ['#0000FF','#FF00FF','#00FFFF','#FF0000','#FFFF00']
            fig = go.Figure(data=go.Pie(labels=df['payment_category'], values=df['sum_of_total_amount'],marker=dict(colors=colors)))
        return df,fig
    
    elif query == 'Payment category which has maximum transactions in each state':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state,payment_category, sum(total_count) as sum_of_total_count \
                    FROM aggregated_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY payment_category, state \
                    ORDER BY sum(total_count) DESC \
                    LIMIT 20;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            fig = go.Figure(data=go.Pie(labels=df['state'], values=df['sum_of_total_count']))
        return df,fig
    
    elif query == 'Payment Category which has high amount involved in transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT year, payment_category, sum(total_amount) \
                    FROM aggregated_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY year, payment_category \
                    ORDER BY year, sum(total_amount) DESC;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            fig = go.Figure()
            for y in df['year'].unique():
                df_year = df[df['year'] == y]
                fig.add_trace(go.Bar(x=df_year['payment_category'], y=df_year['sum(total_amount)'],name=str(y)))        
            fig.update_layout(barmode='group', title='Payment Category with High Amount Involved in Transactions')
        return df,fig
    
    elif query == 'Top 5 districts which has maximum number of transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, district,sum(total_count) as sum_of_total_count\
                    FROM map_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state, district \
                    ORDER BY sum(total_count) DESC \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            colors = ['#DFFF00','#F08080','#DE3163','#40E0D0','#CCCCFF']
            fig = go.Figure(data=go.Bar(x=df['district'], y=df['sum_of_total_count'],marker=dict(color=colors)))
            fig.update_layout(title='District Total Count', xaxis_title='District', yaxis_title='Sum of Total Count')
        return df,fig
    
    elif query == 'District with least number of transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state,district,sum(total_count) as sum_of_total_count \
                    FROM map_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state,district \
                    ORDER BY sum(total_count) \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            colors = ['#FF1493','#FFA500','#9400D3','#32CD32','#0000FF']
            fig = go.Figure(data=go.Bar(x=df['district'], y=df['sum_of_total_count'],marker=dict(color=colors)))
            fig.update_layout(title='Districts to Concentrate', xaxis_title='District', yaxis_title='Sum of Total Count')
        return df,fig
    
    elif query == 'States which has huge amount involved in transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, sum(total_amount) as sum_of_total_amount \
                    FROM map_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state \
                    ORDER BY sum(total_amount) DESC \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            colors = ['#7B68EE','#DAA520','#87CEFA','#663399','#008080']
            fig = go.Figure(data=go.Pie(labels=df['state'], values=df['sum_of_total_amount'],marker=dict(colors=colors)))
        return df,fig
    
    elif query == 'States to concentrate to increase transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, sum(total_count) as sum_of_total_count \
                    FROM map_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state \
                    ORDER BY sum(total_count) \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            colors = ['#8B0000','#9400D3','#FF4500','#FFC0CB','#BDB76B']
            fig = go.Figure(data=go.Pie(labels=df['state'], values=df['sum_of_total_count'],marker=dict(colors=colors)))
        return df,fig
    
    elif query == 'Top 5 pincodes which has maximum number of transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, pincode,sum(total_count) as sum_of_total_count\
                    FROM top_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state, pincode \
                    ORDER BY sum(total_count) DESC \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            colors = ['#FF1493','#FFA500','#9400D3','#32CD32','#0000FF']
            x_labels = [f"{state} - {pincode}" for state, pincode in zip(df['state'], df['pincode'])]
            fig = go.Figure(data=go.Bar(x=x_labels, y=df['sum_of_total_count'],marker=dict(color=colors)))
            fig.update_layout(title='Top 5 Pincodes with Maximum Number of Transactions',
                              xaxis_title='State - Pincode', yaxis_title='Total Count')
        return df,fig
    
    elif query == 'Pincodes to concentrate to increase transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state,pincode,sum(total_count) as sum_of_total_count \
                    FROM top_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state,pincode \
                    ORDER BY sum(total_count) \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            colors = ['#D8BFD8','#FFA500','#FFDAB9','#32CD32','#0000FF']
            x_labels = [f"{state} - {pincode}" for state, pincode in zip(df['state'], df['pincode'])]
            fig = go.Figure(data=go.Pie(labels=x_labels, values=df['sum_of_total_count'],marker=dict(colors=colors)))
        return df,fig
    
def get_User_Query_Result(query, year, quarter):
    if query == 'Drag to choose query':
        return None

    elif query == 'Total count of users with repect to user device':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f"SELECT user_device, sum(total_count) \
                    FROM aggregated_user \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY user_device \
                    ORDER BY sum(total_count) DESC;"
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'States and their percentage of phonepe users':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, sum(percentage) \
                    FROM aggregated_user \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state \
                    ORDER BY sum(percentage) DESC;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'State with more users with Apple':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, sum(total_count) \
                    FROM aggregated_user \
                    WHERE year IN {year}  AND quarter IN {quarter} AND user_device = "Apple" \
                    GROUP BY state \
                    ORDER BY sum(total_count) DESC;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Bottom 10 States with Xiaomi users':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, sum(total_count) \
                    FROM aggregated_user \
                    WHERE year IN {year}  AND quarter IN {quarter} AND user_device = "Xiaomi" \
                    GROUP BY state \
                    ORDER BY sum(total_count) \
                    LIMIT 10;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Users count in year/quarter':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT year, quarter,sum(total_count) \
                    FROM aggregated_user \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY year, quarter \
                    ORDER BY sum(total_count);'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'High number of registered users among states':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, sum(registered_users) \
                    FROM map_user \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state \
                    ORDER BY sum(registered_users) DESC;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Count of app opens in a particular district':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state,district, sum(app_opens) \
                    FROM map_user \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state,district \
                    ORDER BY sum(app_opens) DESC;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'No of Registered users, app opens in a particular quarter and particular year':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT year, quarter,sum(registered_users),sum(app_opens) \
                    FROM map_user \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY year, quarter \
                    ORDER BY sum(app_opens) DESC;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Districts with less number of Registed Users':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state,district, sum(registered_users) \
                    FROM map_user \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state,district \
                    ORDER BY sum(registered_users) \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Top 10 states which has less number customers':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, sum(registered_users) \
                    FROM top_user \
                    WHERE year IN {year} AND quarter IN {quarter} \
                    GROUP BY state \
                    ORDER BY sum(registered_users) \
                    LIMIT 10;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Pincodes with maximum registered users':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, pincode,sum(registered_users) \
                    FROM top_user \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state,pincode \
                    ORDER BY sum(registered_users) DESC \
                    LIMIT 10;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df

def get_changed_state_names():
    with create_connection() as connection:
        cursor = connection.cursor()
        query = f"SELECT distinct state from aggregated_transaction"
        cursor.execute(query)
        rows = cursor.fetchall()
        table_state_names = [row[0] for row in rows]
        return table_state_names

def get_Geo_Query_Result(query,year, quarter,state_names):
    if query == 'State':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f"SELECT state, sum(total_count) as sum_of_total_count\
                    FROM aggregated_transaction \
                    WHERE year in {year} AND quarter IN {quarter}\
                    GROUP BY state"
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
            table_state_names = get_changed_state_names()

            for i in range(len(table_state_names)):
                df['state'] = df['state'].replace({table_state_names[i]: state_names[i]})
        return df
