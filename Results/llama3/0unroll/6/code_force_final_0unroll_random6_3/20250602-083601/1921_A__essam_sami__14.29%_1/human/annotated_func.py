#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t testcases. Each testcase consists of four lines, each line containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000), representing the coordinates of the corners of a square.
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
        
    #State: The output state will be the minimum of the squared distances between points (a, b) and (e, f), and points (c, d) and (g, h) for each testcase, printed on separate lines. The value of t will remain unchanged.

#Overall this is what the function does:This function reads input from stdin, expecting an integer t followed by t test cases, each consisting of four lines of two integers representing coordinates of a square's corners. It calculates the squared distances between two pairs of points for each test case and prints the minimum of these squared distances. The function does not modify the input value t.

