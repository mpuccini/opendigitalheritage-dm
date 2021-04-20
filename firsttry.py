import pymongo
from pymongo import MongoClient 
cluster0=MongoClient("mongodb+srv://giacomo:12345@cluster0.8buoe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster0["sample_airbnb"]
collection=db["listingsAndReviews"]
pipeline=[
    {
        '$match': {
            'price': {
                '$lt': 15
            }
        }
    }, {
        '$project': {
            'price': 1, 
            'name': 1
        }
    }
]
for doc in list(collection.aggregate(pipeline)):
    print(doc)
    print("\n")