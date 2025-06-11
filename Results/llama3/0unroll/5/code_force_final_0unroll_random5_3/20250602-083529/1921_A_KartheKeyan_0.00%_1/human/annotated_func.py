#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of four lines, each containing two integers x and y (-1000 <= x, y <= 1000). The four points (x, y) form a square with sides parallel to the coordinate axes and positive area.
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
        
        res = abs(math.sqrt(p1) * math.sqrt(p2))
        
        print(res)
        
        n -= 1
        
    #State: n is 0, stdin is empty

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases. For each test case, it reads four lines of input, each containing two integers x and y, which form a square with sides parallel to the coordinate axes and positive area. The function then calculates and prints the area of the square. The function repeats this process t times, until all test cases have been processed, leaving the input stream empty.

