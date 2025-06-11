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
        
    #State: The final output state is the number of ways to place the remaining m dominoes in the grid after considering the constraints imposed by the k pairs of integers r_i and c_i.

#Overall this is what the function does:This function calculates the number of ways to place dominoes in a grid after considering constraints imposed by given pairs of integers. It takes as input the number of test cases, followed by the size of the grid and the number of constraints for each test case. The function then outputs the number of ways to place the remaining dominoes in the grid for each test case, considering the constraints.

