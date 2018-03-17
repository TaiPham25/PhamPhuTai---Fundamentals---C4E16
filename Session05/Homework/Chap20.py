
string = 'ThiS is String with Upper and lower case Letters'
alphabet = {}
for i in string.lower():
    alphabet[i] = alphabet.get(i,0) + 1
for i in alphabet.items():
    print(*i)
