#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k > 1 else 1)
        
    #State: The loop has finished executing, and the final output state is the value of `n` if `n - k` is greater than 1, otherwise 1, for each pair of integers `n` and `k` in the input.

#Overall this is what the function does:The function reads a series of pairs of integers from standard input, where each pair represents the number of nodes (n) and the number of edges (k) in a graph. It then prints the minimum number of nodes that must be removed to make the graph a tree, which is either 1 (if the graph is already a tree or can be made into one by removing a single node) or the total number of nodes (n) if the graph has more edges than a tree with n nodes can have. The function processes multiple pairs of integers, one pair per line, and prints the result for each pair.

