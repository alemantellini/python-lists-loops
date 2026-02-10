# EJERCICIO 4 - mixed list
mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]
# Your code below
def values(list):
    for x in range(len(list)):
        mix_type = type(list[x])
        print(mix_type)
values(mix)
