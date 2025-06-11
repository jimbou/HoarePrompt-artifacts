#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two integers n and k, followed by k lines each containing two integers r_i and c_i. 1 <= t <= 10^4, 1 <= n <= 3 * 10^5, 0 <= k <= n.
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
        
    #State: The output state is the number of ways to fill the remaining m cells in the grid with 1s and 0s such that no two adjacent cells have the same value.

#Overall this is what the function does:This function calculates and prints the number of ways to fill the remaining cells in a grid with 1s and 0s such that no two adjacent cells have the same value, after considering a set of predefined cell positions that must be filled in a specific manner. The function accepts a series of test cases as input, where each test case specifies the grid size, the number of predefined cell positions, and the coordinates of these positions. The function processes each test case, calculates the number of remaining cells, and then uses dynamic programming to compute the number of valid fillings for the remaining cells. The result is printed for each test case.

