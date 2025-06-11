#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9) — the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price.
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: The total cost of buns for each test case, considering the modified price for the first k buns and the usual price for the remaining buns.

#Overall this is what the function does:Calculates and prints the total cost of buns for each test case, considering a modified price for the first k buns and the usual price for the remaining buns, where k is the minimum of the number of buns and the difference between the modified and usual prices.

