from pymongo import MongoClient
mongo_uri = 'mongodb://admin:tai123@ds117719.mlab.com:17719/c4e16_taipham'

#connect database
client = MongoClient(mongo_uri)

#get database
db = client.get_default_database()

# create collection
games = db['games']
favorites = db['like']

# # creave document
# new_game = {
#     "name" : "Hung bia",
#     "description" : "best game ever!"
# }
#
# new_favorite = {
    # "1": "movie",
    # "2": "sleep",
    # "3": "swimming",
    # "4": "shopping",
    # "5": "travel",
    # "6": "kissing",
    # "7": "dancing",
    # "8": "basketball",
    # "9": "girlfriend",
    # "10": "game"
#
# # put document in collection
# games.insert_one(new_game)
# favorites.insert_one(new_favorite)

#read
all_game =favorites.find()
for favorite in all_game:
    print(favorite['1'])
