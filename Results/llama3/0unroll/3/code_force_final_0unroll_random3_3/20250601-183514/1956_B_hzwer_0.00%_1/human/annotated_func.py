#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5) — the number of cards you and Nene receive in the beginning of the game. The second line contains n integers a_1, a_2, …, a_n (1 <= a_i <= n) — the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the sequence a_1, a_2, …, a_n at most 2 times.
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
        
    #State: dp is a 2D list of size (n + 1) x (n + 1) where dp[i][j] represents the maximum number of pairs that can be formed using the first i cards and j pairs, considering the constraints that each card can be used at most once and each pair must have a unique card.
    return dp[0][0]
    #The program returns the maximum number of pairs that can be formed using 0 cards and 0 pairs, considering the constraints that each card can be used at most once and each pair must have a unique card.

#Overall this is what the function does:This function determines the maximum number of pairs that can be formed from a given set of cards, with each card used at most once and each pair having a unique card. It takes no parameters and returns the maximum number of pairs that can be formed. The function assumes that the input is provided through standard input, where the first line contains the number of test cases, and each test case consists of two lines: the first line contains the number of cards, and the second line contains the integers on the cards. The function processes each test case and returns the maximum number of pairs that can be formed for each case.

