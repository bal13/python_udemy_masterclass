shopping_List = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

# for index in range(6):
for index in range(len(shopping_List)):
    if shopping_List[index] == item_to_find:
        found_at = index
        break

print(f"Item found az position {found_at}")

item_to_find = "albatross"
found_at = None

# for index in range(6):
# for index in range(len(shopping_List)):
#     if shopping_List[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_List:
    found_at = shopping_List.index(item_to_find)

if found_at is not None:
    print(f"Item found az position {found_at}")
else:
    print(f"{item_to_find} is not found")
