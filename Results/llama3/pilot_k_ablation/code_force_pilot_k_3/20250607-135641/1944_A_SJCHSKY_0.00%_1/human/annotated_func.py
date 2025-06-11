#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: two integers n and k, where n is a positive integer less than or equal to 100 and k is a non-negative integer less than or equal to n*(n-1)/2.
    qs = int(input())
    for _ in range(qs):
        n, k = [int(num) for num in input().split()]
        
        reachable_count = n
        
        while k >= reachable_count - 1 and k > 0:
            k -= reachable_count - 1
            reachable_count -= 1
        
        print(reachable_count)
        
    #State: qs is 0, n is a positive integer less than or equal to 100, k is a non-negative integer, reachable_count is a positive integer less than or equal to n and less than or equal to k + 1, _ is qs, stdin contains no test cases, and the value of reachable_count has been printed for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers, n and k. It then calculates the maximum reachable count for each test case by iteratively subtracting the current reachable count minus one from k until k is less than the reachable count minus one. The function prints the final reachable count for each test case. After processing all test cases, the function leaves the input stream empty.

