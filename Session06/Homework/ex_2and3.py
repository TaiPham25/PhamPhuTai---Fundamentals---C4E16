from pymongo import MongoClient
mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

#connect database
client = MongoClient(mongo_uri)

#get database
db = client.get_default_database()

# create collection
posts = db['posts']

#create document
new_post = {
    "title" : "Ngáo Ngơ",
    "author" : "Tài Smile",
    "content" : """
    Tôi là ai...
             .... đây ....
    .......là đâu !
    Lạc trôi giữa đời...
    .....ớ u ớ.
     """
 }

db.posts.insert_one(new_post)
