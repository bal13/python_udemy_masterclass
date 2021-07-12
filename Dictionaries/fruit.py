fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making soda",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bushes",
         "lime": "a sour, green, citrus fruit",
         "apple": "round and crunchy"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have more fruits, please"}

print(veg)

# veg.update(fruit)
# print(veg)
#
# print(fruit.update(veg))
# print(fruit)
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
print(veg)
print(fruit)