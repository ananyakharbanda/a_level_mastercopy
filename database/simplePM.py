
from pymongo import MongoClient

client = MongoClient("127.0.0.1", 27017)

db = client["a_level"]
coll = db["users"]

for i in coll.find():
    print(i)

print(coll.count_documents({}))


