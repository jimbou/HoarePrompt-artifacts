#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k such that 1 <= n <= 100 and 0 <= k <= n * (n - 1) / 2.
    qs = int(input())
    for _ in range(qs):
        n, k = [int(num) for num in input().split()]
        
        reachable_count = n
        
        while k >= reachable_count - 1 and k > 0:
            k -= reachable_count - 1
            reachable_count -= 1
        
        print(reachable_count)
        
    #State: Output State: The number of reachable nodes after all the iterations of the loop have finished is printed to the console for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers n and k. It then calculates and prints the number of reachable nodes after a series of iterations, where in each iteration, the number of reachable nodes is decremented by 1 and k is reduced by the current number of reachable nodes minus 1, until k is less than the number of reachable nodes minus 1 or k becomes 0. The function repeats this process for each test case and outputs the final number of reachable nodes for each case.

