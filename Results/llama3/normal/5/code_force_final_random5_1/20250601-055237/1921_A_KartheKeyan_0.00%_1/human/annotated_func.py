#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t testcases. Each testcase consists of four lines, each line containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000), representing the coordinates of the corners of a square.
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
        
    #State: n is 0, coord is a list containing four tuples of two integers sorted in ascending order, res is the absolute value of the product of the Euclidean distances between the first and second points and the third and fourth points, i is 3, stdin is empty, and the absolute value of the product of the Euclidean distances between the first and second points and the third and fourth points is being printed.

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases. For each test case, it reads four lines of input, each containing two integers representing the coordinates of the corners of a square. It then calculates the absolute value of the product of the Euclidean distances between the first and second points and the third and fourth points, and prints this value. The function repeats this process t times, until all test cases have been processed.

