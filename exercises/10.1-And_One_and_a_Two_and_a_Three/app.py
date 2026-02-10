# EJERCICIO 10.1 - and one and a two and a three
contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
# Your code here
keys = contact.keys()
values = contact.values()
items = contact.items()
for i in items:
    print(i[0]+":"+" "+i[1])
