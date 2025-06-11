#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^3) and then t pairs of integers n and k (1 <= k <= n <= 10^3).
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(1, n + 1) if k == 1 else [-1]
        
        print(*res)
        
    #State: t is an integer (1 <= t <= 10^3), n is an integer (1 <= n <= 10^3), k is an integer (1 <= k <= n), _ is t - 1, res is a list of integers, stdin contains 0 pairs of integers n and k (1 <= k <= n <= 10^3), and the list of integers in res is being printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers, n and k. For each test case, it generates a list of integers based on the values of n and k. If k is equal to n, the list contains all 1s. If k is 1, the list contains the numbers from 1 to n. Otherwise, the list contains a single -1. The function then prints the generated list for each test case.

