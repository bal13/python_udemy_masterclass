import random


def get_integer(prompt):
    """
       Get an integer from Standard input (stdin).

   The function will continue looping and prompting
   the user, until a valid int is entered
   Args:
       prompt: The String the user will see, when
       they're prompted to enter the value,

   Returns: The integer that the user enters

    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("Szááámot")


print(input.__doc__)
print("*"*80)
print(get_integer.__doc__)

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


