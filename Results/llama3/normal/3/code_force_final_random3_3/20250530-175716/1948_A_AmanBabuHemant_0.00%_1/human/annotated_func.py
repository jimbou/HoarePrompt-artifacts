#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines, each containing an integer n (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = '110' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: _ is t-1, `t` is an integer between 1 and 50 inclusive, `n` is an integer between 1 and 50 inclusive, stdin contains 0 lines. If `n` is odd, 'NO' is printed. If `n` is even, a string `s` of '110' repeated `n // 2` times is created. If the length of `s` is less than 200, 'YES' is printed and the string `s` is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers. For each subsequent integer n, the function checks if n is even or odd. If n is odd, it prints 'NO'. If n is even, it generates a string s consisting of '110' repeated n // 2 times and checks its length. If the length of s is less than 200, it prints 'YES' followed by the string s. Otherwise, it prints 'NO'. The function processes all t integers and then terminates, leaving the standard input empty.

