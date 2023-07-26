user1 = {
"id": 1,
"name": "Leanne Graham",
"username": "Bret",
"email": "Sincere@april.biz",
"address": {
"street": "Kulas Light",
"suite": "Apt. 556",
"city": "Gwenborough",
"zipcode": "92998-3874",
"geo": {
"lat": "-37.3159",
"lng": "81.1496"
}
},
"phone": "1-770-736-8031 x56442",
"website": "hildegard.org",
"company": {
"name": "Romaguera-Crona",
"catchPhrase": "Multi-layered client-server neural-net",
"bs": "harness real-time e-markets"
}
}
# print(user1['name'])
# print(user1['address']['street'])
# print(user1["address"]['geo']['lat'])
# --------------------------------------------------------------------------------------
# using this user
# print yes if the company name starts with R else print no
# if user1['company']['name'].startswith('R'):
#     print('yes')
# else:
#     print('no')
# --------------------------------------------------------------------------------------
d1 = {'a': 155}
d2 = {'b': 188}
d2.update(d1)
print(d2)
# כתבו קוד בפייתון שמדפיס את כמות המפתחות בdict נתון:
dict1 = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7}
# expected result: the dict contains 6 keys
print(f'The dict contains {len(dict1.keys())} keys')
# תאר את המחשב שלך בעזרת מילון תאר את: צבע גודל מחיר וגובה
def create_comp_dict(color, size, price, height):
    comp_dict = {
        "color": color,
        "size": size,
        "price": price,
        "height": height
    }
    return comp_dict
my_comp = create_comp_dict('silver', '14 inches', '2000 ILS', '30 cm')
print(my_comp)

# write a python program to combine two dictionaries by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'c': 400, 'd': 400}
# sample output: Counter({'a: 400, 'b': 400, 'd': 400, 'c': 300})
d3 = {}
for k1, v1 in d1.items():
    if k1 not in d2.keys:
        d3[k1] = v1
    for k2, v2 in d2.items():
        if k1 == k2:
            d3[k1] = v1 + v2
        if k2 not in d1.keys:
            d3[k2] = v2
print(d3)


