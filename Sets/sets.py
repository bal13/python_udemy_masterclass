# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

#
# empty_set = set()
# empty_set2 = {}
# empty_set.add("a")
# # empty_set2.add("a")
#
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
#
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print("-" * 40)
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

# print(sorted(even))
# squares = set(squares_tuple)
# print(sorted(squares))
#
#
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)
#
# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))

# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  # no error, does nothing
# print(squares)
# squares.remove(8)  # error
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 9 is not the member of the set")

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(squares)
#
# if squares.issubset(even):
#     print("squares is a subset is even")
#
# if even.issuperset(squares):
#     print("even is a superset os squares")
#

even = frozenset(range(0, 100, 2))

print(even)
even.add(3)