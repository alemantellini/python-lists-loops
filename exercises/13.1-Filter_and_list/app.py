# EJERCICIO 13.1 - filter and list
all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]
# Your code here
def filter_function(name):
    # Update here
    return name.startswith("R")   
resulting_names = list(filter(filter_function, all_names))
print(resulting_names)
