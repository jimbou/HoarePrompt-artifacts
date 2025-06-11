#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two integers n and k (1 <= n <= 3 * 10^5, 0 <= k <= n) on the first line, and k lines of two integers r_i and c_i (1 <= r_i, c_i <= n) on the following lines.
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
        
    #State: t is 0, n is an integer between 1 and 3 * 10^5 inclusive, k is 0, i is equal to the original value of k, num is an integer between 0 and 2 * (the original value of k), c and r are integers, and stdin contains no test cases. If m is 0, the number 1 is being printed. If m is 1, the number 1 is being printed. If m is greater than 1, dp is a list of m+1 elements with dp[1] equal to 1, dp[2] equal to 3, and dp[i] equal to (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10^9 + 7) for all i from 3 to m inclusive, and the value of dp[m] is being printed which is equal to (dp[m - 1] + (m - 1) * dp[m - 2] * 2) % (10^9 + 7).

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and k, followed by k lines of two integers r_i and c_i. It then calculates the number of ways to place dominoes on an n x n grid such that no two dominoes overlap, given that k dominoes are already placed at positions (r_i, c_i). The function prints the result for each test case. If there are no available positions for dominoes (m = 0), it prints 1. If there is only one available position (m = 1), it also prints 1. Otherwise, it calculates the result using dynamic programming and prints the result modulo 10^9 + 7.

