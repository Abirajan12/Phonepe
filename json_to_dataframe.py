import os
import pandas as pd
import json

def aggregated_transaction_df():
    aggregated_transaction_directory = r'C:\Phonepe\pulse\data\aggregated\transaction\country\india\state'
   
    data = []
    for state_folder in os.listdir(aggregated_transaction_directory):
        state_path = os.path.join(aggregated_transaction_directory,state_folder)
        if os.path.isdir(state_path):

            for year_folder in os.listdir(state_path):
                year_path = os.path.join(state_path,year_folder)
                if os.path.isdir(year_path):

                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path,quarter_file)
                        
                        with open(quarter_path, 'r') as aggregated_transaction_json_file:
                            json_data = json.load(aggregated_transaction_json_file)

                            for transaction in json_data['data']['transactionData']:
                                payment_category = transaction['name']

                                for payment_instrument in transaction['paymentInstruments']:
                                    total_count = payment_instrument['count']
                                    total_amount = payment_instrument['amount']

                                    record = {
                                        'state'  : state_folder,
                                        'year'   : year_folder,
                                        'quarter': quarter_file[0],
                                        'payment_category': payment_category,
                                        'total_count': total_count,
                                        'total_amount': total_amount

                                    }
                                    data.append(record)

    df = pd.DataFrame(data)
    print(df.head())


def map_transaction_df():
    map_transaction_directory = r'C:\Phonepe\pulse\data\map\transaction\hover\country\india\state'
   
    data = []
    for state_folder in os.listdir(map_transaction_directory):
        state_path = os.path.join(map_transaction_directory,state_folder)
        if os.path.isdir(state_path):

            for year_folder in os.listdir(state_path):
                year_path = os.path.join(state_path,year_folder)
                if os.path.isdir(year_path):

                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path,quarter_file)
                        
                        with open(quarter_path, 'r') as map_transaction_json_file:
                            json_data = json.load(map_transaction_json_file)

                            for district in json_data['data']['hoverDataList']:
                                district_name = district['name']

                                for metric in district['metric']:
                                    total_count = metric['count']
                                    total_amount = metric['amount']

                                    record = {
                                        'state'  : state_folder,
                                        'year'   : year_folder,
                                        'quarter': quarter_file[0],
                                        'district': district_name[:-9],
                                        'total_count': total_count,
                                        'total_amount': total_amount

                                    }
                                    data.append(record)

    df = pd.DataFrame(data)
    #print(df[(df['state'] == 'tamil-nadu') & (df['year'] == '2018') & (df['quarter'] == '3')])
    print(df.head())

def top_transaction_df():
    top_transaction_directory = r'C:\Phonepe\pulse\data\top\transaction\country\india\state'
   
    data = []
    for state_folder in os.listdir(top_transaction_directory):
        state_path = os.path.join(top_transaction_directory,state_folder)
        if os.path.isdir(state_path):

            for year_folder in os.listdir(state_path):
                year_path = os.path.join(state_path,year_folder)
                if os.path.isdir(year_path):

                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path,quarter_file)
                        
                        with open(quarter_path, 'r') as top_transaction_json_file:
                            json_data = json.load(top_transaction_json_file)

                            for pincode in json_data['data']['pincodes']:
                                pincode_num = pincode['entityName']
                                metric = pincode['metric']
                                total_count = metric['count']
                                total_amount = metric['amount']
                                #print (district_name, total_count,total_amount)

                                record = {
                                        'state'  : state_folder,
                                        'year'   : year_folder,
                                        'quarter': quarter_file[0],
                                        'pincode': pincode_num,
                                        'total_count': total_count,
                                        'total_amount': total_amount

                                    }
                                data.append(record)

    df = pd.DataFrame(data)
    #print(df[(df['state'] == 'tamil-nadu') & (df['year'] == '2018') & (df['quarter'] == '3')])
    print(df.head())
    #df['total_count'] = pd.to_numeric(df['total_count'], errors='coerce')  # Convert 'total_count' to numeric type
    #df['total_count'] = df['total_count'].fillna(0) 
    #print(df.nlargest(10, 'total_count'))

def aggregated_user_df():
    aggregated_user_directory = r'C:\Phonepe\pulse\data\aggregated\user\country\india\state'
   
    data = []
    for state_folder in os.listdir(aggregated_user_directory):
        state_path = os.path.join(aggregated_user_directory,state_folder)
        if os.path.isdir(state_path):

            for year_folder in os.listdir(state_path):
                year_path = os.path.join(state_path,year_folder)
                if os.path.isdir(year_path):

                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path,quarter_file)
                        
                        with open(quarter_path, 'r') as aggregated_user_json_file:
                            json_data = json.load(aggregated_user_json_file)

                            if json_data['data']['usersByDevice'] is not None:
                                for user in json_data['data']['usersByDevice']:
                                    user_device = user['brand']
                                    total_count = user['count']
                                    percentage = user['percentage']

                                    record = {
                                        'state'  : state_folder,
                                        'year'   : year_folder,
                                        'quarter': quarter_file[0],
                                        'user_device': user_device,
                                        'total_count': total_count,
                                        'percentage': percentage
                                    }
                                    data.append(record)

    df = pd.DataFrame(data)
    print(df.head())

def map_user_df():
    map_user_directory = r'C:\Phonepe\pulse\data\map\user\hover\country\india\state'
   
    data = []
    for state_folder in os.listdir(map_user_directory):
        state_path = os.path.join(map_user_directory,state_folder)
        if os.path.isdir(state_path):

            for year_folder in os.listdir(state_path):
                year_path = os.path.join(state_path,year_folder)
                if os.path.isdir(year_path):

                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path,quarter_file)
                        
                        with open(quarter_path, 'r') as map_user_json_file:
                            json_data = json.load(map_user_json_file)
                            district_data = json_data['data']['hoverData']
                            for district_name, details in district_data.items():
                                district = district_name
                                registered_users = details['registeredUsers']
                                app_opens = details['appOpens']

                                record = {
                                        'state'  : state_folder,
                                        'year'   : year_folder,
                                        'quarter': quarter_file[0],
                                        'district': district[:-9],
                                        'registered_users': registered_users,
                                        'app_opens': app_opens
                                    }
                                data.append(record)

    df = pd.DataFrame(data)
    print(df)

def top_user_df():
    top_user_directory = r'C:\Phonepe\pulse\data\top\user\country\india\state'
   
    data = []
    for state_folder in os.listdir(top_user_directory):
        state_path = os.path.join(top_user_directory,state_folder)
        if os.path.isdir(state_path):

            for year_folder in os.listdir(state_path):
                year_path = os.path.join(state_path,year_folder)
                if os.path.isdir(year_path):

                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path,quarter_file)
                        
                        with open(quarter_path, 'r') as top_user_json_file:
                            json_data = json.load(top_user_json_file)

                            for pincode in json_data['data']['pincodes']:
                                pincode_num = pincode['name']
                                registered_users = pincode['registeredUsers']

                                record = {
                                        'state'  : state_folder,
                                        'year'   : year_folder,
                                        'quarter': quarter_file[0],
                                        'pincode': pincode_num,
                                        'registered_users': registered_users
                                    }
                                data.append(record)

    df = pd.DataFrame(data)
    #print(df[(df['state'] == 'tamil-nadu') & (df['year'] == '2018') & (df['quarter'] == '3')])
    print(df)
    

#aggregated_transaction_df()
#map_transaction_df()
#top_transaction_df()
#aggregated_user_df()
#map_user_df()
top_user_df()