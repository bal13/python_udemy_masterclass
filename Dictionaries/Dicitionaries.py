fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making soda",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bushes",
         "lime": "a sour, green, citrus fruit",
         "apple": "round and crunchy"}

print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# del fruit["lemon"]
# print(fruit)
# # del fruit
# # fruit.clear()
# # print(fruit)
# # print(fruit["tomato"])
# print(fruit)
#
# # while True:
# #     dict_key = input("Please enter a fruit: ")
# #     if dict_key == "quit":
# #         break
# #     # description = fruit.get(dict_key, "We don't have "+dict_key)
# #     # print(description)
# #     if dict_key in fruit:
# #         description = fruit.get(dict_key)
# #         print(description)
# #     else:
# #         print("we don't have a " + dict_key)
#
# for snack in fruit:
#     print(fruit[snack])
#
# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("-" * 40)

# # ordered_keys = list(fruit.keys())
# # ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# for val in fruit.values():
#     print(val)
#
# print("-" * 40)
#
# for key in fruit:
#     print(fruit[key])


# print(fruit.keys())
#
# print(fruit.values())
#
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with icecream"
# print(fruit_keys)

print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))
