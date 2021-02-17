"""
RUN: python json.py
"""

# -*- coding: utf-8 -*-
from translateAPI import translateAPI

response = translateAPI.json_request(
    "DOCUMENT-YOU-WANT-TRANSLATED, has to be dictionary",
    "YOUR-API-KEY-HERE")

print(response)
