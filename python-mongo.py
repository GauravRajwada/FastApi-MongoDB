from pymongo import MongoClient
import pprint
client = MongoClient(host="localhost", port=27017)
# client
# MongoClient(host=['localhost:27017'], ..., connect=True)
db = client.Cosmocloud


print(db)

products = db.products

# sampleProduct = { 
#     "ProductName": "Chimines", 
#     "ProductPrice": 155999, 
#     "ProductQuantity": 1
# }
# result = products.insert_one(sampleProduct)
# print(result)

# for row in products.find():
#     pprint.pprint(row)

# res = products.find_one({"ProductName": "Chimines"})
# pprint.pprint(res)

# client.close()

with MongoClient() as client:
    db = client.Cosmocloud
    for doc in db.products.find():
        pprint.pprint(doc)