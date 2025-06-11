#State of the program right berfore the function call: stdin contains n+1 inputs: the first input is an integer n (1 ≤ n ≤ 1000), and the next n inputs are three integers each, representing the coordinates of the center and the radius of the i-th disk. The coordinates are integers between -10^9 and 10^9, and the radius is a positive integer between 1 and 10^9.
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: n is an integer between 1 and 1000, x is a list of n values where all values are integers, y is a list of n values where all values are integers, r is a list of n values where all values are integers, visited is a list of n False values, coef is a list of n None values, stdin contains 0 inputs, i is n
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
        
    #State: n is an integer between 1 and 1000, x is a list of n values where all values are integers, y is a list of n values where all values are integers, r is a list of n values where all values are integers, visited is a list of n True values, coef is a list of n values where the value at index i is 1 if i has been visited, otherwise None, stdin contains 0 inputs, i is n, tot is 0, bipartite is True, ok is True if any i has been visited and bipartite is True and tot is not 0, otherwise False.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: n is an integer between 1 and 1000, x is a list of n values where all values are integers, y is a list of n values where all values are integers, r is a list of n values where all values are integers, visited is a list of n True values, coef is a list of n values where the value at index i is 1 if i has been visited, otherwise None, stdin contains 0 inputs, i is n, tot is 0, bipartite is True. If any i has been visited and bipartite is True and tot is not 0, then 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:Determines whether a set of disks can be colored with two colors such that no two overlapping disks have the same color. The function reads input from stdin, where the first line contains the number of disks (n), and each subsequent line contains three integers representing the coordinates of the center and the radius of a disk. The function then checks if it is possible to color the disks with two colors and prints 'YES' if it is possible, and 'NO' otherwise.

