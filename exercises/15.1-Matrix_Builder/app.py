# EJERCICIO 15.1 - matrix builder
# Your code here
def matrix_builder(integer):
    result = []
    for i in range(integer):
        row = []
        for x in range(integer):
            row.append(1)
        result.append(row)
    return result
print(matrix_builder(3))
