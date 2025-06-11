#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 50 inclusive) and then a series of integers (between 1 and 50 inclusive).
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
        
    #State: `t` is an integer that is at least 1, `s` is a string of all uppercase English letters, `i` is `t`, stdin contains no input. If `n` is odd, 'NO' is printed. If `n` is even, 'YES' is printed, and a string `ans` is printed, which consists of the first `n // 2` characters of `s`, each repeated twice.

#Overall this is what the function does:The function reads an integer `t` and then `t` number of integers from standard input. For each integer `n`, if `n` is odd, it prints 'NO'. If `n` is even, it prints 'YES' and a string consisting of the first `n // 2` uppercase English letters, each repeated twice. The function consumes all input from standard input and leaves it empty.

