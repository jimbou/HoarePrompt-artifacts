#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains a single integer n (1 ≤ n ≤ 50). The second line of each test case contains n integers k_1,k_2,…,k_n (2 ≤ k_i ≤ 20).
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: stdin contains multiple test cases minus one, N is an integer between 1 and 50 inclusive, vals is an empty list, prod is an integer between 2^N and 20^N inclusive, r is an integer between 2 and 20 inclusive.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing because there is no value or variable specified in the return statement.
    #State: *vals is an empty list, N is an integer between 1 and 50 inclusive, prod is an integer between 2^N and 20^N inclusive, r is an integer between 2 and 20 inclusive, vprod is an empty list, den is an integer equal to prod and den is larger than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: (empty string)

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It reads an integer N and a list of N integers, calculates the product of the integers, and then calculates the quotient of the product divided by each integer. If the sum of these quotients is less than or equal to 0, it prints -1. Otherwise, it prints the list of quotients. The function does not return any value.

