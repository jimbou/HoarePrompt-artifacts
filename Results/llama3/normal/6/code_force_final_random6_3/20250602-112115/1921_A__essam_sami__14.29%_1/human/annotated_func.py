#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of four lines, each containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000), representing the coordinates of the corners of a square.
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
        
    #State: t is an integer equal to 0, stdin is empty, steps is equal to the initial value of t, a, b, c, d, e, f, g, h are integers, n is an integer equal to (a - e)^2 + (b - f)^2, x is an integer equal to (c - g)^2 + (d - h)^2, and the program has printed the larger value between n and x for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four lines of coordinates representing the corners of a square. It calculates the squared distance between two pairs of points for each test case and prints the larger of the two squared distances. The function processes all test cases and empties the standard input.

