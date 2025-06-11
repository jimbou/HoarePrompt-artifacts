#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: `t` is 0, `_` is `t`, `n`, `a`, and `b` are undefined, stdin contains no input.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers n, a, and b. It then calculates and prints the result for each test case based on the values of a and b relative to n. The function handles three scenarios: when b is less than or equal to a, when b minus a is greater than or equal to n, and when b minus a is less than n. After processing all test cases, the function leaves the input stream empty and the variables t, _, n, a, and b undefined.

