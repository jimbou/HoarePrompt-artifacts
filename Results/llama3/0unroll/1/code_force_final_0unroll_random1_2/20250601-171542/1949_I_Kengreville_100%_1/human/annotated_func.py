#State of the program right berfore the function call: n is a positive integer, x, y, and r are lists of integers of length n, visited is a list of boolean values of length n, and coef is a list of integers of length n.
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: n is an integer, x is a list of n integers, y is a list of n integers, r is a list of n integers, visited is a list of n False values, coef is a list of n None values, stdin contains no input
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
        
    #State: Output State: n is an integer, x is a list of n integers, y is a list of n integers, r is a list of n integers, visited is a list of n True values, coef is a list of n integers, tot is an integer, bipartite is a boolean, ok is a boolean
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *n is an integer, x is a list of n integers, y is a list of n integers, r is a list of n integers, visited is a list of n True values, coef is a list of n integers, tot is an integer, bipartite is a boolean. If ok is True, 'YES' is printed. If ok is False, 'NO' is printed.

#Overall this is what the function does:This function determines whether a given set of circles can be colored with two colors such that no two overlapping circles have the same color. It takes as input the number of circles (n) and the coordinates and radii of each circle (x, y, r). The function then performs a depth-first search to check for bipartiteness and prints 'YES' if the circles can be colored and 'NO' otherwise. The function modifies the input lists (visited, coef) and prints a string to the console.

