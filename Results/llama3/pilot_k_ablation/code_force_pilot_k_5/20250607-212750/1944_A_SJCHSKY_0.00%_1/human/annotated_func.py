#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k such that 1 <= n <= 100 and 0 <= k <= n * (n - 1) / 2.
    qs = int(input())
    for _ in range(qs):
        n, k = [int(num) for num in input().split()]
        
        reachable_count = n
        
        while k >= reachable_count - 1 and k > 0:
            k -= reachable_count - 1
            reachable_count -= 1
        
        print(reachable_count)
        
    #State: qs is 0, n is an integer, k is an integer greater than or equal to 0, reachable_count is less than or equal to k, _ is qs, stdin contains no test cases, and the reachable_count which is less than or equal to k is being printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains two integers n and k. It then iteratively calculates the maximum reachable count by subtracting the current reachable count minus one from k, until k is less than the reachable count minus one or k becomes zero. Finally, it prints the calculated reachable count for each test case.

