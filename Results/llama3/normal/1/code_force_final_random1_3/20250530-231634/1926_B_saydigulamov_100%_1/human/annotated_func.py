#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines each containing n characters '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1.
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
        
    #State: `a` is an integer between 2 and 10 (inclusive), `i` is equal to `a`, `b` is an empty string, stdin contains no more test cases, input is empty, `_` is 0, `k` is a list containing the count of '1's in each of the strings input during the loop executions. If the first element of `k` is equal to the second element of `k`, 'SQUARE' is printed. Otherwise, 'TRIANGLE' is printed.

#Overall this is what the function does:This function determines the shape of a figure composed of '1's in a grid of '0's and '1's. It reads multiple test cases from standard input, where each test case consists of an integer n followed by n lines of n characters. The function then analyzes the grid to determine whether the figure is a square or a triangle and prints the corresponding shape. The function processes all test cases and does not return any value.

