#State of the program right berfore the function call: stdin contains one input: an integer
    return int(sys.stdin.readline().strip())
    #The program returns an integer that was provided as input through stdin.

#Overall this is what the function does:The function reads an integer from standard input (stdin) and returns it as an integer value.

#State of the program right berfore the function call: stdin is a file object that contains a string.
    return sys.stdin.readline().strip()
    #The program returns a string that was read from the file object stdin, with leading and trailing whitespace removed.

#Overall this is what the function does:Reads a line of input from the standard input (stdin) and returns the input string with leading and trailing whitespace removed.

#State of the program right berfore the function call: stdin contains a line of space-separated integers
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a value from the line of space-separated integers in stdin, converted to an integer type.

#Overall this is what the function does:Reads a line of space-separated integers from standard input, converts each integer to an integer type, and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers that were read from the standard input, where each integer was separated by a space.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains a line of input: a string of space-separated values
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings where each string is a space-separated value from the input line in stdin.

#Overall this is what the function does:Reads a line of input from stdin, splits it into space-separated values, and returns them as a list of strings.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5).
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: Output State: n is an integer, graph is a dictionary where each key has a list of its adjacent nodes, edges is a list of tuples containing the weight and the two nodes of each edge.
    edges.sort(reverse=True)
    dsu = DSU(n + 1)
    _min_edge = float('inf')
    node_u = -1
    node_v = -1
    for (w, u, v) in edges:
        parent_u = dsu.find(u)
        
        parent_v = dsu.find(v)
        
        if parent_u == parent_v:
            dsu.union(u, v, w)
            if dsu.min_edge[parent_u] < _min_edge:
                _min_edge = dsu.min_edge[parent_u]
                node_u = u
                node_v = v
        else:
            dsu.union(u, v, w)
        
    #State: Output State: The loop has iterated over all edges in the graph, and the DSU object has been updated accordingly. The minimum edge weight _min_edge has been updated to the minimum weight of all edges in the graph, and the nodes node_u and node_v have been updated to the nodes of the minimum edge. The DSU object dsu has been updated to reflect the connected components of the graph after considering all edges. The variables n, graph, and edges remain unchanged.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: minimum edge weight of the graph, number of nodes visited during the DFS traversal starting from node_u
    print(*res)
    #This is printed: the nodes in the cycle of the graph starting from node_u (where node_u is the node of the minimum edge)

#Overall this is what the function does:This function generates a graph with n nodes and m edges, sorts the edges in descending order of their weights, and then iterates over the sorted edges to find the minimum edge weight and the nodes connected by this edge. It uses a disjoint-set data structure (DSU) to keep track of the connected components of the graph. After finding the minimum edge, it performs a depth-first search (DFS) traversal starting from one of the nodes of the minimum edge and prints the minimum edge weight, the number of nodes visited during the DFS traversal, and the nodes in the cycle of the graph starting from the node of the minimum edge.

#State of the program right berfore the function call: curr is a non-negative integer, parent is a non-negative integer, path is a list of non-negative integers, colors is a list of integers with the same length as the number of vertices in the graph, graph is a list of lists of non-negative integers representing the adjacency list of the graph, and node_v is a non-negative integer representing a vertex in the graph.
    if (colors[curr] == 1) :
        return path
        #The program returns a list of non-negative integers representing the path, which includes the current vertex 'curr' with a color of 1, and all the vertices in the path from the root to the current vertex 'curr' in the graph.
    #State: *curr is a non-negative integer, parent is a non-negative integer, path is a list of non-negative integers, colors is a list of integers with the same length as the number of vertices in the graph, graph is a list of lists of non-negative integers representing the adjacency list of the graph, and node_v is a non-negative integer representing a vertex in the graph. The color of the current node (colors[curr]) is not equal to 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: Output State: colors[curr] is 2, path contains the original list of non-negative integers plus the value of curr appended at the end, all other variables remain unchanged.
    colors[curr] = 2
    return []
    #The program returns an empty list.

#Overall this is what the function does:This function performs a depth-first search (DFS) in a graph, starting from a given vertex 'curr', and returns a list of vertices representing the path from the root to the current vertex 'curr' if the color of 'curr' is 1, or an empty list if no such path is found. The function also updates the colors of visited vertices to 1 (for the current vertex) and 2 (for vertices that have been fully explored).

#State of the program right berfore the function call: test_cases is a non-negative integer
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: The state of the program after the loop has finished executing is that the function `func_6()` has been called `test_cases` times, where `test_cases` is the value returned by `func_1()`. The state of the other variables in the program remains unchanged.

#Overall this is what the function does:Executes the function `func_6()` a number of times equal to the value returned by `func_1()`, without modifying any other variables in the program.

