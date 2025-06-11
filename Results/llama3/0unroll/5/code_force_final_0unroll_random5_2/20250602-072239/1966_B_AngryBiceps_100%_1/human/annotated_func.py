#State of the program right berfore the function call: stdin contains a series of test cases. Each test case consists of a line with two integers n and m, followed by n lines, each containing m characters 'W' and 'B'.
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
        
    #State: The output state is a series of 'YES' or 'NO' for each test case, indicating whether the given grid of 'W' and 'B' characters meets the specified conditions.

#Overall this is what the function does:This function processes a series of test cases from standard input, where each test case consists of a grid of 'W' and 'B' characters. It checks if the first and last rows of the grid are the same and contain only one type of character, or if the first and last columns are the same and contain only one type of character. If either condition is met and the first and last rows/columns are different, it prints 'NO', indicating that the grid does not meet the specified conditions. Otherwise, it prints 'YES'. The function returns a series of 'YES' or 'NO' outputs, one for each test case.

