
chosen_item = None

print("1. Valami")
print("2. Ezazz")
print("3. Naaa")
print("0. Exit")


while chosen_item != 0:
    chosen_item = int(input("Válassz! "))
    if chosen_item not in range(0, 4):
        print("Rossz válasz!")
    else:
        print(f"Ezt választottad: {chosen_item}")
else:
    print("Vége a dalnak")
