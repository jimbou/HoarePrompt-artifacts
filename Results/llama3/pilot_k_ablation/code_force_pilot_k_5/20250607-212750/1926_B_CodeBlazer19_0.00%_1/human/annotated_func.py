#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines each containing n characters '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = 0
        
        b = ''
        
        for j in range(n):
            s = input()
            if s.count('1') == 1:
                a = 'Triangle'
            elif s.count('1') > 1:
                b = 'Square'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: `t` is an integer representing the number of test cases that must be greater than or equal to 0, `n` is an integer between 2 and 10, `i` is equal to `t`, `j` is equal to `n`, `s` is a string representing the last test case, stdin is empty. If at least one string `s` contains exactly one '1', then `a` is 'Triangle' and `b` is either an empty string or 'Square', and the value of `a` is being printed. If no string `s` contains exactly one '1', then `a` is 0 and `b` is either an empty string or 'Square', and either an empty string or 'Square' is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n lines of n characters ('0' or '1'). It determines whether the grid of characters contains a triangle or a square that encompasses all the '1's and prints the corresponding shape ('Triangle' or 'Square'). If no shape is found, it prints an empty string. The function processes all test cases and prints the result for each case.

