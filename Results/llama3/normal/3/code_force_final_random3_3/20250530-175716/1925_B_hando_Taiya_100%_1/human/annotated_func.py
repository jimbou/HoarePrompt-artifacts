#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: `x` is an integer between 1 and 10^8, `n` is an integer between 1 and `x`, `ans` is the maximum divisor of `x` that is less than or equal to `n`, `stdin` is empty.
    print(ans)
    #This is printed: the maximum divisor of x that is less than or equal to n (where x is an integer between 1 and 10^8, and n is an integer between 1 and x)

#Overall this is what the function does:The function reads an integer `x` and an integer `n` from standard input, where `x` is between 1 and 10^8 and `n` is between 1 and `x`. It then calculates and prints the maximum divisor of `x` that is less than or equal to `n`.

