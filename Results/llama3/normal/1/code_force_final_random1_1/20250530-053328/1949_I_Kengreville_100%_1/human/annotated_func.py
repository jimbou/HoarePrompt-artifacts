#State of the program right berfore the function call: n is a positive integer, x, y, and r are lists of n integers, visited is a list of n boolean values, and coef is a list of n values that can be either 1 or -1.
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: `n` is a non-negative integer, `i` is `n`, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers, `visited` is a list of `n` False values, `coef` is a list of `n` None values, stdin contains no inputs
    #
    #In natural language, the output state after the loop executes all iterations is that `n` remains unchanged, `i` is now equal to `n`, and the lists `x`, `y`, and `r` are fully populated with integers from the input, while the lists `visited` and `coef` remain unchanged with all False values and None values, respectively.
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
        
    #State: n is a non-negative integer, i is n, x is a list of n integers, y is a list of n integers, r is a list of n integers, visited is a list of n True values, coef is a list of n integers, tot is 0, bipartite is True, ok is True if there exists an i such that bipartite is True and tot is not 0, stdin contains no inputs
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *n is a non-negative integer, i is n, x is a list of n integers, y is a list of n integers, r is a list of n integers, visited is a list of n True values, coef is a list of n integers, tot is 0, bipartite is True, and either 'YES' is printed if there exists an i such that bipartite is True and tot is not 0, or 'NO' is printed if no such i exists.

#Overall this is what the function does:This function determines whether a given graph is bipartite and contains a cycle with a non-zero total edge weight. It takes no arguments, but instead reads input from stdin, expecting a positive integer n followed by n lines, each containing three integers representing the x, y, and r values of an edge. The function then performs a depth-first search on the graph, checking for bipartiteness and non-zero total edge weight. If such a cycle is found, the function prints 'YES', otherwise it prints 'NO'.

