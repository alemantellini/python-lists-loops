# EJERCICIO 14.1 - letter counter
par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"
counts = {}
# Your code here
for letter in par:
    if letter != " ":
        lower_letter = letter.lower()
        if lower_letter in counts:
            counts[lower_letter] += 1
        else:
            counts[lower_letter] = 1
print(counts)
