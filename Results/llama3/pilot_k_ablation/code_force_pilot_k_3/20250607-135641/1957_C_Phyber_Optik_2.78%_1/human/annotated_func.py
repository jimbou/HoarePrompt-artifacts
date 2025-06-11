#State of the program right berfore the function call: n is a non-negative integer.
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
        
    #State: dp is a list with dp[1] equal to 1, dp[2] equal to 3, dp[3] equal to 7, dp[4] equal to 15, dp[5] equal to 31, and dp[n] equal to some value, n is greater than or equal to n, i is n + 1

#Overall this is what the function does:Calculates the nth term of a sequence where each term is the sum of the previous term and twice the product of the current index and the term two positions before, modulo 1000000007, and stores the result in the nth index of the dp list.

