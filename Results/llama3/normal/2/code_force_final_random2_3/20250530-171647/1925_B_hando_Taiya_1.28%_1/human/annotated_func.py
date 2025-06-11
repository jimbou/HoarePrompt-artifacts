#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: `stdin` contains t-1 lines, each containing two integers `x` (1 <= `x` <= 10^8) and `n` (1 <= `n` <= `x`), `x` is an integer greater than or equal to 1, `n` is an integer between 1 and `x`, `ans` is the maximum divisor of `x` that is less than or equal to `n`, `i` is the integer square root of `x` plus 1.
    print(ans)
    #This is printed: the maximum divisor of x that is less than or equal to n

#Overall this is what the function does:The function reads an integer t from stdin, representing the number of test cases. For each test case, it reads two integers x and n, where x is a number and n is a threshold. It then finds the maximum divisor of x that is less than or equal to n and prints this value. The function repeats this process t times, consuming all input lines from stdin.

