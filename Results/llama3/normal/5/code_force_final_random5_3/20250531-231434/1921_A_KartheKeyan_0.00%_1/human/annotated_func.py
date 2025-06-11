#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100), followed by t test cases. Each test case contains four lines, each line containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000), representing the coordinates of the corners of a square with positive area and sides parallel to the coordinate axes.
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
        
    #State: n is an integer equal to its original value minus t and n is currently equal to 0, coord is a sorted list containing four pairs of coordinates (x, y), res is the absolute value of the product of the square roots of the squared differences between the coordinates of the second and first points and the coordinates of the fourth and third points, p1 is the squared difference between the coordinates of the second and first points, p2 is the squared difference between the coordinates of the fourth and third points, i is 3, and stdin contains 0 test cases, and the absolute value of the product of the square roots of the squared differences between the coordinates of the second and first points and the coordinates of the fourth and third points has been printed t times.

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases. For each test case, it reads four pairs of coordinates (x, y) representing the corners of a square with positive area and sides parallel to the coordinate axes. The function then calculates the area of the square by finding the absolute value of the product of the square roots of the squared differences between the coordinates of the second and first points and the coordinates of the fourth and third points. Finally, it prints the calculated area for each test case.

