#State of the program right berfore the function call: stdin contains t test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines each containing n characters '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1.
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
        
    #State: `a` is an integer between 2 and 10 (inclusive) and `a` must be equal to 0, `i` is `a`, `b` is a string of length 2 to 10 containing '0' or '1', `k` is a list containing the count of '1' in `b` if '1' is present in `b`, stdin contains t-`a` test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines each containing n characters '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1, _ is int(input())-1, int(input()) must be greater than or equal to 0. If the first element of `k` is equal to the second element of `k`, 'SQUARE' is printed. Otherwise, 'TRIANGLE' is printed.

#Overall this is what the function does:This function determines the shape of a grid of '0's and '1's, either a triangle or a square, based on the count of '1's in the first two rows. It reads input from stdin, processes multiple test cases, and prints 'SQUARE' if the counts are equal, otherwise 'TRIANGLE'.

