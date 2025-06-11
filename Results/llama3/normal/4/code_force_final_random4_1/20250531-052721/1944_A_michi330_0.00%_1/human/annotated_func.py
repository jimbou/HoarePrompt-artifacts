#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: `t` is an integer (1 <= t <= 10^3), stdin contains 0 lines, `i` is equal to `t`, `n` is an integer between 1 and 100 inclusive, `k` is an integer between 0 and n*(n-1)/2 inclusive, `n` is assigned the value of the first integer from the input, `k` is assigned the value of the second integer from the input. If `k` is greater than or equal to `n - 1`, the number 1 is printed. Otherwise, `n-1` is printed.

#Overall this is what the function does:Reads a series of test cases from standard input, where each case consists of two integers n and k, and prints the minimum number of operations required to make k connections between n nodes, which is either 1 if k is greater than or equal to n-1, or n-1 otherwise.

