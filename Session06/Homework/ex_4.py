from pymongo import MongoClient
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot
mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

#connect database
client = MongoClient(mongo_uri)

#get database
db = client.get_default_database()

# create collection
customers = db['customers']

#count
customers_ads = 0
customers_wom = 0
customers_events = 0
for customer in customers.find():
    if customer['ref'] == 'ads':
        customers_ads += 1
    elif customer['ref'] == 'wom':
        customers_wom += 1
    else:
        customers_events += 1
print("Number of customers group by refs: events : {0}, wom : {1}, ads : {2}".format(customers_events, customers_wom, customers_ads))

# prepare data
labels = ["ads", "wom", "events"]
values = [customers_ads, customers_wom, customers_events]
colors = ['green', 'gold','purple']

#plot
pyplot.pie(values,labels= labels,colors=colors,autopct='%.2f%%')
pyplot.axis('equal')
#show
pyplot.show()
