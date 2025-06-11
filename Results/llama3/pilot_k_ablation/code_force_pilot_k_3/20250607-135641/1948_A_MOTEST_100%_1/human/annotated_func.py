#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines each containing an integer n (1 <= n <= 50).
    os.system('cls')
    s = string.ascii_uppercase
    t = int(input())
    for i in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            ans, x = '', 0
            x = 0
            for j in range(n // 2):
                ans += s[x] * 2
                x += 1
            print('YES')
            print(ans)
        
    #State: `s` is the string of all uppercase ASCII letters, `t` is an integer between 1 and 50 inclusive, `n` is an integer between 1 and 50 inclusive, `i` is `t-1`, stdin is empty. If `n` is odd, 'NO' is being printed. If `n` is even, 'YES' is being printed, and the string `ans` consisting of the first `n/2` uppercase ASCII letters each repeated twice is being printed.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of test cases, and each subsequent integer n represents the size of a string to be generated. For each test case, if n is odd, the function prints 'NO'. If n is even, the function prints 'YES' followed by a string consisting of the first n/2 uppercase ASCII letters, each repeated twice. The function processes all test cases and empties the standard input.

