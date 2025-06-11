#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines each containing n characters '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1.
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print(k)
        
    #State: The output state is a list of integers, where each integer represents the count of '1's in a row of the grid, but only for the rows that contain a square or triangle with all '1's. The list only includes the counts for the first two rows that contain '1's. If no such shape is found, the output is empty. The value of 'a' remains unchanged, still representing the number of lines in the grid.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case represents a grid containing a triangle or square of '1's. It processes each grid, and if the first two rows containing '1's have the same count of '1's, it prints a list of these counts. The function does not modify the input data and does not return any value, only printing the results for specific cases.

