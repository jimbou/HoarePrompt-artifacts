#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: t is an integer greater than or equal to 0, i is t-1, n is an integer, k is an integer, l is a list of integers, stdin is empty, and k-1 is printed t times.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. The function then prints k-1 for each test case, without modifying the input values. The function's purpose is to output a sequence of k-1 values, one for each test case, based on the input provided.

