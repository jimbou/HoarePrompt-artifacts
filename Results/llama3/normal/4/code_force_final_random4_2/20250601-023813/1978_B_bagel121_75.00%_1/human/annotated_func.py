#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9) — the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price.
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if a >= b:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            ans = int((b + (b - k + 1)) / 2 * k)
            p2 = (n - k) * a
            print(ans + p2)
        
    #State: `t` is an integer greater than or equal to 0, `_` is equal to `t`, `n`, `a`, and `b` are integers assigned from the input, stdin is empty. If `a` is greater than or equal to `b`, the product of `n` and `a` is printed. Otherwise, `k` is an integer equal to the minimum of `b - a + 1` and `n`, `ans` is an integer equal to the sum of the integers from `b - k + 1` to `b`, `p2` is an integer equal to the product of `n - k` and `a`, and the sum of `ans` and `p2` is printed.

#Overall this is what the function does:Calculates and prints the total cost of selling a certain number of buns at either their usual price or a modified price, depending on the relationship between the usual and modified prices, for multiple test cases.

