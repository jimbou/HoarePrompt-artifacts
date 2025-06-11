#State of the program right berfore the function call: a and b are positive integers.
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of two positive integers a and b, which is the product of a and b divided by their greatest common divisor (gcd).

#Overall this is what the function does:This function calculates and returns the least common multiple (LCM) of two positive integers, a and b, by dividing their product by their greatest common divisor (gcd).

#State of the program right berfore the function call: vals is a list of integers, N is a positive integer equal to len(vals), and vals contains integers greater than 1.
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: N is a positive integer, vals is an empty list, x is the last integer in the initial vals, den is the result of func_1 applied to the initial den and each integer in the initial vals in order, stdin is empty
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None
    #State: *N is a positive integer, vals is an empty list, x is the last integer in the initial vals, den is the result of func_1 applied to the initial den and each integer in the initial vals in order, minus the sum of the quotients of den divided by each integer in the initial vals. den is larger than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: nothing

#Overall this is what the function does:This function calculates the least common multiple (LCM) of a list of integers, then subtracts the sum of the quotients of the LCM divided by each integer, and prints the quotients if the result is positive; otherwise, it prints -1 and returns None.

