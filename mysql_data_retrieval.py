from mysql_data_insertion import create_connection

def get_years():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT(year) FROM aggregated_transaction")
    year_list = [year[0] for year in cursor.fetchall()]
    connection.close()
    return year_list



