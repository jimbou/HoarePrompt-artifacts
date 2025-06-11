#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of four lines, each containing two integers x_i and y_i (-1000 <= x_i, y_i <= 1000) representing the coordinates of the corners of a square.
    a = int(input())
    for i in range(a):
        x1, y1 = map(int, input().split())
        
        x2, y2 = map(int, input().split())
        
        x3, y3 = map(int, input().split())
        
        x4, y4 = map(int, input().split())
        
        if x1 == x3 and x2 == x4:
            if y1 < y3:
                res = abs(y3 - y1)
            else:
                res = abs(y1 - y3)
        elif x1 == x2 and x3 == x4:
            if y1 < y2:
                res = abs(y2 - y1)
            else:
                res = abs(y1 - y2)
        elif x1 == x4 and x3 == x2:
            if y1 < y2:
                res = abs(y2 - y1)
            else:
                res = abs(y1 - y2)
        
        print(res ** 2)
        
    #State: `a` is an integer between 1 and 100 (inclusive), `i` is `a-1`, `x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, `y4` are integers (-1000 <= `x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, `y4` <= 1000), stdin is empty. If `x1` is equal to `x3` and `x2` is equal to `x4`, then `res` is the absolute difference between `y1` and `y3`. Otherwise, if `x1` is equal to `x2` and `x3` is equal to `x4`, or if `x1` is equal to `x4` and `x3` is equal to `x2`, then `res` is the absolute difference between `y1` and `y2`. The square of `res` is being printed.

#Overall this is what the function does:Calculates and prints the area of squares given their corner coordinates. The function reads an integer t from standard input, representing the number of test cases. For each test case, it reads the coordinates of four corners of a square and calculates the side length of the square by finding the absolute difference between the y-coordinates of two opposite corners. It then prints the square of the side length, which represents the area of the square. The function processes all test cases and leaves the standard input empty.

