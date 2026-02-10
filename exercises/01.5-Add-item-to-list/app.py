# EJERCICIO 1.5 - add item to list
# Remember to import random function here
import random
my_list = [4, 5, 734, 43, 45]
# The magic goes below
for x in range(10):
    number = random.randint(1,11)
    my_list.append(number)
    print(my_list)
