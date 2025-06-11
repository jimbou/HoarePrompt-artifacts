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
        
    #State: The output state will contain `t` lines, each containing a single integer. Each integer will be the result of the calculation `pow * (2 * (k - tot) - 1)` for the corresponding input values of `n` and `k`. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads a series of input lines from standard input, where the first line contains an integer t, representing the number of test cases, and each subsequent line contains two integers n and k. For each test case, it calculates a result based on the values of n and k, and prints the result to standard output. The function performs a total of t calculations and prints t results, one per test case.

