#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9) representing the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price, respectively.
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
        
    #State: `t` is 0, stdin is empty, `x` is a list of three integers (the last input), `n` is an integer, `a` is an integer, `b` is an integer.

#Overall this is what the function does:Calculates and prints the total profit from selling buns at modified prices for multiple test cases. For each test case, it takes the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price as input, and prints the total profit. If the usual price is greater than or equal to the modified price, it simply prints the total profit without any modifications. Otherwise, it calculates the additional profit by selling the first 'k' buns at the modified price, where 'k' is the minimum of the difference between the modified and usual prices and the number of buns minus one, and prints the updated total profit.

