prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for key_prices in prices:
    for key_stock in stock:
        if key_prices == key_stock:
            print(key_prices)
            print('price: ', prices.get(key_prices))
            print('stock: ', stock.get(key_stock))
total = 0
for key_prices,value_prices in prices.items():
        for key_stock, value_stock in stock.items():
            if key_prices == key_stock:
                total += value_prices * value_stock
print('Total: ' ,int(total))
