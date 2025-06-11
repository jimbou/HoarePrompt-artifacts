#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (2 <= n <= 10^5). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases t (1 <= t <= 500) is given at the beginning of the input.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        max = 0
        
        for i in range(1, n):
            if min(a[i], a[i - 1]) > max:
                max = min(a[i], a[i - 1])
        
        print(max)
        
    #State: The output state will contain t number of lines, each containing the maximum value of the minimum of adjacent pairs in the corresponding test case. The value of t remains unchanged, stdin is empty, and the values of n and a_i are also unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n space-separated integers. It then finds the maximum value of the minimum of adjacent pairs in each test case and prints this value. The function processes all test cases and leaves the input stream empty, without modifying the original input values.

