#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100), followed by 4t lines, each containing two integers x and y (-1000 <= x, y <= 1000).
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
        
    #State: The output state after the loop executes all the iterations is the final value of the variable "res" which is the absolute value of the product of the square roots of the squared distances between the coordinates of the two pairs of points.

#Overall this is what the function does:Calculates and prints the absolute value of the product of the square roots of the squared distances between the coordinates of two pairs of points for a given number of test cases.

