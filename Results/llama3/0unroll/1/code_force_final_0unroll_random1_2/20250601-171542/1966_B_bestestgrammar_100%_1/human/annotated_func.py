#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two integers n and m (1 <= n, m <= 500), followed by n lines each containing m characters 'W' and 'B'.
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
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, one for each test case, indicating whether it is possible to make the first and last characters of the grid the same by changing characters in the grid, without changing the characters in the first and last rows and columns. The value of `t` will remain unchanged. The input from stdin will be consumed and not available for further use.

#Overall this is what the function does:This function reads input from stdin, processes it as a series of test cases, and prints to the console whether it's possible to make the first and last characters of a grid the same by changing characters within the grid, without altering the first and last rows and columns. It consumes the input from stdin and leaves the value of `t` unchanged.

