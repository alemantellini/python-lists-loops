# EJERCICIO 5.1 - sum odd items
my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]
# Your code here
def sum_odds(list):
    total = 0
    for x in range(len(list)):
        if list[x] % 2 != 0:
            total += list[x]
    return total
print(sum_odds(my_list))
