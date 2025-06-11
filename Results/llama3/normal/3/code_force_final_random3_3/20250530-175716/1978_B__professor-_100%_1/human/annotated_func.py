#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n // 2))
        else:
            print(int((b - a) * (b - a + 1) // 2 + a * n))
        
    #State: t is an integer equal to 0, `n`, `a`, and `b` are integers (1 <= n, a, b <= 10^9), stdin is empty. If `b` is less than or equal to `a`, the product of `n` and `a` is printed. If `b` is greater than `a`, then if `b - a` is greater than or equal to `n`, the integer value of the expression (2 * b - n + 1) * n // 2 is printed. Otherwise, the sum of the first n terms of an arithmetic sequence with first term a and common difference 1 is printed, where the sum is calculated as (b - a) * (b - a + 1) // 2 + a * n.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts no parameters and returns no value. It reads multiple lines of input, where the first line contains an integer t (1 <= t <= 10^4) and each subsequent line contains three integers n, a, and b (1 <= n, a, b <= 10^9). The function then prints the product of n and a if b is less than or equal to a, or the sum of an arithmetic sequence with first term a and common difference 1 if b is greater than a. The sum is calculated differently depending on whether b - a is greater than or equal to n. After processing all input lines, the function leaves stdin empty and the variables t, n, a, and b with values between 1 and 10^9.

