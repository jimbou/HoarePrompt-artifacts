#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    for q in range(int(input())):
        x, n = list(map(int, input().split(' ')))
        
        ans = 1
        
        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                if x - n * i >= 0 and (x - n * i) % i == 0:
                    ans = max(ans, i)
                if x - n * (x // i) >= 0 and x // i > 0 and (x - n * (x // i)) % (x //
                    i) == 0:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State: `q` is `t-1`, `i` is `sqrt(x) + 1`, `ans` is the maximum divisor of `x` that is less than or equal to `sqrt(x)` and satisfies the conditions `x - n * i >= 0` and `(x - n * i) % i == 0` or `x - n * (x // i) >= 0` and `x // i > 0` and `(x - n * (x // i)) % (x // i) == 0`, and the maximum divisor `ans` is being printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers x and n. It then finds the maximum divisor of x that is less than or equal to the square root of x and satisfies certain conditions, and prints this maximum divisor for each test case.

