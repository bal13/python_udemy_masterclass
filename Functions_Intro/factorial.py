def factorial(input_number: int) -> int:
    """
    Visszadja egy szám faktoriálisát
    @param input_number: a szám
    @return: faktoriális
    """
    ret_val = 1
    if input_number > 0:
        for i in range(input_number):
            ret_val *= i+1

    return ret_val

print(factorial(3))