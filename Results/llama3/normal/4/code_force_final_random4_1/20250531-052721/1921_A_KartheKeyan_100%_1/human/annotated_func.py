#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains four lines, each line contains two integers x_i, y_i (-1000 <= x_i, y_i <= 1000) representing the coordinates of the corners of a square with positive area and sides parallel to the coordinate axes.
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
        
    #State: `coord` is a sorted list containing four tuples of two integers, `res` is the square root of the product of the squared distances between the first and second points and the third and fourth points, `p1` is the squared distance between the first and second points, `p2` is the squared distance between the third and fourth points, `i` is 3, `n` is 0, stdin is empty, and the rounded value of `res` is being printed.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases. For each test case, it reads four lines of input, each containing two integers representing the coordinates of the corners of a square. The function calculates the area of the square by finding the distance between the first and second points and the third and fourth points, and then prints the rounded value of the square root of the product of these distances. The function repeats this process for all test cases and then terminates, leaving the standard input empty.

