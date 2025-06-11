#State of the program right berfore the function call: n is a positive integer, x, y, and r are lists of integers of length n, visited is a list of boolean values of length n, coef0 and coef1 are lists of integers of length n, and nodes is a list of integers.
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef0 = [None] * n
    coef1 = [None] * n
    nodes = []
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: n is an integer, x is a list of integers of length n, y is a list of integers of length n, r is a list of integers of length n, visited is a list of False values of length n, coef0 is a list of None values of length n, coef1 is a list of None values of length n, nodes is an empty list, stdin contains no inputs, i is n-1
    ok = False
    for i in range(n):
        if not visited[i]:
            coef0[i] = 0
            coef1[i] = 1
            nodes = []
            dfs(i)
            c0 = 0
            c1 = 0
            for j in nodes:
                c0 += coef0[j]
                c1 += coef1[j]
            ok = ok or c1 != 0
        
    #State: n is an integer greater than or equal to 0, x is a list of integers of length n, y is a list of integers of length n, r is a list of integers of length n, visited is a list of boolean values of length n where all elements are True, coef0 is a list of integers of length n where all elements are 0, coef1 is a list of integers of length n where all elements are 1, nodes has at least n nodes, ok is True if c1 is not equal to 0, otherwise it remains False, c0 is the sum of all coef0 values in the nodes list, c1 is the sum of all coef1 values in the nodes list, and i is n-1.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: n is an integer greater than or equal to 0, x is a list of integers of length n, y is a list of integers of length n, r is a list of integers of length n, visited is a list of boolean values of length n where all elements are True, coef0 is a list of integers of length n where all elements are 0, coef1 is a list of integers of length n where all elements are 1, nodes has at least n nodes, c0 is the sum of all coef0 values in the nodes list, c1 is the sum of all coef1 values in the nodes list, and i is n-1. If c1 is not equal to 0, 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function determines whether a given set of nodes with coordinates and radii can be traversed in a way that satisfies a certain condition. It takes no parameters but reads input from the standard input, expecting a positive integer n followed by n lines of input, each containing three integers representing the x-coordinate, y-coordinate, and radius of a node. The function then performs a depth-first search on the nodes, calculating coefficients for each node and checking if the sum of these coefficients is non-zero. If the sum is non-zero, the function prints 'YES', indicating that the nodes can be traversed in a way that satisfies the condition. Otherwise, it prints 'NO'.

#State of the program right berfore the function call: i is an integer such that 0 <= i < n, visited is a list of boolean values of length n, nodes is a list of integers, x, y, and r are lists of integers of length n, and coef0 and coef1 are lists of integers of length n.
    if (not visited[i]) :
        visited[i] = True
        nodes.append(i)
        for j in range(n):
            dx = x[i] - x[j]
            
            dy = y[i] - y[j]
            
            if not visited[j] and (r[i] + r[j]) ** 2 == dx ** 2 + dy ** 2:
                coef0[j] = r[i] + r[j] - coef0[i]
                coef1[j] = -coef1[i]
                dfs(j)
            
        #State: i is an integer such that 0 <= i < n, visited is a list of boolean values of length n where all elements are True, nodes is a list of integers with all elements from 0 to n-1 appended to the end, x, y, r, coef0, and coef1 are lists of integers of length n.
    #State: *i is an integer such that 0 <= i < n, visited is a list of boolean values of length n. If all elements of visited are False, then all elements of visited are set to True, and all integers from 0 to n-1 are appended to the end of nodes. x, y, r, coef0, and coef1 are lists of integers of length n. Otherwise, no changes are made to visited, nodes, x, y, r, coef0, and coef1.

#Overall this is what the function does:This function performs a depth-first search (DFS) on a graph, starting from a given node 'i'. If 'i' has not been visited before, it marks 'i' as visited, adds 'i' to the list of nodes, and recursively explores neighboring nodes that are not visited and are at a distance equal to the sum of their radii. The function updates the coefficients (coef0 and coef1) for the neighboring nodes based on the current node's coefficients and radii. If all nodes have been visited, the function returns with the updated lists of visited nodes, nodes, and coefficients. If not all nodes have been visited, the function returns without modifying the input lists.

