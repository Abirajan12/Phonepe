import pandas as pd
import plotly.express as px
import requests
from mysql_data_retrieval import *

def get_state_names_from_geojson():
    # URL of the JSON file
    url = 'https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson'
    # Send a GET request to the URL and retrieve the JSON data
    response = requests.get(url)
    data = response.json()
    # Extract the state names
    state_names = [feature['properties']['ST_NM'] for feature in data['features']]
    state_names.sort()
    return state_names

def get_Geo_Json_Result(query, year, quarter):
    
    if query == 'Drag to choose query':
        return None, None

    elif query == 'State and Total count of Phonepe Transactions':
        state_names = get_state_names_from_geojson()
        df = get_Geo_Query_Result('State',year,quarter,state_names)
        df['sum_of_total_count'] = pd.to_numeric(df['sum_of_total_count'])
        fig = px.choropleth(
            df,
            geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='sum_of_total_count',
            color_continuous_scale='YlGn',
            range_color=(df['sum_of_total_count'].min(), df['sum_of_total_count'].max())
        )
        fig.update_geos(fitbounds="locations", visible=False)
        return df,fig

#st.plotly_chart(fig)