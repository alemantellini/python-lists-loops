# EJERCICIO 9 - max integer from list
my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]
# Your code here
def max_integer(list):
    result = 0
    for i in list:
        if i > result:
            result = i
    return result
print(max_integer(my_list))
