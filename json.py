# -*- coding: utf-8 -*-
import requests

url = "https://translation37.p.rapidapi.com/json/"

payload = {"YOUR": "JSON_HERE"}
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "YOUR-API-KEY",
    'x-rapidapi-host': "translation37.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)