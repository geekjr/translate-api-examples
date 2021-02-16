# -*- coding: utf-8 -*-
import requests

url = "https://translation37.p.rapidapi.com/image/"

payload = {"lang": "LANG IN IMAGE"}
headers = {
    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
    'x-rapidapi-key': "YOUR-API-KEY",
    'x-rapidapi-host': "translation37.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, files={'file': open('FILE', 'r')}, headers=headers)

print(response.text)