"""
RUN: python rdbms.py
"""
# -*- coding: utf-8 -*-
# In this example, we will use MySQL. Function is nearly identical for
# PostGRES.

from translateAPI import translateAPI


# This function(and the PostGRES one) return queries that have translated values.
# You can use these queries to insert into another database.
translated = translateAPI.mysql(
    "URL_TO_SERVER",
    "USERNAME",
    "PASSWORD",
    "TABLE-NAME",
    "DATABASE NAME",
    "YOUR-API-KEY")
print(translated)
