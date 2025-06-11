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
        
    #State: The output state will contain `t` lines, each containing either 'YES' or 'NO'. 'YES' indicates that the corresponding test case has a possible combination of strings `a`, `b`, and `c` that meet the given conditions, while 'NO' indicates that no such combination is possible.

#Overall this is what the function does:Determines the possibility of a combination of strings `a`, `b`, and `c` meeting certain conditions for each of `t` test cases, and outputs 'YES' if possible and 'NO' if not.

