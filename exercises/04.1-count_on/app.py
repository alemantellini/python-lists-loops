# EJERCICIO 4.1 - count on
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]
# Your code here
new_list = []
for x in range(len(my_list)):
    list_type = type(my_list[x])
    if list_type is list or list_type is dict:
        new_list.append(my_list[x])
print(new_list)
