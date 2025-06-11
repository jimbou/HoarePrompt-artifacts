#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: `t` is an integer (1 <= t <= 10^3), `i` is `t`, `n` is an integer (1 <= n <= 100), `k` is an integer (0 <= k <= n*(n-1)/2), stdin is empty. If `k` is greater than or equal to `n-1`, the number 1 is printed `t` times. Otherwise, the value of `n-1` is printed `t` times.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers, n and k. It then prints the minimum number of operations required to make all pairs of nodes in a graph of n nodes connected, given that k connections already exist. If k is greater than or equal to n-1, it prints 1, indicating that only one more connection is needed. Otherwise, it prints n-1, indicating that n-1 more connections are needed. The function repeats this process for each test case.

