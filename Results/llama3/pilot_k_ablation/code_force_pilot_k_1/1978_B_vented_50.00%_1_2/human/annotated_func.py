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
        
    #State: `t` is 0, stdin is empty, `x`, `n`, `a`, `b`, and `profit` are undefined

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing three integers representing the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price. It calculates the total profit for each test case, considering the modified price for the first bun if it's lower than the usual price, and prints the calculated profit. The function continues this process until all test cases have been processed, leaving the input stream empty and the variables used within the function undefined.

