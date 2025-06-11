#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer n (1 ≤ n ≤ 50). The second line contains n integers k_1, k_2, ..., k_n (2 ≤ k_i ≤ 20).
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: stdin contains multiple test cases minus one test case, N is an integer between 1 and 50 inclusive, vals is an empty list, prod is an integer between 2^1 and 20^50 inclusive, r is the last integer in the list vals.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing because the return statement is empty, and the current value of den is less than or equal to 0, and -1 is being printed
    #State: *vals is an empty list, N is an integer between 1 and 50 inclusive, prod is an integer between 2^1 and 20^50 inclusive, r is the last integer in the list vals, vprod is an empty list, den is prod, and den is larger than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: (an empty string)

#Overall this is what the function does:This function reads a test case from standard input, calculates the product of a list of integers, and then calculates the denominator as the product minus the sum of the products of all possible combinations of the integers. If the denominator is less than or equal to 0, it prints -1 and returns without a value. Otherwise, it prints the list of products of all possible combinations of the integers, but since the list is empty, it effectively prints an empty string.

