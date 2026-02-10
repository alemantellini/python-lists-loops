# EJERCICIO 16 - techno beat
def lyrics_generator(numbers):
    song = ""
    count_ones = 0
    for i in numbers:
        if i == 0:
            song += "Boom "
            count_ones = 0
        elif i == 1:
            song += "Drop the bass "
            count_ones += 1

            if count_ones == 3:
                song += "!!!Break the bass!!! "
                count_ones = 0
    return song

# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
