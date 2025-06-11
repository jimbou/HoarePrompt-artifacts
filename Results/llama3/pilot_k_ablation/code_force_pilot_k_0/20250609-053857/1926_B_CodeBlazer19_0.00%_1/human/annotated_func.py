#State of the program right berfore the function call: stdin contains multiple test cases. Each test case starts with an integer n (2 <= n <= 10) followed by n lines, each containing a string of n characters '0' or '1'.
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
        
    #State: The loop will print 'Triangle' if any of the input strings contain exactly one '1', otherwise it will print 'Square'. The value of t will remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n strings of n characters each. It then checks each string for the presence of '1' characters. If any string contains exactly one '1', it prints 'Triangle'. If no string contains exactly one '1' but at least one string contains more than one '1', it prints 'Square'. The function processes all test cases and prints the corresponding shape for each case, leaving the input variable t unchanged.

