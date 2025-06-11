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
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, each corresponding to whether a test case has a possible combination of strings a, b, and c that meet the given conditions. The number of 'YES' or 'NO' printed will be equal to the initial value of t. The value of t will be unchanged, and the values of n, a, b, and c will be updated for each test case but will not be printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and three strings a, b, and c, each of length n. It then checks for each test case whether there exists a combination of strings a, b, and c that meet certain conditions (i.e., a[i] == b[i] and c[i] != a[i], or c[i] == a[i] or c[i] == b[i] but not both). If such a combination exists, it prints 'YES' to the console; otherwise, it prints 'NO'. The function processes all test cases and prints the corresponding results, leaving the input values unchanged.

