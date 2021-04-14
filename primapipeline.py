import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://matt:1234@cluster0.8buoe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["sample_airbnb"]
collection=db["listingsAndReviews"]
pipeline =[
    {
        '$match': {
            'address.country': 'Turkey'
        }
    }, {
        '$group': {
            '_id': 'null', 
            'sum': {
                '$sum': '$number_of_reviews'
            }
        }
    }, {
        '$project': {
            '_id': 0, 
            'sum': 1
        }
    }
]
numRecensioni=list(collection.aggregate(pipeline))
print(numRecensioni)
