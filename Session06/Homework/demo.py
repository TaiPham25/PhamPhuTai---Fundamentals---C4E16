customers = db['customers']

#count
count_customers = customers.find()
customers_ads = 0
customers_wom = 0
customers_events = 0
for customer in customers:
    if customer['ref'] == 'ads':
        customers_ads += 1
    elif customer['ref'] == 'wom':
        customers_wom += 1
    else:
        customers_events += 1
