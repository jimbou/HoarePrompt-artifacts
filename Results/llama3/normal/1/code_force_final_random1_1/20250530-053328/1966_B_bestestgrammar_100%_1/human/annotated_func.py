#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and m (1 <= n, m <= 500) followed by n strings of length m consisting of characters 'W' and 'B'.
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
        
    #State: t is 0, tc is t, stdin is empty, n is an integer between 0 and 500 inclusive, m is an integer between 1 and 500 inclusive, gr is a list containing n strings, i is n-1, ans is either 'YES' or 'NO' depending on the conditions described above, and impossible is either True or False depending on the conditions described above.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a grid of characters 'W' and 'B'. It then checks if it's possible to transform the top-left character of the grid into the bottom-right character by changing one character at a time, either horizontally or vertically, without changing the color of any two adjacent characters. The function prints 'YES' if such a transformation is possible and 'NO' otherwise.

