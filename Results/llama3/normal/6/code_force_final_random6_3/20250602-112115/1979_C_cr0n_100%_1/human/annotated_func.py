#State of the program right berfore the function call: a and b are positive integers.
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of two positive integers a and b, which is the product of a and b divided by their greatest common divisor (gcd).

#Overall this is what the function does:Calculates and returns the least common multiple (LCM) of two positive integers a and b, which is the product of a and b divided by their greatest common divisor (gcd).

#State of the program right berfore the function call: vals is a list of integers, N is an integer such that N = len(vals) and vals contains at least one element.
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: N is an integer, vals is an empty list, den is the result of func_1 applied to the last element of vals and the last element in the list, stdin is empty, x is the last element in the list
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None
    #State: *N is an integer, vals is an empty list, den is the result of func_1 applied to the last element of vals and the last element in the list minus the sum of the list comprehension of (den // r) for r in vals, stdin is empty, x is the last element in the list, and den is larger than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: an empty string

#Overall this is what the function does:This function calculates the result of a custom operation (func_1) applied to all elements in a list of integers, then uses this result to compute a new list of values (vprod) by dividing the result by each element in the original list. If the final result (den) is less than or equal to 0, it prints -1 and returns None. Otherwise, it prints the new list of values (vprod) and returns None.

