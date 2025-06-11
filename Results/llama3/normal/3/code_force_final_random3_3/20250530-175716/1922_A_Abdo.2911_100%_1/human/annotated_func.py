#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 20) followed by three strings a, b, and c, each consisting of exactly n lowercase Latin letters.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        possible = False
        
        for i in range(n):
            if a[i] == b[i]:
                if c[i] != a[i]:
                    possible = True
                    break
            elif c[i] == a[i] or c[i] == b[i]:
                continue
            else:
                possible = True
                break
        
        if possible:
            print('YES')
        else:
            print('NO')
        
    #State: t is 0, stdin is empty, n is an integer between 1 and 20, a is a string of n lowercase Latin letters, b is a string of n lowercase Latin letters, c is a string of n lowercase Latin letters, i is n. If there exists at least one index j such that a[j] is not equal to b[j] and c[j] is not equal to a[j] and c[j] is not equal to b[j], then 'YES' is printed. Otherwise, if for all indices j, either a[j] equals b[j] or c[j] equals a[j] or c[j] equals b[j], then 'NO' is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of three strings of the same length. It then checks if there exists at least one position where the third string differs from both the first and second strings. If such a position is found, it prints 'YES', otherwise it prints 'NO'. The function processes all test cases and empties the standard input.

