#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n * (n - 1) / 2).
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: `t` is an integer (1 <= t <= 10^3), `n` is an integer (1 <= n <= 100), `k` is an integer (0 <= k <= n * (n - 1) / 2), `i` is `t-1`, stdin is empty. If `k` is greater than or equal to `n - 1`, the number 1 is printed. Otherwise, the value of `n`, which is an integer between 1 and 100 (inclusive), is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers: the number of nodes (n) and the number of edges (k) in a graph. It then prints the minimum number of nodes that need to be removed to make the graph a tree, which is 1 if the number of edges is greater than or equal to the number of nodes minus 1, and the number of nodes otherwise. The function processes all test cases and prints the result for each case.

