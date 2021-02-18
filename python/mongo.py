"""
RUN: python mongo.py
"""
# -*- coding: utf-8 -*-
from pymongo import MongoClient
from translateAPI import translateAPI

mongo_client = MongoClient('CONNECTION STRING')

db = mongo_client.some_database
col = db.some_collection


for doc in col.find():
    # Translated is the translated document - you can do whatever you want
    # with it :)
    translated = translateAPI.json_request(doc, "YOUR-API-KEY-HERE")
