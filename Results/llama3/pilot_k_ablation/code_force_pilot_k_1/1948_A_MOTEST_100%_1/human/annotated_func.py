#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers (1 <= n <= 50).
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
        
    #State: `s` is the string of all uppercase English letters, `t` is an integer between 1 and 50 inclusive, `i` is `t`, the console screen has been cleared, stdin is empty. For each integer `n` in the input, if `n` is an odd integer, 'NO' is printed. If `n` is an even integer, 'YES' is printed, and the string consisting of the first `n//2` characters of `s` repeated twice is printed.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer represents the number of subsequent integers to process. For each subsequent integer, if it is even, the function prints 'YES' followed by a string consisting of the first half of the uppercase English alphabet repeated twice. If the integer is odd, the function prints 'NO'. The function clears the console screen before processing the input and empties the standard input buffer after processing.

