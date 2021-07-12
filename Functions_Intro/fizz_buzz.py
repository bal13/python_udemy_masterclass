def fizz_buzz(input_number: int) -> str:
    """

    @param input_number: Szám amire futtatjuk
    @return: fizz vagy buzz vagy fizzbuzz vagy a szám
    """
    if input_number % 15 == 0:
        return "fizz buzz"
    elif input_number % 5 == 0:
        return "buzz"
    elif input_number % 3 == 0:
        return "fizz"
    else:
        return str(input_number)


# for i in range(100):
#     print(f"{i}: {fizz_buzz(i)}")
#
# input("Play fizz buzz, Press ENTER to start")
# print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print(f"WRONG, the correct answer was {correct_answer}")
        break
else:
    print(f"Well done you reached {next_number}")
