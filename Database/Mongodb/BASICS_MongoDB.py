# install mongodb(community version) - (https://www.mongodb.com/try/download/community?tck=docs_server)
#Install [MongoDB compass](https://www.mongodb.com/products/compass) (Optional)


# to connect python with the mongodb 
# python -m pip install pymongo

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
print(client)
#MongoClient(connect=True) then it is connected

