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
        
    #State: `s` is the string of all uppercase ASCII letters, `t` is 0, `i` is `t`, stdin is empty. If any `n` is 1, 'NO' is printed. If all `n` are at least 2, 'YES' is printed for each `n`, and the string `ans` is printed for each `n`, which is 'AAABBBBCD...Z' if `n` is odd otherwise it is the first `n//2` letters of `s` repeated twice if `n` is even.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers n. For each n, if n is 1, it prints 'NO'. If n is at least 2, it prints 'YES' followed by a string of uppercase ASCII letters. The string is constructed by repeating the first n//2 letters of the alphabet twice if n is even, or by starting with 'AAA' and then repeating the next n//2 - 1 letters of the alphabet twice if n is odd. After processing all integers, the function leaves the standard input empty and the string of all uppercase ASCII letters unchanged.

