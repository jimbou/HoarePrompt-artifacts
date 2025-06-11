#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 5000) followed by t test cases. Each test case contains an integer n (1 ≤ n ≤ 50) followed by 2n integers a_1,a_2,...,a_{2n} (1 ≤ a_i ≤ 10^7).
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: t is 0, n is an integer between 1 and 50 inclusive, A is a list of 2n integers where each integer is between 1 and 10^7 inclusive, stdin contains no test cases, and the sum of all the elements at even indices of the list A is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains an integer n followed by 2n integers. It then calculates and prints the sum of the integers at even indices (0-based indexing) for each test case. The function continues this process until all test cases have been processed, at which point it terminates.

