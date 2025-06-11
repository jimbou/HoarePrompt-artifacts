#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 20) followed by three strings a, b, c, each consisting of n lowercase Latin letters.
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
        
    #State: t is 0, stdin is empty, n is an integer greater than or equal to 0 and less than or equal to 20, a is a string of n lowercase Latin letters, b is a string of n lowercase Latin letters, c is a string of n lowercase Latin letters, i is n. If there exists at least one index i such that a[i] is not equal to b[i] and c[i] is not equal to a[i] and c[i] is not equal to b[i], then 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three strings of lowercase Latin letters. It checks if there exists at least one position where the corresponding characters in the first two strings are different and the character in the third string is different from both. If such a position exists, it prints 'YES', otherwise it prints 'NO'. The function processes all test cases and then terminates, leaving the input stream empty.

