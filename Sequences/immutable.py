result = True
another_result = result
print(id(result))
print(id(result))

result = False
print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(result))

result += "ish"
print(id(result))