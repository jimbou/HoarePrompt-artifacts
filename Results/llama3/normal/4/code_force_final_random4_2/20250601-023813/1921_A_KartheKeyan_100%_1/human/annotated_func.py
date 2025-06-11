#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of four lines, each containing two integers x and y (-1000 <= x, y <= 1000).
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
        
    #State: n is an integer equal to 0 and n is currently greater than or equal to 0, coord is a sorted list containing four tuples of two integers, res is the square root of the product of the squared differences of the x and y coordinates of the first and second tuples and the third and fourth tuples in the sorted coord, p1 is the squared difference of the x and y coordinates of the first and second tuples in the sorted coord, p2 is the squared difference of the x and y coordinates of the third and fourth tuples in the sorted coord, i is 3, stdin contains 0 test cases, and the rounded value of res is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of four lines containing two integers each. It calculates the area of a rectangle formed by the points in each test case and prints the result. The function continues to process test cases until the specified number of cases (read from standard input) is reached.

