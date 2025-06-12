#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100) followed by t test cases. Each test case consists of four lines, each line containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000) representing the coordinates of the corners of a square.
    t = int(input())
    for steps in range(t):
        a, b = map(int, input().split())
        
        c, d = map(int, input().split())
        
        e, f = map(int, input().split())
        
        g, h = map(int, input().split())
        
        n = (a - c) * (a - c) + (b - d) * (b - d)
        
        x = (a - e) * (a - e) + (b - f) * (b - f)
        
        if x > n:
            print(n)
        else:
            print(x)
        
    #State: t is an integer between 1 and 100, stdin contains 0 test cases, steps is t, a, b, c, d, e, f, g, h are integers, n is the square of the distance between points (a, b) and (c, d) of the last test case, x is the square of the distance between points (a, b) and (e, f) of the last test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four pairs of coordinates representing the corners of a square. For each test case, it calculates the square of the distance between two pairs of points and prints the smaller of the two squared distances. The function processes all test cases and then terminates, leaving the input stream empty.

