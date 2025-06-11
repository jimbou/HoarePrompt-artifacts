#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains an integer n (2 <= n <= 10) followed by n strings of n characters each, consisting of '0' and '1'. The grid contains exactly one triangle or exactly one square that contains all the '1' s in the grid. The size of the triangle or square is greater than 1.
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
        
    #State: The loop will print out either 'TRIANGLE' or 'SQUARE' for each test case, depending on whether the grid contains a triangle or a square of '1's, respectively. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints out whether each test case contains a triangle or a square of '1's. It accepts no parameters and returns no value, only printing the results for each test case. The function's purpose is to classify the shapes formed by '1's in the input grids.

