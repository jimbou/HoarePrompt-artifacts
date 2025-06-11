#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case consists of two integers n and m, followed by n strings of length m, each containing only 'W' and 'B'.
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        a = []
        
        first_row = ''
        
        last_row = ''
        
        for i in range(n):
            a.append(input())
            first_row += a[-1][0]
            last_row += a[-1][-1]
        
        if len(set(a[0])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: The output state will be a series of 'YES' or 'NO' strings, each indicating whether the corresponding test case has a valid configuration of 'W' and 'B' characters. The number of 'YES' or 'NO' strings will be equal to the number of test cases t.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a grid of 'W' and 'B' characters. It checks each grid for a valid configuration, printing 'YES' if the configuration is valid and 'NO' otherwise. A valid configuration is one where either the first and last rows are the same, or the first column and last column are the same. The function processes all test cases and outputs the results in the same order they were input.

