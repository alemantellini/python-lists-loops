# EJERCICIO 12.5 - yes and no
the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
# Your code here
def wikiwoko(element):
    if element == 1:
        return "wiki"
    else:
        return "woko"
my_list = list(map(wikiwoko, the_bools))
print(my_list)
