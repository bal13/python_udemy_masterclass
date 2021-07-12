def multiply(x: float, y: float) -> float:
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)
print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

# word = input("Please enter a word to check: ")
# if (is_palindrome(word)):
#     print(f"'{word}' is a palindrome")
# else:
#     print(f"'{word}' is NOT a palindrome")

answer = multiply(18, 3)
print(answer)


def fibonacci(n: int) -> int:
    """Return the ´n´ th Fibonacci number for positive ´n´ """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = is_palindrome(3)
