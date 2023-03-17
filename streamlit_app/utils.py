import spacy
from geopy.geocoders import Nominatim
from tqdm import tqdm
import pandas as pd
import urllib.request
import os 

global LOC_MAP
LOC_MAP = set()

def getDataFromURL(url): 
    return urllib.request.urlopen(url).read()

def getAndSaveDatasetFromURL(url = 'https://www.gutenberg.org/files/103/103-0.txt', filename="words.txt"):
    if not os.path.exists(filename): 
        print(f"Getting data from {url}")
        data = getDataFromURL(url)
        with open(filename, "w") as f: 
            f.write(str(data))
        print(f"Data is stored in {filename}")
    else: 
        print("File already exists. Data loaded")

def preprocessDataFromFile(filename="words.txt"):
    with open(filename, "r") as f: 
        corpse = f.read()

    nlp = spacy.load("en_core_web_lg")
    doc_corpse = nlp(corpse)

    location_data = set()

    for ent in doc_corpse.ents:
        if ent.label_ == 'GPE':
            location_data.add(str(ent.text).replace("\n", " "))

    return list(location_data)

def getLatAndLong(data):
    locs = []
    err_count = {
        "count": 0,
        "places": []
    }
    geolocator = Nominatim(user_agent="aroundTheWorldIn80Days")
    for place in tqdm(data):
        place = place.lower()
        if place not in LOC_MAP:
            LOC_MAP.add(place)
            try:
                loc = geolocator.geocode(place)
                locs.append((place, loc.latitude, loc.longitude))
            except Exception as e: 
                err_count["count"] += 1
                err_count["places"].append(place)
    return locs, err_count

def sortedDataFrame(df):
    df['sort_lat'] = df["Lat"].astype("float64")
    df['sort_long'] = df["Long"].astype("float64")

    df.sort_values(['sort_long'], ascending=False, inplace=True)
    df.drop(['sort_lat', 'sort_long'], axis='columns', inplace=True)
    return df

def saveDataFrame(df, filename): 
    if not os.path.exists(filename): 
        df.to_csv(filename, index=False)
    else: 
        print("File already exists")


