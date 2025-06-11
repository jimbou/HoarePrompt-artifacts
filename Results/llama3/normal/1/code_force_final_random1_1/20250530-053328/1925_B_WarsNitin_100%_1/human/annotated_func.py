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
        
    #State: `q` is `t-1`, `i` is `sqrt(x)`, `sqrt(x)` is an integer greater than or equal to 1, `x` is greater than or equal to 0, stdin is empty, `ans` is the maximum of 1 and the largest divisor of `x` that satisfies the conditions: (`x` - `n` * `i` >= 0 and (`x` - `n` * `i`) % `i` == 0) or (`x` - `n` * (`x` // `i`) >= 0 and (`x` - `n` * (`x` // `i`)) % (`x` // `i`) == 0), and the value of `ans` is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers x and n. It then finds the largest divisor of x that satisfies certain conditions based on x and n, and prints the maximum of 1 and this largest divisor. The function repeats this process for each test case, until all test cases have been processed and standard input is empty.

