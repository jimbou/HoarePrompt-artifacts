#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    for q in range(int(input())):
        x, n = list(map(int, input().split(' ')))
        
        ans = 1
        
        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                if x - n * i >= 0 and (x - n * i) % i == 0:
                    ans = max(ans, i)
                if x - n * (x // i) >= 0 and x // i > 0 and x - n * (x // i) % (x // i
                    ) == 0:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State: `q` is `t-1`, `stdin` is empty, `x` and `n` are the last two integers read from `stdin`, `ans` is the maximum divisor of `x` that is less than or equal to the square root of `x` and satisfies the condition `x - n * i >= 0` and `(x - n * i) % i == 0`, and the maximum divisor of `x` that is less than or equal to the square root of `x` and satisfies the condition `x - n * i >= 0` and `(x - n * i) % i == 0` is being printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where each pair consists of a number x and a number n. For each pair, it finds the largest divisor of x that is less than or equal to the square root of x and satisfies the condition that x minus n times the divisor is non-negative and divisible by the divisor. It then prints this largest divisor for each pair. The function continues this process until all pairs have been read from standard input.

