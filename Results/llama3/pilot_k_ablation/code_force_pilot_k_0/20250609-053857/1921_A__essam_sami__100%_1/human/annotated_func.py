#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of four lines, each containing two integers x_i and y_i (-1000 <= x_i, y_i <= 1000), representing the coordinates of the corners of a square.
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
        
    #State: The loop will print the square of the length of the shorter diagonal of each square, for each test case. The value of `t` remains unchanged. The input state of `stdin` is consumed and is now empty.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case represents the coordinates of a square's corners, and prints the square of the length of the shorter diagonal for each square.

