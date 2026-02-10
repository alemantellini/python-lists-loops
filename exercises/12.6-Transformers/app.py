# EJERCICIO 12.6 - Transformers
incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here
def full_name(person):
    return person["name"] + " " + person["last_name"]

def data_transformer(strings):
    return list(map(full_name, strings))

print(data_transformer(incoming_ajax_data))
