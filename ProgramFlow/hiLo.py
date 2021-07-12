low = 1
high = 1000

print(f"Please think of a number between {low} and {high}")
input("Press ENTER to start ")

guess = 1
guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input(f"My guess is {guess}. Should I guess higher or lower? "
                     f"Enter h or l, or c if my guess was correct ").casefold()
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower...
        high = guess -1
    elif high_low == "c":
        print(f"I got it in {guesses} guesses!")
        break
    else:
        print("please enter h, l or c")

    guesses += 1
else:
    print(f"You thought of the number {low}")
    print(f"I got it in {guesses} guesses")
