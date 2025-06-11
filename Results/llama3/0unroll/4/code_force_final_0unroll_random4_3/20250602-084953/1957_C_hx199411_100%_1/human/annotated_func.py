#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two integers n and k, followed by k lines each containing two integers r_i and c_i. n is a positive integer, k is a non-negative integer less than or equal to n, and r_i and c_i are non-negative integers less than n.
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
        
    #State: t = 0, n = 0, k = 0, num = 0, m = 0, dp = [0], c = 0, r = 0, i = 0

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the result for each case. It calculates the number of ways to arrange a set of non-overlapping rectangles of size 1x2 within a grid of size n x n, where some cells are already occupied. The function takes no parameters and returns no value, but instead prints the result for each test case. The final state of the program is that all input has been processed, and the results have been printed to stdout.

