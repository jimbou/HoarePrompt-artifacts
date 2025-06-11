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
        
    #State: `t` is an integer greater than or equal to 0, `_` is equal to `t`, `n` is an integer from the last test case, `a` is an integer between 1 and 10^9 (inclusive) from the last test case, `b` is an integer between 1 and 10^9 (inclusive) from the last test case, stdin contains no test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains three integers n, a, and b. It then calculates and prints the result for each test case based on the values of a and b. If b is less than or equal to a, it prints n times a. If b minus a is greater than or equal to n, it prints the sum of an arithmetic series with n terms, starting from b and decreasing by 1. Otherwise, it prints the sum of an arithmetic series with b minus a plus 1 terms, starting from a and increasing by 1, plus a times n. After processing all test cases, the function leaves the standard input empty.

