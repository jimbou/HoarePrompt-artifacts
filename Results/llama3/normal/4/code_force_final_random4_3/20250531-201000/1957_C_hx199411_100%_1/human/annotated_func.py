#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k (1 <= n <= 3 * 10^5, 0 <= k <= n) followed by k lines, each containing two integers r_i and c_i.
    t = int(input())
    while t:
        t -= 1
        
        n, k = list(map(int, input().split(' ')))
        
        num = 0
        
        for i in range(k):
            c, r = list(map(int, input().split(' ')))
            if c == r:
                num += 1
            else:
                num += 2
        
        m = n - num
        
        if m == 0:
            print(1)
        elif m == 1:
            print(1)
        else:
            dp = [(0) for i in range(m + 1)]
            dp[1] = 1
            dp[2] = 3
            for i in range(3, m + 1):
                dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10 ** 9 + 7)
            print(dp[m])
        
    #State: `t` is 0, `n` is an integer between 1 and 3 * 10^5 inclusive, `k` is an integer between 0 and `n` inclusive, `num` is an integer between `k` and 2*`k` inclusive, `i` is equal to `k` if `m` is 0 or 1, otherwise `i` is equal to `m+1`, `m` is an integer between `n - 2k` and `n - k` inclusive, stdin contains multiple test cases minus one, each test case contains 0 lines. If `m` is 0 or 1, the number 1 is being printed. Otherwise, a list `dp` of length `m+1` is created with `dp[1] = 1`, `dp[2] = 3`, and for all `i` from 3 to `m+1`, `dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10^9 + 7)`, and the `m`th element of the `dp` list, which is `dp[m]`, is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing two integers n and k, followed by k lines of two integers each. It calculates the number of ways to arrange the integers in a specific pattern, considering the values of n and k. If the calculated value m is 0 or 1, it prints 1. Otherwise, it uses dynamic programming to calculate the mth element of a list dp, which represents the number of ways to arrange the integers, and prints this value. The function continues this process until all test cases have been processed, at which point it terminates.

