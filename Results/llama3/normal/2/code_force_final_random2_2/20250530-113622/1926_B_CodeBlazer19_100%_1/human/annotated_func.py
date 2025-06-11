#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of an integer n (2 <= n <= 10) followed by n strings of n characters each, where each character is either '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1.
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
        
    #State: `t` is an integer between 1 and 100, stdin is empty, `i` is equal to `t`, `n` is an integer, `j` is equal to `n`, `s` is a string from the input, `a` is either 0 or 'TRIANGLE', `b` is either an empty string or 'SQUARE'. The value of `a` or `b` is printed for each test case.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the shape ('TRIANGLE' or 'SQUARE') of the figure formed by '1's in each test case. It accepts no parameters and returns no value, only printing the results for each test case. After execution, stdin is empty, and the function has printed the shape for each of the 't' test cases.

