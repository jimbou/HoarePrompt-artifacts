#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t testcases. Each testcase consists of four lines, each line containing two integers x and y (-1000 <= x, y <= 1000) representing the coordinates of the corners of a square with positive area and sides parallel to the coordinate axes.
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
        
    #State: t is an integer between 1 and 100 (inclusive), stdin is empty, steps is equal to t, a, b, c, d, e, f, g, h are integers, n is the square of the distance between (a, b) and (c, d) for the last testcase, x is the square of the distance between (a, b) and (e, f) for the last testcase.

#Overall this is what the function does:This function reads input from stdin, processes t test cases, and prints the minimum square distance between two points in each testcase. It accepts no parameters and returns no value, but it modifies the state of stdin by consuming all input. The function's purpose is to calculate and print the minimum square distance between two points in each testcase.

