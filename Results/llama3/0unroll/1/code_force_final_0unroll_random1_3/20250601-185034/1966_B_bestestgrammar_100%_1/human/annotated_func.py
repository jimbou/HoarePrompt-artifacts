#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two integers n and m, followed by n strings of length m, each containing only 'W' and 'B'. 1 <= t <= 10^4, 1 <= n, m <= 500, and the sum of n*m over all test cases does not exceed 3*10^5.
    t = int(input())
    for tc in range(t):
        n, m = map(int, input().split())
        
        gr = []
        
        for i in range(n):
            gr.append(input())
        
        ans = 'YES'
        
        if gr[0][0] != gr[n - 1][m - 1]:
            impossible = True
            for j in range(m - 1):
                if gr[0][j] != gr[0][j + 1] or gr[n - 1][j] != gr[n - 1][j + 1]:
                    impossible = False
            if impossible:
                ans = 'NO'
            impossible = True
            for i in range(n - 1):
                if gr[i][0] != gr[i + 1][0] or gr[i][m - 1] != gr[i + 1][m - 1]:
                    impossible = False
            if impossible:
                ans = 'NO'
        
        print(ans)
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, each corresponding to a test case. The output will indicate whether it is possible to transform the first row and column of the grid into the last row and column by changing only one cell at a time, with the constraint that the entire grid must remain a valid chessboard pattern at each step. The number of 'YES' and 'NO' outputs will be equal to the value of t, which is an integer between 1 and 10^4.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a grid of 'W' and 'B' characters. It then determines whether it is possible to transform the first row and column of the grid into the last row and column by changing only one cell at a time, while maintaining a valid chessboard pattern at each step. The function prints 'YES' to the console for each test case where such a transformation is possible, and 'NO' otherwise. The number of outputs is equal to the number of test cases provided in the input.

