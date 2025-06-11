#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30) — the number of yogurts Maxim wants to buy, the price for one yogurt, and the price for two yogurts on promotion.
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X)
            print(X * C + B)
        
    #State: The total cost of yogurts for each test case, considering the optimal purchase strategy between buying individual yogurts and taking advantage of the two-yogurt promotion.

#Overall this is what the function does:Calculates and prints the minimum cost of buying a specified number of yogurts, considering the optimal purchase strategy between buying individual yogurts and taking advantage of a two-yogurt promotion, for multiple test cases.

