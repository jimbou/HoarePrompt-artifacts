#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers n (1 <= n <= 50).
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
        
    #State: `s` is a string of all uppercase English letters, `t` is 0, `i` is equal to the initial value of `t`. For each even integer `n` read from stdin, a string consisting of the first `n/2` characters of `s` repeated twice is printed, preceded by 'YES'. For each odd integer `n` read from stdin, 'NO' is printed. If `t` is 0, no integers are read from stdin and no output is printed.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers to read. For each subsequent integer n, if n is even, the function prints 'YES' followed by a string consisting of the first n/2 uppercase English letters repeated twice. If n is odd, the function prints 'NO'. If t is 0, the function does not read any integers and does not produce any output.

