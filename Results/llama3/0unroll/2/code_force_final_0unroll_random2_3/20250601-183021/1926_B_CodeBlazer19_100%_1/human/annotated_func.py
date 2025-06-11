#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains an integer n (2 <= n <= 10) followed by n strings of n characters each, where each character is either '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1.
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
        
    #State: The loop will print either 'TRIANGLE' or 'SQUARE' for each test case, depending on whether a string with exactly one '1' is found or a string with more than one '1' is found, respectively. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the shape ('TRIANGLE' or 'SQUARE') of the figure formed by '1's in each test case. It iterates through each test case, examining the strings to determine the shape, and outputs the result for each case. The function does not modify the input value `t` and only uses it to control the number of iterations.

