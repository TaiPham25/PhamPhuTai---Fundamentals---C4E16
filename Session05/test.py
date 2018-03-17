# person = ['Quy', 20, 0, 'Ha Noi', 'Vinh Phuc', 3, 10, ['coding', 'manga', 'ping pong']]

# #dictionary


#creave
person = {
    #key      #value
    "name" : "Quy",
    "age" : 20,
    "ex" : 0,
    "sex" : "male",
}
#read
# key = "age"
# if "age" in person:
#     print(person[key])
# else:
#     print('not found')

#key
# for k in person:
#     print (k, person[k])

#value
# for value in person.values():
#     print(value)

#key and value
# for key,value in person.items():
#     print(key, value)

#update
# person["age"] += 3

#append
person['school'] = 'HUST'
print(person)
