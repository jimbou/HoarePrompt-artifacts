#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100) followed by t test cases. Each test case consists of four lines, each containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000) representing the coordinates of the corners of a square.
    """
    n = int(input())
     
    while n :
        
        l = int(input())
        s = 0
        s += (l//4)+(l-(4*(l//4)))//2
        print(s)
        n-=1
     
            
    """
    n = int(input())
    while n:
        coord = []
        
        res = 0
        
        for i in range(4):
            x, y = map(int, input().split())
            coord.append((x, y))
        
        coord = sorted(coord)
        
        p1 = (coord[1][0] - coord[0][0]) ** 2 + (coord[1][1] - coord[0][1]) ** 2
        
        p2 = (coord[3][0] - coord[2][0]) ** 2 + (coord[3][1] - coord[2][1]) ** 2
        
        res = math.sqrt(p1) * math.sqrt(p2)
        
        print(round(res))
        
        n -= 1
        
    #State: n is 0, stdin is empty, and the standard output contains n lines, each containing a rounded result of the product of the lengths of the diagonals of a rectangle.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four lines representing the coordinates of the corners of a rectangle. It calculates the product of the lengths of the diagonals of each rectangle, rounds the result, and prints it to standard output. The function continues this process until all test cases have been processed, at which point the standard input is empty and the standard output contains the rounded results for each test case.

