# EJERCICIO 12 - map a list
celsius_values = [-2, 34, 56, -10]
def celsius_to_fahrenheit(celsius):
    # The magic happens here
    total = (celsius * 9/5) + 32
    return total 
result = list(map(celsius_to_fahrenheit, celsius_values))
print(result)
