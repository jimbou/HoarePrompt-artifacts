#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9) — the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price.
    t = int(input())
    while t:
        x = list(map(int, input().split(' ')))
        
        n = x[0]
        
        a = x[1]
        
        b = x[2]
        
        profit = n * a
        
        if a >= b:
            print(profit)
        else:
            k = b - a
            k = min(n - 1, k)
            profit = profit + (b - a) * (k + 1) - k * (k + 1) / 2
            print(int(profit))
        
        t -= 1
        
    #State: t = 0

#Overall this is what the function does:Calculates and prints the maximum profit that can be achieved by selling buns at a modified price for the first bun, considering multiple test cases with different numbers of buns, usual prices, and modified prices.

