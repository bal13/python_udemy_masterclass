
# Python3 program to Split string into characters
def split(word):
    return [char for char in word]


vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
input_string = input("Írjad be a szöveget e!: ")

print(split(input_string))

print(''.join(sorted(set(split(input_string)).difference(vowels))))