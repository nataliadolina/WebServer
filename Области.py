import requests

cities = ["Барнаул", "Мелеуз", "Йошкар-Ола"]
geocoder_request = None
for i in range(3):
    if i == 0:
        geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode={}&format=json".format(cities[i])
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['Components'][2]["name"]
        print(cities[i], "относится к области", toponym_address)
