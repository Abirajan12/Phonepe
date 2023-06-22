import pandas as pd
from mysql_data_insertion import create_connection

def get_years():
    with create_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT(year) FROM aggregated_transaction")
        year_list = [year[0] for year in cursor.fetchall()]
    return year_list

def get_Query_Result(query, year, quarter):
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