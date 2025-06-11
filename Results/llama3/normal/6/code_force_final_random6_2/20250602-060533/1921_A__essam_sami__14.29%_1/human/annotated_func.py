#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100) followed by t test cases. Each test case consists of four lines, each containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000), which are the coordinates of the corners of a square with sides parallel to the coordinate axes and positive area.
    t = int(input())
    for steps in range(t):
        a, b = map(int, input().split())
        
        c, d = map(int, input().split())
        
        e, f = map(int, input().split())
        
        g, h = map(int, input().split())
        
        n = (a - e) * (a - e) + (b - f) * (b - f)
        
        x = (c - g) * (c - g) + (d - h) * (d - h)
        
        if x > n:
            print(n)
        else:
            print(x)
        
    #State: t is an integer between 1 and 100 inclusive and greater than or equal to 0, steps is t-1, stdin is empty, a, b, c, d, e, f, g, h are integers, n is the square of the distance between points (a, b) and (e, f), x is the square of the distance between points (c, d) and (g, h). If x > n, the square of the distance between points (a, b) and (e, f) which is n is being printed. Otherwise, the square of the distance between points (c, d) and (g, h) which is x is being printed.

#Overall this is what the function does:This function reads input from stdin, processes t test cases where each test case consists of four points representing the corners of a square, and prints the square of the distance between two opposite corners of the square. The function determines the square of the distance between the two pairs of opposite corners and prints the smaller of the two values.

