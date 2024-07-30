from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://pasindu9225:Pasindu1234@lms.fudgrvm.mongodb.net/?retryWrites=true&w=majority&appName=lms"

# Create a new client and connect to the server
cluster = MongoClient(uri)
db = cluster['database1']
collection = db['collection1']

