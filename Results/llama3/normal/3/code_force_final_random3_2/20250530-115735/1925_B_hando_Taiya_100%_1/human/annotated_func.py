#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: `stdin` contains `t-1` lines, each containing two integers `x` (1 <= `x` <= 10^8) and `n` (1 <= `n` <= `x`), `x` is an integer between 1 and 10^8, `n` is an integer between 1 and `x`, `x` must be greater than 0, `i` is `isqrt(x) + 1`. `ans` is the maximum divisor of `x` that is less than or equal to `n`.
    print(ans)
    #This is printed: the maximum divisor of x that is less than or equal to n

#Overall this is what the function does:This function reads an integer t from standard input, followed by t lines, each containing two integers x and n. It then calculates and prints the maximum divisor of x that is less than or equal to n for each pair of x and n.

