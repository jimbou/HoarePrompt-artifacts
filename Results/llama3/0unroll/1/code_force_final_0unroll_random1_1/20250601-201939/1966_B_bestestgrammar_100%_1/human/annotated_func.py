#State of the program right berfore the function call: stdin contains a sequence of lines where the first line contains a single integer t (1 ≤ t ≤ 10^4), then t test cases. Each test case starts with a line containing two integers n and m (1 ≤ n, m ≤ 500), then n lines each containing m characters 'W' and 'B'.
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
        
    #State: The loop will print 'YES' or 'NO' for each test case, indicating whether it is possible to transform the top-left character into the bottom-right character by changing one character at a time, either horizontally or vertically, without changing the color of the character. The output will be a series of 'YES' or 'NO' separated by newline characters, with the number of lines equal to the number of test cases.

#Overall this is what the function does:The function reads a sequence of test cases from standard input, where each test case consists of a grid of characters 'W' and 'B'. It then determines whether it is possible to transform the top-left character into the bottom-right character by changing one character at a time, either horizontally or vertically, without changing the color of the character. The function prints 'YES' if such a transformation is possible and 'NO' otherwise, with the output consisting of a series of 'YES' or 'NO' separated by newline characters, one for each test case.

