name = input("What is your name? ")
age = int(input("And your age? "))

if 18 <= age <= 30:
    print(f"You are welcome, {name}")
else:
    print(f"Get out {name}")