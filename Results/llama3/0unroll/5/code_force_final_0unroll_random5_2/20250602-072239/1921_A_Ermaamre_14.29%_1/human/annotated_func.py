#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains four lines, each line containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000) representing the coordinates of the corners of a square.
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
        
    #State: The output state will be the squares of the lengths of the sides of 'a' squares, each square represented by four lines of coordinates, printed to the console.

#Overall this is what the function does:This function reads input from the standard input, where the first line contains an integer 't' representing the number of test cases. Each test case consists of four lines, each containing two integers representing the coordinates of the corners of a square. The function calculates the length of the side of each square and prints the square of this length to the console for each test case.

