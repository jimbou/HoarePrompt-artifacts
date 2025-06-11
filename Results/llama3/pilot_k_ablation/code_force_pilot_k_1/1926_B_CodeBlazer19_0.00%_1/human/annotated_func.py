#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines each containing n characters '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1.
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
        
    #State: `t` is an integer between 1 and 100, inclusive, `n` is an integer between 2 and 10, inclusive, `i` is `t`, stdin contains 0 test cases, `a` is either 'Triangle' or 0, `b` is either 'Square' or an empty string. If the grid contains exactly one triangle, then `a` is 'Triangle' and it was printed. If the grid contains exactly one square, then `b` is 'Square' and it was printed. If the grid contains neither a triangle nor a square, then `a` is 0 and `b` is an empty string, and an empty string was printed.

#Overall this is what the function does:This function reads input from stdin, processes a series of test cases, and prints the shape ('Triangle' or 'Square') of a single shape composed of '1's in a grid, or an empty string if no shape is found. It accepts no parameters and returns no value, instead printing the shape of the grid for each test case. After execution, the function has processed all test cases and printed the corresponding shapes or empty strings.

