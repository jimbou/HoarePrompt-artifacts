#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two integers n and m (1 <= n, m <= 500) and a grid of n x m characters 'W' and 'B'.
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
        
    #State: n is greater than or equal to 0, i is n-1, m is an integer, a is a list containing n lines read from stdin, first_row is a string containing the first character of each line read from stdin, last_row is a string containing the last character of each line read from stdin, stdin contains 0 test cases, _ is t-1. If the first and last lines of a both contain only one unique character and are not the same, then 'NO' is printed. Otherwise, either the first row of a or the last row of a or both contain more than one unique character, or the first row of a is equal to the last row of a, or both the first row of a and the last row of a contain exactly one unique character, and 'YES' is printed.

#Overall this is what the function does:Determines whether a given grid of characters 'W' and 'B' has a valid configuration, printing 'YES' if the first and last rows or columns have the same character or more than one unique character, and 'NO' otherwise.

