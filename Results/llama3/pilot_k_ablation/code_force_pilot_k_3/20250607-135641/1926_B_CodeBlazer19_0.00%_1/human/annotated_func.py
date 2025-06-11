#State of the program right berfore the function call: stdin contains t test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines, each containing n characters '0' or '1'.
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
        
    #State: `t` is an integer between 2 and 10 (inclusive) and greater than or equal to 0, `i` is `t`, `n` is an integer between 2 and 10 (inclusive), `j` is `n`, `s` is the last string read from `stdin`, `stdin` is empty. If any of the strings `s` contains exactly one '1', then `a` is 'Triangle' and 'Triangle' is printed. If any of the strings `s` contains more than one '1', then `b` is 'Square' and 'Square' is printed. If none of the strings `s` contains exactly one '1' or more than one '1', then `a` is 0 and an empty string is printed.

#Overall this is what the function does:Determines and prints the shape represented by a series of 0s and 1s input from stdin, where 'Triangle' is printed if any row contains exactly one '1', 'Square' is printed if any row contains more than one '1', and an empty string is printed otherwise, for each of t test cases.

