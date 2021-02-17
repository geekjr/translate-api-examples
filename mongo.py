from pymongo import MongoClient
import requests

mongo_client = MongoClient()

db = mongo_client.some_database
col = db.some_collection


def json_request(doc_to_send):
    url = "https://translation37.p.rapidapi.com/json/"

    payload = doc_to_send
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "YOUR-API-KEY",
        'x-rapidapi-host': "translation37.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    return response.text


for doc in col.find():
    # Translated is the translated document - you can do whatever you want with it :)
    translated = json_request(doc)
