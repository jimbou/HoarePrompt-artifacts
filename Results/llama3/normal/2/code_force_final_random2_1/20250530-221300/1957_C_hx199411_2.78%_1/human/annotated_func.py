#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and k (1 <= n <= 3 * 10^5, 0 <= k <= n) followed by k pairs of integers r_i and c_i (1 <= r_i, c_i <= n).
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
        
    #State: t is 0, n is an integer between 1 and 3 * 10^5, k is 0, m is an integer between -2*3*10^5 and 3*10^5, i is -1 if m is not 0 and 1 otherwise, c is an integer, r is an integer, and stdin contains no test cases. The current value of num is equal to the sum of the number of times c is not equal to r plus twice the number of times c is equal to r. If m is 0, 0 is printed. If m is 1, 1 is printed. If m is not 0 and not 1, dp is a list of m+1 integers with dp[1] equal to 1, dp[2] equal to 3, and dp[i] equal to (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10^4), and dp[m] is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the result for each case. It calculates the number of pairs of integers (r, c) where r is not equal to c, and then uses dynamic programming to calculate the number of ways to arrange these pairs in a specific order. The function prints the result for each test case, which can be 0, 1, or a calculated value based on the dynamic programming algorithm.

