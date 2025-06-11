#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines, each containing a string of n characters '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1.
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print('SQUARE')
        else:
            print('TRIANGLE')
        
    #State: The loop will execute 'a' number of times, where 'a' is an integer between 1 and 100. In each iteration, it will read a test case from stdin, determine whether the shape formed by '1's in the grid is a square or a triangle, and print the result. After all iterations, the loop will finish, and the program will terminate. The value of 'a' will remain unchanged.

#Overall this is what the function does:Determines and prints the shape (SQUARE or TRIANGLE) formed by '1's in a grid for multiple test cases read from standard input.

