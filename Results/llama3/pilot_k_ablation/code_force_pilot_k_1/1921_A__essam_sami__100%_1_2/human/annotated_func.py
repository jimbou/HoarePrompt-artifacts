#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100) followed by 4t lines, each containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000) representing the coordinates of the corners of a square with sides parallel to the coordinate axes and positive area.
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
        
    #State: t is an integer between 1 and 100 (inclusive), stdin is empty, steps is t, a, b, c, d, e, f, g, h are integers, n is a non-negative integer, x is a non-negative integer. The value of either n or x is printed for each iteration of the loop.

#Overall this is what the function does:The function reads input from stdin, expecting an integer t (1 <= t <= 100) followed by 4t lines of two integers each, representing coordinates of squares. It then calculates the squared distances between points on each square and prints the smaller of the two squared distances for each square. The function consumes all input from stdin and produces t output values, one for each square.

