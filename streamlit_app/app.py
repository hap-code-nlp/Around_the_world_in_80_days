import streamlit as st
from streamlit_folium import st_folium
import folium

import pandas as pd 
import numpy as np

from constants import *

st.set_page_config(page_title= "Foggs Journey", layout="wide")
st.title(f"{APP_TITLE}...")

st.text(f"The visualization of the {LOCATION_DATASET}. The dataset can be found below the map")
st.markdown("Check out the code [here](https://github.com/hap-code-nlp/Around_the_world_in_80_days/tree/main/streamlit_app)")
df = pd.read_csv(LOCATION_DATASET)
loc_df = df
df = df[["Place", "Lat", "Long"]].values.tolist()


latAndLong = list()
locationMap = folium.Map(location=[0,0], zoom_start=2)

for i in range(len(df)): 
    popup = folium.Popup(f"City: {df[i][0]}", max_width = 250)
    folium.Marker(location=df[i][1: ], popup=popup, icon=folium.DivIcon(html="""<div style="height: 2px; width: 2px; border-radius: 50%; background-color: red"></div>""")).add_to(locationMap)
    if i != 0: 
        cur = df[i-1][1: ]
        nex = df[i][1: ]
        latAndLong.append([cur, nex])
folium.PolyLine(latAndLong).add_to(locationMap)

st_folium(locationMap, key=APP_TITLE, width=MAP_WIDTH, height=MAP_HEIGHT)

st.header("Locations")
st.text(f"{LOCATION_DATASET}")
loc_df

st.header("Tech Stack")
st.markdown(
"""
- SpaCy
- Geopy
- Streamlit
""")

st.header("Developed by")
st.markdown(
"""
<a href="https://github.com/Hemanthhari2000" title="Hemanth Kumar"><img src = "https://github.com/hemanthhari2000.png?size=50" style = "border-radius: 50%" /></a>
<a href="https://github.com/antoprince001" title="Antony Prince"><img src = "https://github.com/antoprince001.png?size=50" style = "border-radius: 50%" /></a>

""", unsafe_allow_html=True)