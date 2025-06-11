#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100) followed by 4t lines, each containing two integers x and y (-1000 <= x, y <= 1000).
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
        
    #State: t is an integer between 1 and 100, steps is t - 1, a, b, c, d, e, f, g, h are integers, n is a non-negative integer equal to (a - c)^2 + (b - d)^2, x is a non-negative integer equal to (a - e)^2 + (b - f)^2, stdin contains 0 lines. If x is greater than n, then the value of n which is the squared Euclidean distance between points (a, b) and (c, d) is printed. Otherwise, the value of x which is (a - e)^2 + (b - f)^2 is printed.

#Overall this is what the function does:This function reads input from stdin, expecting a series of test cases. Each test case consists of four lines, each containing two integers. The function calculates the squared Euclidean distance between the points represented by the first and second lines, and the points represented by the first and third lines. It then prints the smaller of these two distances. The function repeats this process for the specified number of test cases, after which it concludes, leaving stdin empty.

