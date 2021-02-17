# -*- coding: utf-8 -*-
from translateAPI import translateAPI


response = translateAPI.image_request('PATH-TO-IMAGE', 'YOUR-API-KEY')

print(response.text)