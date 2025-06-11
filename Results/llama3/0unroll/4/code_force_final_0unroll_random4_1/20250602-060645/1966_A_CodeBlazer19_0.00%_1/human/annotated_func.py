#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case contains two integers n and k (1 <= n <= 100, 2 <= k <= 100) followed by n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: The output state will contain `t` lines, each containing the value `k - 1`, where `k` is the second integer in each test case. The values of `t`, `n`, and `c_1, c_2, ..., c_n` remain unchanged.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of two integers (n and k) followed by n integers, and prints the value of k-1 for each test case, without modifying the input values.

