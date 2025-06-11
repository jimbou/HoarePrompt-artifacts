#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of an integer n (2 <= n <= 10) followed by n strings of length n consisting of characters '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1.
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
        
    #State: The loop will execute 'a' number of times, where 'a' is an integer between 1 and 100 inclusive. In each iteration, it will read a test case from stdin, determine whether the grid contains a triangle or a square based on the count of '1's in the strings, and print 'TRIANGLE' or 'SQUARE' accordingly. After all iterations, the loop will finish, and the program will terminate. The value of 'a' and the contents of stdin will remain unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a grid of '0's and '1's. It analyzes each grid to determine whether it contains a triangle or a square shape formed by the '1's, and prints 'TRIANGLE' or 'SQUARE' accordingly. The function processes a variable number of test cases, as specified by the initial input, and does not modify the input values.

