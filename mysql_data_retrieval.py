import pandas as pd
from mysql_data_insertion import create_connection

def get_years():
    with create_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT(year) FROM aggregated_transaction")
        year_list = [year[0] for year in cursor.fetchall()]
    return year_list

def get_Transaction_Query_Result(query, year, quarter):
    if query == 'Drag to choose query':
        return None

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
        return df
    
    elif query == 'Total count of transactions in each payment category':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT payment_category, sum(total_count) \
                    FROM aggregated_transaction WHERE year IN {year}  \
                    AND quarter IN {quarter} \
                    GROUP BY payment_category;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Total amount of transactions in each payment category':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT payment_category, max(total_amount) \
                    FROM aggregated_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY payment_category;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Payment category which has maximum transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT payment_category, sum(total_count) \
                    FROM aggregated_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY payment_category \
                    ORDER BY sum(total_count) DESC \
                    LIMIT 1;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Payment Category which has high amount involved in transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT payment_category, sum(total_amount) \
                    FROM aggregated_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY payment_category \
                    ORDER BY sum(total_amount) DESC \
                    LIMIT 1;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Top 5 districts which has maximum number of transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, district,sum(total_count) \
                    FROM map_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state, district \
                    ORDER BY sum(total_count) DESC \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'District with least number of transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state,district,sum(total_count) \
                    FROM map_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state,district \
                    ORDER BY sum(total_count) \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'States which has huge amount involved in transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, sum(total_amount) \
                    FROM map_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state \
                    ORDER BY sum(total_amount) DESC \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'States to concentrate to increase transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, sum(total_count) \
                    FROM map_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state \
                    ORDER BY sum(total_count) \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Top 5 pincodes which has maximum number of transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state, pincode,sum(total_count) \
                    FROM top_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state, pincode \
                    ORDER BY sum(total_count) DESC \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
    elif query == 'Pincodes to concentrate to increase transactions':
        with create_connection() as connection:
            cursor = connection.cursor()
            query = f'SELECT state,pincode,sum(total_count) \
                    FROM top_transaction \
                    WHERE year IN {year}  AND quarter IN {quarter} \
                    GROUP BY state,pincode \
                    ORDER BY sum(total_count) \
                    LIMIT 5;'
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=column_names)
        return df
    
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