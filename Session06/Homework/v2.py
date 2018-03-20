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
    "title" : "Real Rap",
    "author" : "Tài Smile",
    "content" : """
    có nhiều thằng đang muốn bắn tao (paprrapap poom poom)
    giã con vợ mày như giã gạo (cacrracac coom coom)
    cắc cùm cum. cắc cùm cum. fuck con vợ mày tùm lum
    giã từ lotte đến kangnam, từ sàn nhà lên lan can
    gọi bạn bè qua gangbang.

    baby i'm real.
    baby i'm real.
    nhạc lên là phiêu.
    baby i'm real.
    """
 }

db.posts.insert_one(new_post)
