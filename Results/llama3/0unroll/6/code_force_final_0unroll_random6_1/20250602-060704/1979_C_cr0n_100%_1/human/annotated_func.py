#State of the program right berfore the function call: a and b are positive integers.
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of two positive integers a and b.

#Overall this is what the function does:Calculates and returns the least common multiple (LCM) of two positive integers a and b, which is the smallest number that is a multiple of both a and b.

#State of the program right berfore the function call: vals is a list of integers, N is a positive integer such that N = len(vals) and all elements in vals are greater than or equal to 2.
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: Output State: vals is a list of integers greater than or equal to 2, N is a positive integer equal to the number of elements in vals, den is an integer greater than or equal to 2 and is the result of func_1 applied to the initial value of den and each element in vals, in order.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing and ends its execution, with the current value of den being an integer less than or equal to 0, and -1 printed.
    #State: *vals is a list of integers greater than or equal to 2, N is a positive integer equal to the number of elements in vals, den is an integer greater than 0 and is the result of func_1 applied to the initial value of den and each element in vals, in order, vprod is a list of integers, where each element is the result of integer division of den by the corresponding element in vals, den is an integer equal to its original value minus the sum of the elements in vprod.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: [den // vals[0]] [den // vals[1]] ... [den // vals[N-1]] (where den is the result of func_1 applied to the initial value of den and each element in vals, in order, and N is the number of elements in vals)

#Overall this is what the function does:This function calculates the result of a custom operation (func_1) applied to the initial value of the first element in the input list (vals) and each subsequent element in the list, in order. It then uses this result to compute a list of integer divisions (vprod) and updates the result (den) by subtracting the sum of these divisions. If the updated result is less than or equal to 0, the function prints -1 and returns without any output. Otherwise, it prints the list of integer divisions (vprod) and returns without any output.

