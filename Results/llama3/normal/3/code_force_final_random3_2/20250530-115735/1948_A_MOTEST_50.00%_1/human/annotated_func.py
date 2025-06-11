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
        
    #State: `s` is the string of all uppercase English letters, `t` is an integer and is at least 1, `i` is `t`, stdin is empty. If `n` is 1, 'NO' is printed. If `n` is even, 'YES' is printed, `x` is `n//2`, `j` is `n//2 - 1`, and `ans` is a string consisting of two occurrences of each uppercase English letter from 'A' to the (`n//2`)th uppercase English letter. If `n` is odd, 'YES' is printed, `x` is `n // 2`, `j` is `n // 2 - 1`, and `ans` is 'AAA' followed by 2 * (`n // 2 - 1`) uppercase English letters, and `ans` is printed.

#Overall this is what the function does:This function reads a series of integers from standard input, generates and prints a specific string pattern for each integer, and handles cases for both even and odd integers. It takes no parameters and returns no value, but instead prints the results directly to the console. For each input integer n, if n is 1, it prints 'NO'. If n is even, it prints 'YES' followed by a string consisting of two occurrences of each uppercase English letter from 'A' to the (n//2)th uppercase English letter. If n is odd, it prints 'YES' followed by 'AAA' and then 2 * (n // 2 - 1) uppercase English letters. The function continues this process until all input integers have been processed, at which point the standard input is empty.

