#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 10^3). Each of the following t lines contains two integers n and k (1 ≤ n ≤ 100, 0 ≤ k ≤ n*(n-1)/2).
    qs = int(input())
    for _ in range(qs):
        n, k = [int(num) for num in input().split()]
        
        reachable_count = n
        
        while k >= reachable_count - 1 and k > 0:
            k -= reachable_count - 1
            reachable_count -= 1
        
        print(reachable_count)
        
    #State: qs is 0, stdin is empty, n and k are the last two integers read from stdin, reachable_count is an integer between 1 and n, and _ is qs-1.

#Overall this is what the function does:This function reads a series of queries from standard input, where each query consists of two integers n and k. For each query, it calculates the largest integer reachable_count such that k is greater than or equal to the sum of reachable_count-1 and all previous reachable counts. The function then prints the calculated reachable_count for each query, effectively determining the maximum reachable count for each input pair (n, k).

