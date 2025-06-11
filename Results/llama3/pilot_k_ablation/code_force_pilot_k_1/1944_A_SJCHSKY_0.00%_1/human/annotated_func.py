#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k such that 1 <= n <= 100 and 0 <= k <= n * (n - 1) / 2.
    qs = int(input())
    for _ in range(qs):
        n, k = [int(num) for num in input().split()]
        
        reachable_count = n
        
        while k >= reachable_count - 1 and k > 0:
            k -= reachable_count - 1
            reachable_count -= 1
        
        print(reachable_count)
        
    #State: `qs` is 0, `n` is an integer, `k` is an integer, `reachable_count` is not defined, and `qs` number of values have been printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers n and k. It then calculates and prints the maximum number of nodes that can be reached in a graph with n nodes and k edges, for each test case. The function continues this process until all test cases have been processed, at which point it terminates, having printed the results for all test cases.

