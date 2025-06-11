#State of the program right berfore the function call: stdin contains a number of test cases t, followed by t test cases. Each test case contains two integers n and m, followed by n strings of length m, each containing only 'W' and 'B'.
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
        
    #State: t is 0, tc is t, gr is a list containing n strings, i is n-1, stdin contains 0 test cases, n is an integer, m is an integer, and either 'YES' or 'NO' has been printed t times.

#Overall this is what the function does:The function reads a number of test cases from standard input, where each test case consists of two integers (n and m) followed by n strings of length m containing only 'W' and 'B'. It then checks if it's possible to transform the first string into the last string by changing one character at a time, with the constraint that the first and last characters of each string must be the same. If it's possible, it prints 'YES', otherwise it prints 'NO'. This process is repeated for each test case.

