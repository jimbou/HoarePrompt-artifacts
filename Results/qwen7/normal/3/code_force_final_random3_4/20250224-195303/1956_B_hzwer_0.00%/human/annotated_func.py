#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the list of integers a_1, a_2, ..., a_n represents the integers on the cards in your hand, where each integer from 1 through n appears at most twice; the sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
def func_1():
    n = int(input())
    cards = list(map(int, input().split()))
    dp = [([0] * (n + 1)) for _ in range(n + 1)]
    dp[n - 1][0] = 0
    dp[n - 2][0] = 0
    for i in range(n - 3, -1, -1):
        for j in range(n - 1, -1, -1):
            if cards.count(j + 1) == 0:
                dp[i][j] = dp[i + 1][j]
            elif cards.count(j + 1) == 1:
                dp[i][j] = max(dp[i + 1][j], dp[i + 2][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i + 2][j - 1] + 1, dp[i + 1][j + 1])
        
    #State: The final output state after the loop executes all its iterations will be such that `dp[i][0]` contains the maximum value obtainable for each `i` from `0` to `n-1`. This value represents the optimal solution for the problem defined by the loop, which involves making decisions based on the count of occurrences of each integer in the `cards` list. Specifically, `dp[i][0]` reflects the best outcome for the subproblems starting from index `i` down to `0`, considering the conditions provided within the loop.
    return dp[0][0]
    #The program returns the maximum value obtainable when starting from index 0 and considering the conditions provided within the loop.
#Overall this is what the function does:The function processes a list of integers representing cards in a hand, where each integer from 1 through n appears at most twice. It calculates and returns the maximum value obtainable by making decisions based on the count of occurrences of each integer in the list. Specifically, it uses dynamic programming to determine the best outcome for subproblems starting from index 0 down to 0, considering the constraints provided.

