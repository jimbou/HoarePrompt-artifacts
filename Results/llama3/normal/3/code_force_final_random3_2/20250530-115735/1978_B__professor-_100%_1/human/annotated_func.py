#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three space-separated integers: n, a, and b (1 <= n, a, b <= 10^9).
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n // 2))
        else:
            print(int((b - a) * (b - a + 1) // 2 + a * n))
        
    #State: `t` is 0, `n`, `a`, and `b` are integers, `_` is `t`, and stdin contains no more test cases.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of three integers: n, a, and b. It then calculates and prints the result for each test case based on the values of a and b relative to n. The function handles three scenarios: (1) b is less than or equal to a, (2) b minus a is greater than or equal to n, and (3) b minus a is less than n. After processing all test cases, the function leaves the input stream empty.

