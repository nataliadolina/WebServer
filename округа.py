import requests

cities = ["Хабаровск", "Уфа", "Нижний Новгород", "Калининград"]
for i in range(4):
    geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode={}&format=json".format(cities[i])
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['Components'][1]["name"]
        print(cities[i], "относится к федеральному округу", toponym_address)
