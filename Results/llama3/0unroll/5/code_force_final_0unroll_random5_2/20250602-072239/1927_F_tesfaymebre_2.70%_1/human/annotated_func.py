#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(sys.stdin.readline().strip())
    #The program returns an integer that was provided as input through stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: stdin contains a string
    return sys.stdin.readline().strip()
    #The program returns the string from stdin with leading and trailing whitespace removed.

#Overall this is what the function does:Reads a line of input from standard input, removes leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a space-separated integer from the input line in stdin, and all integers are converted to int data type.

#Overall this is what the function does:Reads a line of space-separated integers from standard input, converts each integer to an integer data type, and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers that were read from the standard input, where each integer was separated by a space.

#Overall this is what the function does:Reads a line of space-separated integers from the standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains a string of space-separated values
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings where each string is a space-separated value from the input string in stdin.

#Overall this is what the function does:Reads a line of space-separated values from standard input and returns them as a list of strings, where each string is a value from the input line.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5). The function func_3() returns a tuple of two integers. The function func_3() returns a tuple of three integers. The function DSU(n+1) returns a DSU object with n+1 elements. The function dsu.find(x) returns the parent of node x. The function dsu.union(u, v, w) merges the sets containing u and v with weight w. The function dsu.min_edge[x] returns the minimum edge weight in the set containing x. The function dfs(u, parent, path) returns a list of nodes representing a path in the graph.
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: Output State: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), n and m are assigned new values returned by func_3(), graph is a dictionary where each key is a node and its corresponding value is a list of its neighbors, edges is a list of tuples where each tuple contains the weight and the two nodes of an edge.
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
        
    #State: Output State: The loop has iterated over all edges in the graph, and the DSU object has been updated accordingly. The minimum edge weight _min_edge has been updated to the minimum weight of all edges in the graph, and the nodes node_u and node_v have been updated to the nodes of the minimum edge. The DSU object dsu has been updated to reflect the union of all nodes in the graph. The variables n, m, graph, and edges remain unchanged.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: minimum edge weight of all edges in the graph, length of the list res
    print(*res)
    #This is printed: the elements of the result list res

#Overall this is what the function does:This function generates a graph with n nodes and m edges, finds the minimum edge weight in the graph, and performs a depth-first search (DFS) from the node with the minimum edge weight. It then prints the minimum edge weight, the length of the DFS path, and the nodes in the DFS path.

#State of the program right berfore the function call: curr and parent are non-negative integers such that 0 <= curr < len(graph) and 0 <= parent < len(graph), graph is a list of lists where each inner list contains non-negative integers, colors is a list of integers with the same length as graph, node_v is a non-negative integer, and path is a list of non-negative integers.
    if (colors[curr] == 1) :
        return path
        #The program returns the list of non-negative integers 'path'
    #State: *curr and parent are non-negative integers such that 0 <= curr < len(graph) and 0 <= parent < len(graph), graph is a list of lists where each inner list contains non-negative integers, colors is a list of integers with the same length as graph, node_v is a non-negative integer, and path is a list of non-negative integers. The color of the current node (colors[curr]) is not 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: The loop iterates over all neighbors (nei) of the current node (curr) in the graph. For each neighbor, it checks if the color of the neighbor is not 2 (i.e., it has not been visited before) and if the neighbor is not the parent of the current node. If both conditions are true, it calls the dfs function recursively with the neighbor as the new current node, the current node as the parent, and the updated path. The dfs function returns a list of nodes (res) and the loop checks if the list is not empty and if the node_v is in the set of nodes returned by dfs. If both conditions are true, the loop returns the list of nodes returned by dfs. If the loop iterates over all neighbors without finding a path that includes node_v, it does not return anything. The state of the other variables (graph, colors, node_v, and path) remains unchanged.
    colors[curr] = 2
    return []
    #The program returns an empty list. The loop has iterated over all neighbors of the current node without finding a path that includes node_v. The state of the other variables (graph, colors, node_v, and path) remains unchanged, but the color of the current node (curr) is now 2, indicating that it has been visited.

#Overall this is what the function does:This function performs a depth-first search (DFS) in a graph to find a path that includes a specific node (node_v). It accepts as input the current node (curr), its parent node (parent), the graph represented as a list of lists, a list of colors to keep track of visited nodes, the target node (node_v), and the current path. The function returns a list of nodes representing the path that includes node_v if found, or an empty list if no such path exists. The function modifies the colors list to mark visited nodes and updates the path as it traverses the graph.

#State of the program right berfore the function call: No specific precondition can be derived from the given function signature as it does not contain any parameters.
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is returned by `func_1()` and `func_6()` has been executed `test_cases` times.

#Overall this is what the function does:Executes `func_6()` a number of times determined by the return value of `func_1()`, without modifying or returning any values.

