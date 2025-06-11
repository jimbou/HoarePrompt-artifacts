#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 50 inclusive) and then a series of integers (between 1 and 50 inclusive).
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
        
    #State: `t` is 0, `_` is `t`, `n` is an integer, and stdin is empty. If `n` is odd, 'NO' is printed. If `n` is even, a string `s` is created by repeating 'AAB' n//2 times. If the length of `s` is less than 200, 'YES' is printed and the string `s` is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n. For each test case, it checks if n is even. If n is odd, it prints 'NO'. If n is even, it generates a string s by repeating 'AAB' n//2 times and checks if the length of s is less than 200. If the length of s is less than 200, it prints 'YES' followed by the string s. Otherwise, it prints 'NO'. The function continues this process until all test cases have been processed, at which point standard input is empty.

