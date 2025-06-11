#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer n (1 <= n <= 50). The second line contains n integers k_1,k_2,...,k_n (2 <= k_i <= 20).
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: Output State: N is an integer, vals is a list of integers, prod is the product of all integers in vals, stdin contains multiple test cases - 1
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing, as the return statement is empty. The values of N, vals, prod, vprod, and den remain unchanged. The current value of den is still less than or equal to 0. The program does not print anything, as the stdin contains multiple test cases - 1, and -1 is printed, but this is not related to the return statement.
    #State: *N is an integer, vals is a list of integers, prod is the product of all integers in vals, vprod is a list of integers where each element is the product of all integers in vals divided by the corresponding element in vals, den is an integer equal to the product of all integers in vals minus the sum of the elements in vprod, stdin contains multiple test cases - 1, and den is larger than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: [product of all integers in vals divided by the first element in vals] [product of all integers in vals divided by the second element in vals] ... [product of all integers in vals divided by the last element in vals]

#Overall this is what the function does:This function reads a test case from standard input, calculates the product of all integers in the test case, and then calculates the product of all integers divided by each integer. If the difference between the product of all integers and the sum of the products divided by each integer is less than or equal to 0, it prints -1. Otherwise, it prints the products divided by each integer. The function does not return any value and does not modify the input variables.

