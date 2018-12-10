# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:46:50 2018

@author: jpz
"""
import pymongo
import requests
from pymongo import MongoClient
client = MongoClient('localhost', 27017) # client starten

db = client['firstdb'] # database aanmaken



# db.create_collection('secondcol') # gebeurt hieronder al
collection = db['secondcol']

response = requests.get('https://amerpodia.yesplan.nl/api/events/date%3A02-05-2017?api_key=030A44EB593240A3207CF3E245C8D291') 

Resp = response.json()

# print (Resp['data'])

for item in Resp['data']:
    collection.insert_one(item)
 
    
        

#   return [element for element in Resp if element ['name'] == name]
 






# collection.insert_many(InsResp(x))




