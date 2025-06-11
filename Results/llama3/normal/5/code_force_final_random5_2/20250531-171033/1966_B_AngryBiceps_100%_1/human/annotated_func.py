#State of the program right berfore the function call: stdin contains multiple test cases. Each test case starts with a line containing two integers n and m, followed by n lines each containing m characters 'W' and 'B'.
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
        
    #State: n is 0, m is an integer, a is an empty list, first_row is an empty string, last_row is an empty string, stdin contains no integers, i is -1. 'YES' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a grid of characters 'W' and 'B'. It checks if the first and last rows of the grid are the same or if the first and last columns are the same. If either condition is true, it prints 'NO', otherwise it prints 'YES'. The function processes all test cases and then terminates, leaving the input stream empty.

