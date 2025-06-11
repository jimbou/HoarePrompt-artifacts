#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 50) and then t integers (1 <= n <= 50).
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
        
    #State: `t` is an integer between 0 and 47 inclusive, `n` is an integer between 1 and 50 inclusive, `_` is t, stdin contains 0 integers (1 <= n <= 50). If `n` is odd, 'NO' is printed. If `n` is even, a string `s` of '110' repeated n//2 times is created. If the length of `s` is less than 200, 'YES' is printed and the string `s` is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer (t) represents the number of test cases, and each subsequent integer (n) represents the size of a string. For each test case, if n is odd, it prints 'NO'. If n is even, it creates a string of '110' repeated n//2 times and checks its length. If the length is less than 200, it prints 'YES' and the string; otherwise, it prints 'NO'.

