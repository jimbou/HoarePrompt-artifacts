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
        
    #State: t is 0, n is an integer equal to the integer value of the first input, a is a string equal to the second input, b is a string equal to the third input, c is a string equal to the fourth input, stdin contains no test cases, i is n.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by three strings a, b, and c. It then checks if there exists at least one position i where a[i] is not equal to c[i] and b[i] is not equal to c[i], or if there exists at least one position i where a[i] is equal to b[i] and c[i] is not equal to a[i]. If such a position exists, it prints 'YES', otherwise it prints 'NO'. The function processes all test cases and then terminates, leaving the input stream empty.

