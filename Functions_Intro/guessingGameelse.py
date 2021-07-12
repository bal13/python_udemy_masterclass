import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("Szááámot")


highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing


print(f"Please guess number between 1 and {highest}: ")

guessed = False

while not guessed:
    guess = get_integer(": ")
    if guess > answer:
        print("Lower")
        continue
    elif guess < answer:
        print("Higher")
        continue
    else:
        print("Yeah, right!")
        guessed = True

# if guess != answer:
#     if guess < answer:
#         print("Higher")
#     else:
#         print("Lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#         print("Sorry")
# else:
#     print("Wow")
# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done!")
#     else:
#         print("Sorry...")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done!")
#     else:
#         print("Sorry...")
# else:
#     print("You got it first time")


