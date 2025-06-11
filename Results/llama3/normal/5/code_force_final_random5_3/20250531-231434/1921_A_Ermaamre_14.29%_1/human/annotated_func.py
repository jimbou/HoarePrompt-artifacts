#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of four lines, each line containing two integers x and y (-1000 <= x, y <= 1000) representing the coordinates of the corners of a square.
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
        
    #State: a is an integer greater than or equal to 0 and less than or equal to 100, i is equal to a, x1, y1, x2, y2, x3, y3, x4, and y4 are integers (-1000 <= x, y <= 1000), stdin is empty. If x1 equals x3 and x2 equals x4, then res is the absolute difference between y1 and y3. If x1 equals x2 and x3 equals x4, or x1 equals x4 and x3 equals x2, then res is the absolute difference between y1 and y2, and the square of res is printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four lines representing the coordinates of a square's corners. It calculates the area of each square by determining the length of its side, which is the absolute difference between the y-coordinates of two opposite corners, and prints the area (side length squared) for each test case. The function processes all test cases and leaves the standard input empty upon completion.

