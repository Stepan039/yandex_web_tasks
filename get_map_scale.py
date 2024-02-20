def get_scale(object_name):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": object_name,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        return "90, 90"

    json_response = response.json()

    lower_corner = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"]["lowerCorner"]
    upper_corner = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"]["upperCorner"]

    down, left = map(float, lower_corner.split())
    up, right = map(float, upper_corner.split())
    return str(up - down) + "," + str(right - left)
