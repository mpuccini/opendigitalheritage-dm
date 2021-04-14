import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://matt:1234@cluster0.8buoe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["sample_analytics"]
collection=db["customers"]

customerProva={
    "username": "MatMar",
    "name": "MatteoMaraziti",
    "address": "00152- via del corso, 100",
    "birthdate": {
        "date": "1999-03-22T11:37:34.000Z"
    },
    "email": "m.maraz@gmail.com",
    "accounts": [534932],
    "tier_and_details": {}
}

collection.insert_one(customerProva)
print("sono alla fine")