#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n < m:
            print('NO')
        elif n & 1 and m & 1 or n % 2 == 0 and m % 2 == 0:
            print('YES')
        
    #State: `n` and `m` are integers between 1 and 100, `stdin` contains 0 lines, each containing two integers `n` and `m` (1 <= `n`, `m` <= 100), and `t` is 0. If `n` is less than `m`, 'NO' is printed. Otherwise, if both `n` and `m` are odd or both are even, 'YES' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and m. It then checks each test case and prints 'YES' if n and m have the same parity (both odd or both even) and n is not less than m, otherwise it prints 'NO'. The function continues this process until all test cases have been read from standard input, at which point the input is exhausted.

