#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers n (1 <= n <= 50).
    os.system('cls')
    s = string.ascii_uppercase
    t = int(input())
    for i in range(t):
        n = int(input())
        
        if n == 1:
            print('NO')
        else:
            ans = ''
            x = 0
            if n % 2 == 0:
                for j in range(n // 2):
                    ans += s[x] * 2
                    x += 1
            else:
                ans, x = 'AAA', 1
                for j in range(n // 2 - 1):
                    ans += s[x] * 2
                    x += 1
            print('YES')
            print(ans)
        
    #State: `stdin` is empty, `s` is the string of all uppercase English letters, `t` is an integer between 1 and 50 inclusive, `i` is `t`. If `n` is 1, 'NO' is printed. If `n` is even and at least 52, 'YES' is being printed, and `ans` is the string of all uppercase English letters repeated twice. If `n` is odd and at least 51, 'YES' is being printed, and `ans` is 'AAA' followed by two 'B's, then two 'C's, then two 'D's, and so on until two 'Y's, and `ans` is being printed.

#Overall this is what the function does:The function reads a series of inputs from stdin, where the first input is an integer t (1 <= t <= 50) and the following t inputs are integers n (1 <= n <= 50). For each n, if n is 1, it prints 'NO'. If n is even, it prints 'YES' followed by a string of all uppercase English letters repeated twice. If n is odd, it prints 'YES' followed by a string starting with 'AAA' and then two consecutive uppercase English letters from 'B' to 'Y'. After processing all inputs, stdin is left empty.

