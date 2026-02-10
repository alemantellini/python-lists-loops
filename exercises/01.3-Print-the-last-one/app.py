# EJERCICIO 1.3 - print the last one
# import the random package here "import random"
import random
def generate_random_list():
    aux_list = []
    randonlength = random.randint(1, 100)
    for i in range(randonlength):
        aux_list.append(randonlength)
        i += i
    return aux_list
my_stupid_list = generate_random_list()
# Write your code below this comment, good luck!
list_len = len(my_stupid_list)
the_last_one = my_stupid_list[list_len -1]
print(the_last_one)
