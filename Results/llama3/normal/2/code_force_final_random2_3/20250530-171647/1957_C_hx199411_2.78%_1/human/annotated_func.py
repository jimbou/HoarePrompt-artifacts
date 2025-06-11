#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n and an integer k on the first line, and k pairs of integers on the following k lines. n is a positive integer and k is a non-negative integer less than or equal to n.
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
            print(0)
        elif m == 1:
            print(1)
        else:
            dp = [(0) for i in range(m + 1)]
            dp[1] = 1
            dp[2] = 3
            for i in range(3, m + 1):
                dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10 ** 9 + 7)
            print(dp[m])
        
    #State: `t` is 0, `n` is an integer, `k` is a non-negative integer, `num` is an integer, `i` is equal to `k` if `m` is 0 or 1, otherwise `i` is equal to `m`, `m` is an integer equal to `n - num`, stdin is empty. If `m` is 0, the value 0 is being printed. If `m` is 1, the number 1 is being printed. If `m` is not 0 or 1, `dp` is a list of `m` + 1 elements initialized with 0, except `dp[1]` is 1, `dp[2]` is 3, and for all integers `j` from 3 to `m`, `dp[j]` is (`dp[j - 1]` + (`j` - 1) * `dp[j - 2]` * 2) % (10^9 + 7).

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a positive integer n and a non-negative integer k, followed by k pairs of integers. It calculates the number of remaining elements (m) after processing the pairs, and then prints the result based on the value of m. If m is 0, it prints 0. If m is 1, it prints 1. If m is greater than 1, it calculates and prints the m-th element of a dynamic programming sequence (dp) modulo 10^9 + 7, where dp[i] = (dp[i-1] + (i-1) * dp[i-2] * 2) % (10^9 + 7) for i >= 3. The function continues this process until all test cases have been read from standard input.

