# EJERCICIO 12.2 - map function inside variable
names = ['Alice', 'Bob', 'Marry', 'Joe', 'Hilary', 'Stevia', 'Dylan']
def prepender(name):
    return "My name is: " + name
# Your code here
new_list = list(map(prepender, names))
print(new_list)
