#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and m (1 <= n, m <= 500) followed by n strings of length m consisting of 'W' and 'B'.
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        a = []
        
        first_row = ''
        
        last_row = ''
        
        for i in range(n):
            a.append(input())
            first_row += a[-1][0]
            last_row += a[-1][-1]
        
        if len(set(a[0])) == 1 and len(set(a[-1])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and len(set(last_row)
            ) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: t is 0, n is 0, m is an integer greater than 0, a is a list containing n strings, first_row is a string containing n characters, last_row is a string containing n characters, stdin contains 0 test cases, _ is t-1, i is n-1. If the first and last strings in the list a contain only one unique character each and these characters are different from each other, 'NO' is printed. Otherwise, if the first and last strings in the list a are single-character strings and are different, 'NO' is printed. In all other cases, 'YES' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a grid of characters ('W' and 'B'). It checks if the first and last rows or columns of the grid are single-character strings and different from each other. If so, it prints 'NO', indicating that the grid does not meet the condition. Otherwise, it prints 'YES', indicating that the grid meets the condition. The function processes all test cases and prints the result for each one.

