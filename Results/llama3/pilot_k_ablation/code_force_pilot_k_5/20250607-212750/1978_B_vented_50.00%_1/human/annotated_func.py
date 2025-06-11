#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains three space-separated integers n, a, and b (1 <= n, a, b <= 10^9) representing the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price, respectively.
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
        
    #State: t is 0, stdin is empty, x is a list of three integers, n is an integer between 1 and 10^9, a is an integer between 1 and 10^9, b is an integer between 1 and 10^9, and the integer value of profit is being printed. If a is greater than or equal to b, the profit which is equal to n * a is being printed. Otherwise, the profit which is equal to n * a + (b - a) * (min(n - 1, b - a) + 1) - min(n - 1, b - a) * (min(n - 1, b - a) + 1) / 2 is being printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases (t) and each subsequent line contains three integers (n, a, b) representing the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price, respectively. It then calculates the profit for each test case based on the given prices and prints the result. If the usual price (a) is greater than or equal to the modified price (b), the profit is simply the product of the number of buns (n) and the usual price (a). Otherwise, the profit is calculated using the formula: n * a + (b - a) * (min(n - 1, b - a) + 1) - min(n - 1, b - a) * (min(n - 1, b - a) + 1) / 2. The function continues to process test cases until all input has been read (i.e., t becomes 0).

