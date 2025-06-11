#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines, each containing an integer n (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = 'AAB' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: `_` is equal to `t`, `n` is an integer between 1 and 50 (inclusive) and is equal to the integer on the last line of stdin, stdin is empty. If `n` is odd, 'NO' is printed. If `n` is even, a string `s` consisting of 'AAB' repeated n//2 times is created. If the length of `s` is less than 200, 'YES' is printed and the string `s` is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads a series of integers from standard input, determines whether each integer is even or odd, and prints 'YES' or 'NO' accordingly. For even integers, it generates a string consisting of 'AAB' repeated n//2 times and prints it if the string's length is less than 200. The function processes multiple test cases based on the initial input value t, and it consumes all input from stdin.

