#State of the program right berfore the function call: stdin contains t test cases. Each test case contains an integer n followed by n lines each containing a string of n characters that are either '0' or '1'.
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
        
    #State: `t` is a positive integer, `i` is `t-1`, `n` is an integer, `a` is either 'Triangle' or 0, `b` is either 'Square' or an empty string. If `a` is 'Triangle', then at least one string `s` contains exactly one '1'. If `a` is 0, then no string `s` contains exactly one '1' and `b` is either 'Square' or an empty string.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts a positive integer `t` representing the number of test cases. For each test case, it reads an integer `n` and `n` lines of strings containing '0' or '1' characters. It checks each string for the presence of exactly one '1' (indicating a 'Triangle') or more than one '1' (indicating a 'Square'). If a 'Triangle' is found, it prints 'Triangle'. Otherwise, it prints 'Square' if a 'Square' is found; otherwise, it prints nothing. The function processes all `t` test cases and prints the corresponding results.

