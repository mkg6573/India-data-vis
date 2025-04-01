import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv(r'india.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')


st.sidebar.title("India Data")
selected_state = st.sidebar.selectbox("Select a state",list_of_states)
primary = st.sidebar.selectbox("Select Primary Parameter",sorted(df.columns[5:]))
Secondary = st.sidebar.selectbox("Select Secondary Parameter",sorted(df.columns[5:]))

plot = st.sidebar.button("plot graph")

if plot:
    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=Secondary, zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1500,height=900,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)

    else:
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=Secondary, zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1500,height=900,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)