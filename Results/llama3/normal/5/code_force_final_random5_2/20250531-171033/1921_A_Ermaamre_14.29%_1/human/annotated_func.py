#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains four lines, each line contains two integers x_i, y_i (-1000 <= x_i, y_i <= 1000), coordinates of the corners of a square with sides parallel to the coordinate axes and positive area.
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
        
    #State: a is at least 1, i equals a - 1, stdin is empty, x1, y1, x2, y2, x3, y3, x4, y4 are integers. If x1 equals x3 and x2 equals x4, then res is the absolute difference between y3 and y1. If x1 is not equal to x3 or x2 is not equal to x4, then if x1 equals x2 and x3 equals x4, then res is the absolute difference between y2 and y1. If x1 is not equal to x2 or x3 is not equal to x4, then if x1 equals x4 and x3 equals x2, then res is the absolute difference between y2 and y1, and the square of the result is printed.

#Overall this is what the function does:Calculates and prints the area of squares defined by their corner coordinates.

