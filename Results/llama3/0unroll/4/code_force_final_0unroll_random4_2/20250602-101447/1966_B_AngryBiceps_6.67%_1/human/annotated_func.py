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
        
    #State: The output state is a series of 'YES' or 'NO' strings, each corresponding to a test case. The output is 'YES' if the first row is the same as the last row or if the first column is the same as the last column, and 'NO' otherwise. The number of 'YES' or 'NO' strings is equal to the number of test cases, which is given by the integer t in the initial state.

#Overall this is what the function does:This function reads input from standard input, processes it as a series of test cases, and outputs a series of 'YES' or 'NO' strings. Each test case consists of two integers n and m, followed by n strings of length m, containing only 'W' and 'B'. The function checks if the first row is the same as the last row or if the first column is the same as the last column. If either condition is true, it outputs 'YES'; otherwise, it outputs 'NO'. The number of output strings corresponds to the number of test cases provided in the input.

