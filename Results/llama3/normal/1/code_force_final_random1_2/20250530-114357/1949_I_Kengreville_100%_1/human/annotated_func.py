#State of the program right berfore the function call: stdin contains n+1 inputs: the first input is an integer n (1 ≤ n ≤ 1000), and the next n inputs are three integers each, representing the x, y coordinates and the radius r of a disk, such that -10^9 ≤ x, y ≤ 10^9 and 1 ≤ r ≤ 10^9.
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: `n` is an integer between 1 and 1000 (inclusive), `x` is a list of n values where all values are integers, `y` is a list of n values where all values are integers, `r` is a list of n values where all values are integers, `visited` is a list of n False values, `coef` is a list of n None values, `stdin` contains 0 inputs, `i` is n-1.
    #
    #In natural language, after the loop executes all the iterations, the lists `x`, `y`, and `r` will be fully populated with integers, representing the x, y coordinates and radius of each disk, respectively. The `visited` list remains unchanged with all False values, and the `coef` list remains unchanged with all None values. The `stdin` will be empty as all inputs have been consumed, and the loop counter `i` will be at `n-1`, indicating that the loop has completed all iterations.
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
        
    #State: n is an integer between 1 and 1000 (inclusive), x is a list of n values where all values are integers, y is a list of n values where all values are integers, r is a list of n values where all values are integers, visited is a list of n True values, coef is a list of n values where coef[i] is 1 if i was not visited before, otherwise it remains None, i is n-1, tot is a value that may or may not be 0, bipartite is True if the graph is bipartite and False otherwise, ok is True if the graph is bipartite and tot is not 0 and False otherwise, stdin contains 0 inputs.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: n is an integer between 1 and 1000 (inclusive), x is a list of n values where all values are integers, y is a list of n values where all values are integers, r is a list of n values where all values are integers, visited is a list of n True values, coef is a list of n values where coef[i] is 1 if i was not visited before, otherwise it remains None, i is n-1, stdin contains 0 inputs. If the graph is bipartite and the current value of tot is not 0, then ok is True and 'YES' is printed. Otherwise, ok is False because either the graph is not bipartite or tot is 0, and 'NO' is printed.

#Overall this is what the function does:This function determines whether a graph represented by a set of disks is bipartite and has a non-zero total value. It takes as input a series of disks, each described by its x and y coordinates and radius, and outputs 'YES' if the graph is bipartite and has a non-zero total value, and 'NO' otherwise. The function processes the input disks, checks for bipartiteness, and calculates the total value. If the graph is bipartite and the total value is non-zero, it prints 'YES', otherwise it prints 'NO'.

