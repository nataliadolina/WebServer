import requests

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode=Хабаровск&format=json"
geocoder_request1 = "http://geocode-maps.yandex.ru/1.x/?geocode=Уфа&format=json"
geocoder_request2 = "http://geocode-maps.yandex.ru/1.x/?geocode=Нижний Новгород&format=json"
response = requests.get(geocoder_request)
response1 = requests.get(geocoder_request1)
response2 = requests.get(geocoder_request2)
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['Components'][1]["name"]
    print("Хабаровск относится к федеральному округу", toponym_address)
if response1:
    json_response1 = response1.json()
    toponym = json_response1["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['Components'][1]["name"]
    print("Уфа относится к федеральному округу", toponym_address)
if response2:
    json_response2 = response2.json()
    toponym = json_response2["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['Components'][1]["name"]
    print("Нижний Новгород относится к федеральному округу", toponym_address)
