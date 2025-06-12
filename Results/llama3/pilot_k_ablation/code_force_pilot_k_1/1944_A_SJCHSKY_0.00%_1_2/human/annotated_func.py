#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n * (n - 1) / 2).
    qs = int(input())
    for _ in range(qs):
        n, k = [int(num) for num in input().split()]
        
        reachable_count = n
        
        while k >= reachable_count - 1 and k > 0:
            k -= reachable_count - 1
            reachable_count -= 1
        
        print(reachable_count)
        
    #State: qs is an integer between 1 and 10^3 (inclusive), stdin is empty, _ is qs, n is an integer between 1 and 100 (inclusive), k is the remainder of the initial value of k divided by the initial value of reachable_count minus 1 plus 1, reachable_count is 1, and qs values have been printed.

#Overall this is what the function does:Reads a series of test cases from standard input, where each case consists of two integers n and k, and prints the minimum number of nodes that can be reached in a graph with n nodes and k edges, repeating this process for a specified number of test cases.

