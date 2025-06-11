#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k (1 <= n <= 3 * 10^5, 0 <= k <= n) on the first line, and k lines of two integers r_i and c_i (1 <= r_i, c_i <= n) on the following lines.
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
        
    #State: The final output state is the number of ways to place dominoes on a grid of size n x n with k pairs of cells already occupied, modulo 10^9 + 7.

#Overall this is what the function does:Calculates the number of ways to place dominoes on an n x n grid with k pairs of cells already occupied, modulo 10^9 + 7, and prints the result for multiple test cases.

