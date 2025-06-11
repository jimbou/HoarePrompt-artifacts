#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100) followed by 4t lines, each containing two integers x and y (-1000 <= x, y <= 1000).
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
        
    #State: n is 0, stdin is empty, and the standard output contains 4n lines, each containing a single integer representing the area of a rectangle.

#Overall this is what the function does:This function calculates and prints the area of rectangles given their coordinates. It reads an integer t from standard input, followed by 4t lines of coordinates, each containing two integers x and y. For each set of 4 coordinates, it calculates the area of the rectangle formed by the points and prints the result to standard output, rounded to the nearest integer. The function continues this process until it has processed all t sets of coordinates, at which point it terminates, leaving the standard input empty and the standard output containing t lines, each with the area of a rectangle.

