#State of the program right berfore the function call: stdin contains t test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines each containing n characters '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1.
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print(k)
        
    #State: The loop will print the number of '1's in the first and second rows of each grid that contains a square, and the value of 'a' will be unchanged.

#Overall this is what the function does:This function reads input from stdin, processes a series of test cases, and prints the number of '1's in the first and second rows of each grid that contains a square. It does not modify the input value 'a' and does not perform any actions on grids that contain triangles or other shapes.

