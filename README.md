# PhonePe Pulse 2.0

This project aims for a live geo visualization dashboard that displays
information and insights from the Phonepe pulse Github repository in an interactive and visually appealing manner.

## Table of Contents

    1. Installation
    2. Github repository cloning
    3. Data Extraction and Processing
    4. Data Insertion
    5. Data and Geo Visualization
    6. Dynamic updating of data
    4. Usage
    5. Documentation
    6. Demo

## 1. Installation

    UI
    --
    import streamlit as st
    import plotly.express as px

    Database Insertion and Retrieval
    --------------------------------
    import mysql.connector
    import pandas as pd
    import json
    import numpy as np

    Data Visualization
    ------------------
    import plotly.graph_objects as go
    import plotly.express as px

## 2. Github repository cloning

    For this project, the data gets extracted from the PhonePe Pulse pulse Github repository through scripting and cloning. The link to the Pulse data repository is as below
    https://github.com/PhonePe/pulse#readme

## 3. Data Extraction and Processing

    As mentioned in the problem statement, after cloning the repository to the folder, convert all the json data files to appropriate dataframes using
        * get_aggregated_transaction_df()
        * get_map_transaction_df()
        * get_top_transaction_df()
        * get_aggregated_user_df()
        * get_map_user_df()
        * get_top_user_df()

    For the Processing part, since the null values have been handled already in the above functions, the rest of the data transformations done by using
        * transform_df(df)

## 4. Data Insertion

    All those cleaned and Processed dataframes got inserted as mysql tables with the functions in
        -> mysql_data_insertion.py
    using "mysql-connector-python"

## 5. Data and Geo Visualization

    The Streamlit and Plotly libraries in Python have been used to create an interactive and visually appealing dashboard.

    This project has 3 major tabs.
        * Transaction
        * User
        * Geo
    Each of these sections have 3 major drop downs, wherein which two of them for querying against the year and the quarter. All those query results will be fetched from the database as requested by the user using these functions
        * get_Transaction_Query_Result(query, year, quarter)
        * get_User_Query_Result(query, year, quarter)
        * get_Geo_Query(query_word, year, quarter)
        * get_Geo_Query_Result(query_word,year, quarter,state_names)

## 6. Dynamic updating of data

    Plotly's built-in geo map functions can be used to display the data on a map and Streamlit can be used to create a user-friendly interface with multiple dropdown options for users to select different facts and figures to display in
        -> main.py
        -> geotrail.py

## 7. Usage

    PhonePe Pulse 2.0 can be used to compare the data related to transactions, users over the years and across all the quarters in a visually appealing manner

## 8. Documentation

[PhonePe Pulse Data](https://github.com/PhonePe/pulse#readme)

[Indian states Geojson](https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson)

## 9. Demo

[PhonePe Pulse 2.0 Demo link](https://www.linkedin.com/posts/abirami-rengarajan-4b017b27a_phonepepulse-datascience-visualization-activity-7079003576873730048-Noz9?utm_source=share&utm_medium=member_desktop)
