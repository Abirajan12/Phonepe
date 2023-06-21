import pandas as pd
from mysql_data_insertion import create_connection

def get_years():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT(year) FROM aggregated_transaction")
    year_list = [year[0] for year in cursor.fetchall()]
    connection.close()
    return year_list

def get_Query_Result(query,year,quarter):
    connection = create_connection()
    cursor = connection.cursor()
    if query == 'Drag to choose query':
        None 
    elif query == 'Details of top 10 districts based on total count of tansactions happened in a particular year in a particular Quarter': 
        cursor.execute("SELECT * FROM map_transaction WHERE year = %s AND quarter = %s ORDER BY total_count DESC LIMIT 10", (year[0], quarter[0]))
        df = pd.DataFrame(cursor.fetchall())
        connection.close()
        return df