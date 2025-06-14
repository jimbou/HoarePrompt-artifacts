#State of the program right berfore the function call: x is an integer such that 2 <= x <= 1000.
def func_1(x):
    """Finds the y that maximizes gcd(x, y) + y.

  Args:
    x: The given integer.

  Returns:
    The optimal y.
  """
    max_val = 1
    for y in range(x - 1, 1, -1):
        if x % y == 0:
            if 2 * y >= x:
                return y
            max_val = y
        
    #State: x is an integer such that 2 <= x <= 1000, y is not defined, max_val is the largest divisor of x that is less than x and greater than 1, and the function has returned a value if there exists a divisor y such that 2 * y >= x.
    return max_val
    #The program returns the largest divisor of x that is less than x and greater than 1, provided that there exists a divisor y such that 2 * y >= x.
#Overall this is what the function does:The function `func_1` accepts an integer `x` (2 <= x <= 1000) and returns the largest divisor of `x` that is less than `x` and greater than 1, provided that there exists a divisor `y` such that 2 * y >= x. If no such divisor exists, the function returns 1.

