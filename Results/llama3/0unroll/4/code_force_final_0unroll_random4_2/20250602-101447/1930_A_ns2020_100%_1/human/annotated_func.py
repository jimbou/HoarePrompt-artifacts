#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers a_1, a_2, ..., a_2n (1 <= a_i <= 10^7).
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: t = 0, n = last value, A = last value, stdin = empty

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It sorts the integers in ascending order, then prints the sum of the integers at even indices (0-based indexing). The function repeats this process for each test case until all input has been processed, leaving the input stream empty.

