#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 ≤ n ≤ 50). The second line contains n integers k_1,k_2,...,k_n (2 ≤ k_i ≤ 20).
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: Output State: stdin contains multiple test cases minus one, N is an integer between 1 and 50, vals is an empty list, prod is the product of all integers in the initial vals list.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing because the return statement is empty. The value of N remains an integer between 1 and 50, vals remains an empty list, prod remains the product of all integers in the initial vals list which is undefined since vals is empty, vprod remains an empty list, den remains less than or equal to 0, and -1 is still printed.
    #State: *N is an integer between 1 and 50, vals is an empty list, prod is the product of all integers in the initial vals list, vprod is an empty list, den is equal to prod and den is larger than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: (empty string)

#Overall this is what the function does:This function reads a test case from standard input, calculates the product of a list of integers, and then calculates the modular multiplicative inverse of each integer in the list. If the denominator of the modular multiplicative inverse is less than or equal to 0, it prints -1 and returns without printing the inverses. Otherwise, it prints the modular multiplicative inverses of the integers in the list. The function does not return any value.

