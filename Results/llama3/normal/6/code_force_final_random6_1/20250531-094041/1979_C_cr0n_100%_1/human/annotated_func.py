#State of the program right berfore the function call: a and b are positive integers.
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of two positive integers a and b, which is calculated by multiplying a and b and then dividing by their greatest common divisor (gcd).

#Overall this is what the function does:This function calculates and returns the least common multiple (LCM) of two positive integers a and b.

#State of the program right berfore the function call: vals is a list of integers, N is a positive integer such that N = len(vals), and vals contains at least one element.
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: vals is a list of integers, N is a positive integer equal to the number of elements in vals, den is the result of func_1 applied to the result of func_1 applied to the result of func_1 applied to ... applied to the first element of vals and the first element of vals, and the second element of vals, and the third element of vals, ..., and the Nth element of vals, x is the Nth element of vals, stdin contains no input
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing because the return statement is empty. The value of den is still less than or equal to 0, and -1 has been printed. The list vals remains unchanged, and the value of x is still the Nth element of vals. The list vprod remains unchanged, and the value of N is still the number of elements in vals.
    #State: *vals is a list of integers, N is a positive integer equal to the number of elements in vals, den is the result of func_1 applied to the result of func_1 applied to the result of func_1 applied to ... applied to the first element of vals and the first element of vals, and the second element of vals, and the third element of vals, ..., and the Nth element of vals, minus the sum of the list vprod which is a list of integers where each element is the integer division of den by the corresponding element in vals, x is the Nth element of vals, stdin contains no input, vprod is a list of integers where each element is the integer division of the original value of den by the corresponding element in vals. den is larger than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: [den//vals[0]] [den//vals[1]] [den//vals[2]] ... [den//vals[N-1]] (where den is the result of repeatedly applying func_1 to the elements of vals, and vals is a list of integers)

#Overall this is what the function does:This function calculates the result of repeatedly applying the func_1 function to the elements of a list of integers, then uses this result to calculate a new list of integers where each element is the integer division of the result by the corresponding element in the original list. If the result minus the sum of the new list is less than or equal to 0, it prints -1 and returns without modifying the original list. Otherwise, it prints the new list of integers.

