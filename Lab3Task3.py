from geopy.exc import GeocoderUnavailable

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify")

from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.geocode,  min_delay_seconds  =  0.3) 

import requests

import pprint

import folium

def twitter_data(name):

    base_url = 'https://api.twitter.com/'

    bearer_token = 'AAAAAAAAAAAAAAAAAAAAAP8nNAEAAAAAg8fR4Xy%2F9C%2F022I69SE5v5rBhXY%3Dd3IUas4TLJmNmi3qDVLVf0CfyJHhWrLCbg4HUDg3xdQrGIvyuV'

    search_url = f'{base_url}1.1/friends/list.json'

    search_headers = {
        'Authorization' : 'Bearer {}'.format(bearer_token)
    }

    search_params = {
        'screen_name': name,
        'count' : 50
    }

    responce = requests.get(search_url, headers= search_headers, params= search_params)

    json_responce = responce.json()

    return json_responce["users"]

def get_location_and_name(users):
    list_of_location = []
    for i in range(len(users)):
        if users[i]["location"] != "":
            list_of_location.append((users[i]["screen_name"],users[i]["location"]))
    return list_of_location

def folium_map(lst):
    if len(lst) < 1:
        return "failure"
    followers_map = folium.Map(tiles='OpenStreetMap')
    fg = folium.FeatureGroup(name='map')

    for loc in lst:

        location = geolocator.geocode(loc[1])
        try:
            fg.add_child(folium.Marker(location=((location.latitude,location.longitude)),
                                    popup = loc[0]))
        except AttributeError:
            pass
        except  GeocoderUnavailable:
            pass
    followers_map.add_child(fg)

    return followers_map

