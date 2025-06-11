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
        
    #State: The output state is the number of ways to place a domino on a grid of size n x n, where n is the number of test cases, and k is the number of pairs of integers r_i and c_i. The output is calculated using dynamic programming and modular arithmetic.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the number of ways to place a domino on a grid of size n x n for each test case. It accepts no parameters and returns no value. The function iterates over multiple test cases, each consisting of an integer n and k pairs of integers, and calculates the result using dynamic programming and modular arithmetic. The output is printed to standard output.

