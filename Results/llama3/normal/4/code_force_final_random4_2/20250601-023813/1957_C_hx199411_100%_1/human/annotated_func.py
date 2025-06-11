#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k (1 <= n <= 3 * 10^5, 0 <= k <= n) on the first line, and k lines of two integers r_i and c_i each.
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
        
    #State: t is 0, n is an integer, k is 0, num is either 1, 2, 3, 4, 5, or 6, i is equal to k if m is not 0, otherwise i is equal to m, c and r are assigned the values of the last two integers from the input, m is either n-1, n-2, n-3, n-4, n-5, or n-6, and stdin contains multiple test cases minus k+1. If m is 0, the number 1 is being printed. If m is 1, the number 1 is being printed. Otherwise, dp is a list of m+1 elements with dp[1] equal to 1, dp[2] equal to 3, and dp[i] equal to (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10^9 + 7).

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and k, followed by k lines of two integers each. It calculates the number of ways to arrange the integers in a specific pattern, depending on the values of n and k. If m (n minus the number of pairs with equal integers) is 0 or 1, it prints 1. Otherwise, it uses dynamic programming to calculate the number of ways to arrange the integers and prints the result. The function continues this process until all test cases have been processed.

