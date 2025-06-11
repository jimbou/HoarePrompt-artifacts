#State of the program right berfore the function call: stdin contains n+1 inputs: first an integer n (1 ≤ n ≤ 1000) and then n lines each containing three integers x, y, and r (-10^9 ≤ x, y ≤ 10^9 and 1 ≤ r ≤ 10^9).
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: n is an integer between 1 and 1000, x is a list of n integers, y is a list of n integers, r is a list of n integers, visited is a list of n False values, coef is a list of n None values, stdin contains no inputs.
    tot = 0
    bipartite = True
    ok = False
    for i in range(n):
        if not visited[i]:
            coef[i] = 1
            tot = 0
            bipartite = True
            dfs(i)
            ok = ok or bipartite and tot != 0
        
    #State: n is an integer between 1 and 1000, x is a list of n integers, y is a list of n integers, r is a list of n integers, visited is a list of n True values, coef is a list of n integers, tot is an integer, bipartite is a boolean, ok is a boolean, stdin contains no inputs.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *n is an integer between 1 and 1000, x is a list of n integers, y is a list of n integers, r is a list of n integers, visited is a list of n True values, coef is a list of n integers, tot is an integer, bipartite is a boolean, stdin contains no inputs. If ok is True, 'YES' is printed. If ok is False, 'NO' is printed.

#Overall this is what the function does:Determines whether a given set of circles can be colored with two colors such that no two overlapping circles have the same color. The function reads input from stdin, where the first line contains the number of circles (n) and the subsequent n lines contain the x, y coordinates and radius of each circle. It then checks if it's possible to color the circles with two colors and prints 'YES' if possible, 'NO' otherwise.

