#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5 * 10^4) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^9).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
            L.append(m)
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * (k - tot) - 1))
            tot += a
            pow *= 2
        
    #State: The output state will contain `t` lines, each containing a single integer. Each integer represents the result of the calculation `pow * (2 * (k - tot) - 1)` for the corresponding input values of `n` and `k`. The value of `t` remains unchanged.

#Overall this is what the function does:The function reads a series of input values from stdin, where the first value t represents the number of test cases, and each subsequent pair of values n and k represents a test case. For each test case, the function calculates a result based on the values of n and k, and prints the result to the output. The function processes all t test cases and produces t output values, each representing the calculated result for the corresponding input values of n and k.

