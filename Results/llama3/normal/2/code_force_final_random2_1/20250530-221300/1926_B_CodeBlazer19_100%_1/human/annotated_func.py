#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines, each containing n characters that are either '0' or '1'.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = 0
        
        b = ''
        
        for j in range(n):
            s = input()
            if s.count('1') == 1:
                a = 'TRIANGLE'
            elif s.count('1') > 1:
                b = 'SQUARE'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: t is an integer between 1 and 100 inclusive, i is t-1, n is an integer between 2 and 10 inclusive and must be greater than or equal to 0, j is n, s is a string of n characters that are either '0' or '1', stdin contains 0 test cases. If any of the strings s contains exactly one '1', then 'TRIANGLE' is printed. Otherwise, if any of the strings s contains more than one '1', then 'SQUARE' is printed, otherwise an empty string is printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints a shape type ('TRIANGLE', 'SQUARE', or an empty string) based on the presence of '1's in the input strings. It iterates over a specified number of test cases, each containing a square matrix of characters, and determines the shape type by checking the count of '1's in each row. If a row contains exactly one '1', it prints 'TRIANGLE'. If a row contains more than one '1', it prints 'SQUARE'. If no '1's are found in any row, it prints an empty string.

