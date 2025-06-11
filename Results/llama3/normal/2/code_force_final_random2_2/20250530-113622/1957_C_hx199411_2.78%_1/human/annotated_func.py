#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n and an integer k on the first line, followed by k lines, each containing two integers r_i and c_i. 1 <= n <= 3 * 10^5, 0 <= k <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: t is 0, n is an integer, i is equal to m, m is an integer equal to n minus k or n minus 2 times k, c is an integer, r is an integer, num is either k or 2 times k, stdin contains no more test cases. If m is 0, the value 0 is being printed. If m is 1, the number 1 is being printed. Otherwise, dp is a list of m+1 elements where dp[1] is 1, dp[2] is 3, and for all i from 3 to m, dp[i] is (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10^9 + 7).

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n and an integer k, followed by k lines with two integers each. It calculates the number of ways to arrange the integers in a specific pattern, based on the values of n and k. If the calculated value m is 0, it prints 0. If m is 1, it prints 1. Otherwise, it uses dynamic programming to calculate the number of ways to arrange the integers and prints the result modulo 10^9 + 7. The function continues this process until all test cases have been read from standard input.

