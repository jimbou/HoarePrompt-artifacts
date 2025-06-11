#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 5000) followed by t test cases. Each test case contains an integer n (1 ≤ n ≤ 50) followed by 2n integers a_1,a_2,...,a_{2n} (1 ≤ a_i ≤ 10^7).
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: t is an integer (0 ≤ t ≤ 0), n is an integer (1 ≤ n ≤ 50), A is a list of 2n integers (1 ≤ a_i ≤ 10^7), stdin contains t test cases, each test case contains an integer n (1 ≤ n ≤ 50) followed by 2n integers a_1,a_2,...,a_{2n} (1 ≤ a_i ≤ 10^7), and the sum of all elements at even indices of the list A has been printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It then calculates and prints the sum of the integers at even indices (0-based indexing) for each test case. The function continues to process test cases until all input has been consumed, at which point it terminates.

