import requests

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode={}&format=json".format('Петровка, 38')
response = requests.get(geocoder_request)
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['postal_code']
    print('Почтовый индекс Московского Уголовного Розыска -', toponym_address)
