#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and m, followed by n strings of length m, each containing only 'W' and 'B'.
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
        
    #State: The output state will contain a series of 'YES' or 'NO' strings, each corresponding to the result of the loop's execution for each test case. The number of 'YES' or 'NO' strings will be equal to the number of test cases in the input.

#Overall this is what the function does:Determines whether a given set of strings can be transformed into each other by rotating the first and last rows, and prints 'YES' if possible, 'NO' otherwise, for each test case in the input.

