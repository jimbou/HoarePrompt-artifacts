#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 50). The second line contains n integers k_1, k_2, ..., k_n (2 <= k_i <= 20).
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: N is an integer between 1 and 50 inclusive, vals is an empty list, r is the last integer in the list, prod is equal to the product of all integers in the list, stdin contains multiple test cases minus one test case.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing because the return statement is empty. The current state of the variables remains unchanged: N is an integer between 1 and 50 inclusive, vals is a list, r is the last integer in the list, prod is equal to the product of all integers in the list, vprod is a list, den is equal to prod and the current value of den is less than or equal to 0, and -1 has been printed.
    #State: *N is an integer between 1 and 50 inclusive, vals is an empty list, r is the last integer in the list, prod is equal to the product of all integers in the list, vprod is an empty list, den is equal to prod and is larger than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: (an empty string)

#Overall this is what the function does:This function reads a test case from standard input, calculates the product of a list of integers, and then computes the modular multiplicative inverse of each integer in the list. If the denominator of the modular multiplicative inverse is less than or equal to 0, it prints -1. Otherwise, it prints the modular multiplicative inverses of the integers in the list. The function does not return any value.

