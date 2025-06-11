#State of the program right berfore the function call: a and b are positive integers.
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of two positive integers a and b, which is the product of a and b divided by their greatest common divisor (gcd).

#Overall this is what the function does:This function calculates and returns the least common multiple (LCM) of two positive integers, a and b, by dividing their product by their greatest common divisor (gcd).

#State of the program right berfore the function call: vals is a list of integers, N is an integer such that N = len(vals) and vals contains integers greater than or equal to 2.
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: Output State: vals is a list of integers, N is an integer equal to the length of vals, vals contains integers greater than or equal to 2, den is an integer equal to the result of func_1 applied to the first two elements of vals, then func_1 applied to the result and the third element of vals, and so on, until the last element of vals, stdin contains no input.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing, as there is no return statement with a value. The program simply ends without producing any output.
    #State: *vals is a list of integers, N is an integer equal to the length of vals, vals contains integers greater than or equal to 2, den is an integer equal to the result of func_1 applied to the first two elements of vals, then func_1 applied to the result and the third element of vals, and so on, until the last element of vals, minus the sum of the integer divisions of the original den by each element in vals, stdin contains no input. den is larger than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: the list of products of the elements in vals, where each product is calculated by multiplying the current product by the next element in vals, starting from the first element of vals, and the products are separated by spaces

#Overall this is what the function does:This function calculates the product of a list of integers and then calculates the product of each integer in the list with the overall product, minus the sum of the integer divisions of the overall product by each integer in the list. If the result of the subtraction is less than or equal to 0, it prints -1 and ends. Otherwise, it prints the list of products of each integer in the list with the overall product, separated by spaces.

