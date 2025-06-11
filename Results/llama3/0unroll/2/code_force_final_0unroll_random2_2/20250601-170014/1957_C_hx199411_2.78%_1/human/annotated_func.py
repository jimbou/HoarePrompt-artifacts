#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two integers n and k (1 <= n <= 3 * 10^5, 0 <= k <= n) and k pairs of integers r_i and c_i (1 <= r_i, c_i <= n) such that no two pairs have the same row or column and no pair has r_i = c_i.
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
        
    #State: The output state after the loop executes all the iterations is the final state of the variables t, n, k, num, m, and dp.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints output to standard output. It accepts no parameters and returns no values. The function reads a number of test cases, and for each test case, it reads two integers n and k, followed by k pairs of integers. It then calculates the value of m based on the input and prints a value based on the value of m. If m is 0, it prints 0. If m is 1, it prints 1. If m is greater than 1, it calculates a value using dynamic programming and prints the result modulo 10^9 + 7. The function repeats this process for each test case.

