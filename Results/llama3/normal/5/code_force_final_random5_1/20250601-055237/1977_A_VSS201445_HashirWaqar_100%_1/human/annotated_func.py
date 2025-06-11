#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: `n` and `m` are integers greater than 0, `_` is `t`, stdin contains at least one integer `t` that is greater than 0. If `n` is greater than or equal to `m` and the difference between `n` and `m` is even, 'YES' is being printed. Otherwise, 'NO' is being printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers `n` and `m`. It then checks if `n` is greater than or equal to `m` and if the difference between `n` and `m` is even. If both conditions are met, it prints 'YES', otherwise it prints 'NO'. The function repeats this process for a number of test cases specified by the first integer `t` read from standard input.

