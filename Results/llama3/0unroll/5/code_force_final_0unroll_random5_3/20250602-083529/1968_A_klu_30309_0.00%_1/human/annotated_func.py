#State of the program right berfore the function call: x is an integer such that 2 <= x <= 1000.
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
        
    #State: max_val is the largest factor of x less than x/2, x remains unchanged.
    return max_val
    #The program returns the largest factor of x that is less than x/2.

#Overall this is what the function does:This function finds the largest factor of a given integer x that is less than x/2, or returns x/2 if it is a factor of x, otherwise returns the largest factor of x less than x/2.

