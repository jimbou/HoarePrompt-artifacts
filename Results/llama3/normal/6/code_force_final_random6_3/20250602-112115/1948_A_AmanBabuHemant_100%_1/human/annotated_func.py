#State of the program right berfore the function call: stdin contains two inputs: first an integer (greater than 0 and less or equal than 50) and then a series of integers (greater or equal than 1 and less or equal than 50).
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
        
    #State: `t` is an integer equal to 0, `n` is an integer greater or equal than 1 and less or equal than 50, stdin contains no input. If `n` is odd, 'NO' is printed. If `n` is even, a string `s` of 'AAB' repeated `n // 2` times is created. If the length of `s` is less than 200, 'YES' is printed and the string `s` is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n. For each test case, if n is odd, it prints 'NO'. If n is even, it creates a string s by repeating 'AAB' n/2 times and checks if the length of s is less than 200. If the length of s is less than 200, it prints 'YES' followed by the string s. Otherwise, it prints 'NO'. The function processes all test cases and then terminates, leaving the standard input empty.

