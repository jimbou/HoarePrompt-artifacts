#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: The output will contain t lines, each containing a list of integers. If k equals n, the list will contain n ones. If k equals 1, the list will contain integers from 0 to n-1. Otherwise, the list will contain a single -1.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of two integers n and k. It then generates and prints a list of integers based on the values of n and k. If k equals n, the list contains n ones. If k equals 1, the list contains integers from 0 to n-1. For all other cases, the list contains a single -1. The function processes multiple test cases and prints the corresponding lists for each case.

