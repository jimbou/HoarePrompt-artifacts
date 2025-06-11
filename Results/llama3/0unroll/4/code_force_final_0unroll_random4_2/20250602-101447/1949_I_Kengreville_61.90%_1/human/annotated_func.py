#State of the program right berfore the function call: n is a positive integer, x, y, and r are lists of integers of length n, visited is a list of boolean values of length n, coef0 and coef1 are lists of integers of length n, nodes is a list of integers.
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
        
    #State: Output State: n is a positive integer equal to the input value, x is a list of n integers, y is a list of n integers, r is a list of n integers, visited is a list of n False values, coef0 is a list of n None values, coef1 is a list of n None values, and nodes is an empty list.
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
        
    #State: Output State: The output state after the loop executes all the iterations is as follows:
    #
    #- `n` remains unchanged as a positive integer equal to the input value.
    #- `x` remains unchanged as a list of `n` integers.
    #- `y` remains unchanged as a list of `n` integers.
    #- `r` remains unchanged as a list of `n` integers.
    #- `visited` is a list of `n` True values, as each node is visited during the depth-first search (DFS) traversal.
    #- `coef0` and `coef1` are lists of `n` integers, where each element represents the coefficients of the nodes in the DFS traversal. The values of these coefficients depend on the structure of the graph represented by the input lists `x` and `y`.
    #- `nodes` is a list of nodes that were visited during the DFS traversal.
    #- `ok` is True if at least one node in the DFS traversal has a non-zero coefficient, indicating that the graph contains a cycle. Otherwise, `ok` is False.
    #
    #Note that the exact values of `coef0`, `coef1`, and `nodes` depend on the specific input graph represented by `x` and `y`, which is not provided in the problem statement.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The program executes a depth-first search (DFS) traversal on a graph represented by input lists `x` and `y`, and determines whether the graph contains a cycle. If the graph contains a cycle (i.e., `ok` is True), the program prints 'YES'. Otherwise, it prints 'NO'. The program maintains the original input values of `n`, `x`, `y`, and `r`, and updates the `visited`, `coef0`, `coef1`, and `nodes` lists based on the DFS traversal. The `ok` variable is set to True if at least one node has a non-zero coefficient, indicating a cycle, and False otherwise.

#Overall this is what the function does:This function determines whether a graph represented by input lists `x` and `y` contains a cycle. It performs a depth-first search (DFS) traversal on the graph, updating the `visited`, `coef0`, `coef1`, and `nodes` lists accordingly. If the graph contains a cycle, it prints 'YES'; otherwise, it prints 'NO'. The function maintains the original input values of `n`, `x`, `y`, and `r`, and updates the `ok` variable to indicate the presence or absence of a cycle.

#State of the program right berfore the function call: i is an integer such that 0 <= i < n, visited is a list of n boolean values, nodes is a list of integers, x and y are lists of n integers, r is a list of n positive integers, coef0 and coef1 are lists of n real numbers.
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
            
        #State: visited is a list of n boolean values where visited[j] is True for all j such that (r[i] + r[j])
    #State: *i is an integer such that 0 <= i < n, visited is a list of n boolean values, nodes is a list of integers, x and y are lists of n integers, r is a list of n positive integers, coef0 and coef1 are lists of n real numbers. If visited[i] is False, then visited is updated to a list of n boolean values where visited[j] is True for all j such that (r[i] + r[j]) <= coef0[j]*x[j] + coef1[j]*y[j]. Otherwise, no changes are made to the visited list.

#Overall this is what the function does:This function performs a depth-first search (DFS) on a graph defined by the input parameters. It takes an integer `i` and updates the `visited` list to mark all nodes `j` as visited if they are not already visited and satisfy the condition `(r[i] + r[j])

