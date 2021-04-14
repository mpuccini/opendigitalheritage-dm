import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://matt:1234@cluster0.8buoe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["sample_analytics"]
collection=db["customers"]

cursor=collection.find({ "name":"MatteoMaraziti" })
for doc in cursor:
    print(doc)