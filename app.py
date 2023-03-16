import nltk
import en_core_web_sm
import urllib.request
from tqdm import tqdm
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

from geopy.geocoders import Nominatim


nlp = en_core_web_sm.load()

nltk.download('stopwords')

nltk.download('punkt')

stop_words = set(stopwords.words('english'))


def get_data_from_url(url):
    return urllib.request.urlopen(url).read()


def process_words(location):
    filtered_location = []
    location_tokens = word_tokenize(location.lower())

    [filtered_location.append(re.sub("[\n\r\t.,;]", "", token.replace("\\r"," ").replace("\\n"," "))) for token in location_tokens if token not in stop_words]
  
    return (" ").join(filtered_location).strip()


def get_location_data():
    url = 'https://www.gutenberg.org/files/103/103-0.txt'
    locations = []
    data = get_data_from_url(url)
    doc = nlp(str(data))
    [locations.append(process_words(loc.text))
                      for loc in doc.ents if loc.label_ == 'LOC']
    locations_set = set(locations)
    return list(locations_set)


def get_latitude_and_longitude_from_city_name(city_list):
    locations = []
    geolocator = Nominatim(user_agent="TestApp")
    for city in tqdm(city_list):
        try:
            location = geolocator.geocode(city)
            locations.append((city, location.latitude, location.longitude))
        except Exception as e:
            locations.append((city, 0, 0)) 
    return locations


if __name__ == "__main__":
    locations = get_location_data()
    latAndlong = get_latitude_and_longitude_from_city_name(locations)
    df = pd.DataFrame(latAndlong, columns=['Place','Lat','Long'])

    df = df.drop(df[(df.Lat == 	0.000000) & (df.Long == 	0.000000 )].index)
    df = df.dropna()
    
    df.to_csv("dataset.csv")

