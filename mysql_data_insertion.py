import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Phonepe',
            user='root',
            password='Guviabi12*'
        )
        print('Connected to MySQL database')
    except Error as e:
        print(f'Error connecting to MySQL database: {e}')
    return connection

def get_modified_column_datatypes(df, column_names):
    column_info = ', '.join([f'{column} TINYINT' if dtype == 'int8' 
                             else f'{column} SMALLINT' if dtype == 'int16' 
                             else f'{column} BIGINT' if dtype == 'int64' 
                             else f'{column} TEXT' if dtype == 'object' 
                             else f'{column} INT' if dtype == 'int'
                             else f'{column} DOUBLE' if dtype == 'float64'
                             else f'{column} {dtype}' for column, dtype in df.dtypes.items()])
    return column_info


def insert_dataframe_into_mysql(df, table_name, connection):
    # Convert the DataFrame to a list of tuples
    data = df.values.tolist()

    column_names = list(df.columns)
    column_info = get_modified_column_datatypes(df, column_names)
    # Create the table if it does not exist
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_info});"

    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully or already exists.")
    except Error as e:
        print(f"Error creating table: {e}")

    # Prepare the INSERT statement
    insert_statement = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['%s'] * len(column_names))})"

    # Check if the table already has values
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    result = cursor.fetchone()
    has_values = result[0] > 0
    
    # Insert the data into the MySQL table
    if has_values:
        print(f"The table '{table_name}' already has values. Skipping data insertion.")
    else:
        try:
            cursor = connection.cursor()
            cursor.executemany(insert_statement, data)
            connection.commit()
            print(f"Data inserted into MySQL table: {table_name}")
        except Error as e:
            connection.rollback()
            print(f"Error inserting data into MySQL table: {e}")

def insert_dataframes(dataframes):
    connection = create_connection()
    try:
        for table_name, df in dataframes.items():
            insert_dataframe_into_mysql(df, table_name, connection)
    except Error as e:
        print(f'Error inserting dataframes: {e}')
    finally:
        if connection:
            connection.close()
