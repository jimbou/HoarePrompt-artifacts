#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9) — the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price.
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: `t` is 0, `_` is `t`, `n` is an integer between 1 and 10^9, `a` is an integer between 1 and 10^9, `b` is an integer between 1 and 10^9, stdin contains no test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing three integers: the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price. It then calculates and prints the total price for each test case based on the given prices and the number of buns. The function handles three different scenarios: when the modified price is less than or equal to the usual price, when the difference between the modified and usual prices is greater than or equal to the number of buns, and when the difference is less than the number of buns. After processing all test cases, the function leaves the input stream empty.

