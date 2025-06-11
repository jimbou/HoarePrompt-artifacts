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
        
    #State: The output state is a list of integers, each representing the total cost of buns for a test case. The total cost is calculated based on the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price.

#Overall this is what the function does:Calculates and prints the total cost of buns for multiple test cases, considering the number of buns, usual price, and modified price of the first bun, and outputs the total cost for each test case.

