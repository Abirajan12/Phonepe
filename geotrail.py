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
        df = get_Geo_Query_Result('Statecount',year,quarter,state_names)
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
    
    elif query == 'States - Total Amount of Phone Pe Transactions':
        state_names = get_state_names_from_geojson()
        df = get_Geo_Query_Result('Stateamount',year,quarter,state_names)
        fig = px.choropleth(
            df,
            geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='sum_of_total_amount',
            color_continuous_scale='hot',
            range_color=(df['sum_of_total_amount'].min(), df['sum_of_total_amount'].max())
        )
        fig.update_geos(fitbounds="locations", visible=False)
        return df,fig
    
    elif query == 'States - Total count of Users':
        state_names = get_state_names_from_geojson()
        df = get_Geo_Query_Result('Stateusercount',year,quarter,state_names)
        fig = px.choropleth(
            df,
            geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='sum_of_total_count',
            color_continuous_scale='bupu',
            range_color=(df['sum_of_total_count'].min(), df['sum_of_total_count'].max())
        )
        fig.update_geos(fitbounds="locations", visible=False)
        return df,fig
    
    elif query == 'States - Percentage of Users':
        state_names = get_state_names_from_geojson()
        df = get_Geo_Query_Result('Stateuserpercent',year,quarter,state_names)
        fig = px.choropleth(
            df,
            geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='sum_of_percent',
            color_continuous_scale='jet',
            range_color=(df['sum_of_percent'].min(), df['sum_of_percent'].max())
        )
        fig.update_geos(fitbounds="locations", visible=False)
        return df,fig
    
    elif query == 'States - Registered Users':
        state_names = get_state_names_from_geojson()
        df = get_Geo_Query_Result('Statereguser',year,quarter,state_names)
        fig = px.choropleth(
            df,
            geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='total_reg_users',
            color_continuous_scale='turbo',
            range_color=(df['total_reg_users'].min(), df['total_reg_users'].max())
        )
        fig.update_geos(fitbounds="locations", visible=False)
        return df,fig
    
    elif query == 'States - App Opens':
        state_names = get_state_names_from_geojson()
        df = get_Geo_Query_Result('Stateappopens',year,quarter,state_names)
        fig = px.choropleth(
            df,
            geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='total_app_opens',
            color_continuous_scale='dense',
            range_color=(df['total_app_opens'].min(), df['total_app_opens'].max())
        )
        fig.update_geos(fitbounds="locations", visible=False)
        return df,fig

#st.plotly_chart(fig)