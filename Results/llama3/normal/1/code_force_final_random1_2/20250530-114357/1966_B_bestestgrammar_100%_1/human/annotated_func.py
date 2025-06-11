#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two integers n and m (1 <= n, m <= 500) followed by n lines, each containing m characters 'W' and 'B'.
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
        
    #State: `t` is a positive integer, `tc` is `t`, `n` is an integer, `m` is an integer, `gr` is a list containing `n` strings, `i` is `n-1`, `ans` is 'YES' if the first character of the first string in `gr` is the same as the last character of the last string in `gr`, 'NO' otherwise.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers (n and m) followed by n lines of m characters ('W' and 'B'). It then checks if the first character of the first line is the same as the last character of the last line. If they are the same, it prints 'YES', otherwise, it checks if there are any differences in the first or last columns or rows. If there are no differences, it prints 'NO', otherwise, it prints 'YES'. The function repeats this process for all test cases.

