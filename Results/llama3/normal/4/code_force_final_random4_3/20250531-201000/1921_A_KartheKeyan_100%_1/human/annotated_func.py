#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t testcases. Each testcase consists of four lines, each line containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000), which are the coordinates of the corners of a square with sides parallel to the coordinate axes and positive area.
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
        
    #State: n is an integer equal to 0, coord is a sorted list containing four tuples of two integers, res is the square root of the product of the squared differences between the coordinates of the second and first tuples and the fourth and third tuples, p1 is the squared difference between the coordinates of the second and first tuples, p2 is the squared difference between the coordinates of the fourth and third tuples, i is equal to 3, x is an integer, y is an integer, stdin contains 0 testcases, and the rounded value of res is being printed.

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases. For each test case, it reads four lines of input, each containing two integers representing the coordinates of a square's corners. The function then calculates the area of the square by finding the difference between the coordinates of the second and first points, and the fourth and third points, taking the square root of the product of these differences, and rounding the result. The function prints the rounded area for each test case. After processing all test cases, the function concludes with the input buffer empty and the number of test cases set to 0.

