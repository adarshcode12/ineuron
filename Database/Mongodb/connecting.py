# import pymongo
# client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.sm9s5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test

import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
print(client)