#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains two integers n and m (1 <= n, m <= 500) followed by n strings of length m consisting of characters 'W' and 'B'.
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
        
    #State: The output state contains t lines, each containing either 'YES' or 'NO'. Each 'YES' or 'NO' corresponds to the result of the test case in the same order as they appear in the input. 'YES' indicates that the given matrix is good, and 'NO' indicates that it is not.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs a result for each case. It accepts a series of test cases, each consisting of a matrix of characters 'W' and 'B', and determines whether the matrix is "good" or not based on specific conditions. The function returns a series of 'YES' or 'NO' outputs, one for each test case, indicating whether the corresponding matrix is good or not.

