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
        
    #State: `t` is 0, stdin contains no test cases, `x` is a list of three integers, `n` is an integer between 1 and 10^9, `a` is an integer between 1 and 10^9, `b` is an integer between 1 and 10^9. If `a` is greater than or equal to `b`, the profit which is equal to `n` times `a` is being printed. If `a` is less than `b`, the profit which is equal to `n` times `a` plus (`b` - `a`) times (`k` + 1) minus `k` times (`k` + 1) divided by 2, where `k` is the minimum of `n` - 1 and `b` - `a`, is being printed.

#Overall this is what the function does:Calculates and prints the maximum profit from selling buns at a modified price for multiple test cases. The function takes no parameters and returns no value, but it prints the profit for each test case. It reads input from stdin, processes each test case, and prints the result. The profit is calculated based on the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price. If the usual price is greater than or equal to the modified price, the profit is simply the number of buns times the usual price. If the usual price is less than the modified price, the profit is calculated by adding the difference between the modified price and the usual price times the minimum of the number of buns minus one and the difference between the modified price and the usual price, minus the sum of the first k natural numbers, where k is the minimum of the number of buns minus one and the difference between the modified price and the usual price.

