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
            query = f"SELECT * FROM map_transaction WHERE year IN {year} AND quarter in {quarter} ORDER BY total_count DESC LIMIT 10"
            cursor.execute(query)
            df = pd.DataFrame(cursor.fetchall())
        return df