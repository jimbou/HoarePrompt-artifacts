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
        
    #State: `t` is 0, stdin is empty, `n`, `a`, and `b` are the last set of integers read from stdin, the profit for each test case has been printed to the console

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing three integers representing the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price. It calculates the total profit for each test case, taking into account the possibility of selling the first bun at a modified price, and prints the profit for each test case to the console. The function continues to process test cases until all input has been read, at which point it concludes, leaving the input stream empty and the last set of integers read from the input as the values of `n`, `a`, and `b`.

