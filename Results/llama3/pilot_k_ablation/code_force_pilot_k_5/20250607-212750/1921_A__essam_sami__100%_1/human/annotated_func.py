#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t testcases. Each testcase contains four lines, each line contains two integers x_i, y_i (-1000 <= x_i, y_i <= 1000), coordinates of the corners of the square.
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
        
    #State: t is an integer between 1 and 100, steps is equal to t-1, a, b, c, d, e, f, g, and h are integers, n is the square of the difference between a and c plus the square of the difference between b and d, x is the square of the difference between a and e plus the square of the difference between b and f, stdin is empty. If x is greater than n, the value of n is printed. Otherwise, the value of x is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four pairs of integers representing the coordinates of the corners of a square. It calculates the square of the distance between the first pair of coordinates and the second pair, and the square of the distance between the first pair and the third pair. It then prints the smaller of these two squared distances for each test case.

