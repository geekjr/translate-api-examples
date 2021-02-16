# -*- coding: utf-8 -*-

import requests


url = "https://translation37.p.rapidapi.com/text/"

payload = {"text": "TEXT TO TRANSLATE"}
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "YOUR-API-KEY",
    'x-rapidapi-host': "translation37.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)