# -*- coding: utf-8 -*-
from translateAPI import translateAPI

response = translateAPI.text_request("TEXT-TO-TRANSLATE", 'YOUR-API-KEY')

print(response.text)