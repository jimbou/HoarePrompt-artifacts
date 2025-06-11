#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: The output will contain `t` lines, each containing a list of integers. For each line, if `k` equals `n`, the list will contain `n` ones. If `k` equals 1, the list will contain the numbers from 0 to `n-1`. Otherwise, the list will contain a single -1.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases. For each test case, it reads two integers n and k, and then prints a list of integers based on the values of n and k. If k equals n, the list contains n ones. If k equals 1, the list contains the numbers from 0 to n-1. Otherwise, the list contains a single -1. The function repeats this process t times, producing t lines of output.

