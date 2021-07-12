shopping_List = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_List:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_List:
    if item == "spam":
        continue

    print("Buy " + item)
print("-" * 80)
for item in shopping_List:
    if item == "spam":
        break

    print("Buy " + item)