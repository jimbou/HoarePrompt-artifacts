#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: t is an integer between 1 and 500 (inclusive), i is t-1, n is an integer, k is an integer, l is a list of integers, stdin is empty, and the value of k-1 has been printed t times.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers (n and k) followed by a list of n integers. It then prints the value of k-1 for each test case, without modifying the input values. The function processes a variable number of test cases (between 1 and 500), and its output consists of the repeated values of k-1, one for each test case.

