import sys
from io import BytesIO
from get_map_scale import get_scale

import json
import requests
from PIL import Image


toponym_to_find = "австралия"

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
print(response.links)
if not response:
    pass


json_response = response.json()

toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]

toponym_coodrinates = toponym["Point"]["pos"]

toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")


json.dump(json_response, open("rs.json", "w", encoding='utf-8'), ensure_ascii=False)


map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": get_scale(toponym_to_find),
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"

response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()