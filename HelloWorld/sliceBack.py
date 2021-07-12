letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)
backwards = letters[25:-1:-1]   # Nem oké!!!
print(backwards)
backwards = letters[25::-1]
print(backwards)
backwards = letters[::-1]
print(backwards)

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])

