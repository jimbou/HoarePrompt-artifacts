#State of the program right berfore the function call: stdin contains one input: an integer
    return int(sys.stdin.readline().strip())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it.

#State of the program right berfore the function call: stdin contains a string that needs to be read and stripped of leading and trailing whitespaces.
    return sys.stdin.readline().strip()
    #The program returns a string that was read from stdin and stripped of leading and trailing whitespaces.

#Overall this is what the function does:Reads a string from standard input, removes leading and trailing whitespaces, and returns the resulting string.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a value from the line of space-separated integers read from stdin.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers, where each integer is a value from the space-separated list of integers provided as input to stdin.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns a list of integers, where each integer is a value from the input list.

#State of the program right berfore the function call: stdin contains a line of text that can be split into a list of values
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of values that were read from the standard input (stdin) and split into separate elements, with any leading or trailing whitespace removed from each element.

#Overall this is what the function does:Reads a line of text from standard input, splits it into a list of values, removes leading and trailing whitespace from each value, and returns the resulting list.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), graph is a dictionary representing an undirected weighted graph with n vertices and m edges, edges is a list of tuples representing the edges of the graph, where each tuple contains the weight and the two vertices of the edge, dsu is an instance of the DSU class representing a disjoint-set data structure, _min_edge is a float representing the minimum edge weight, node_u and node_v are integers representing the vertices of the minimum edge, colors is a list of integers representing the colors of the vertices, and res is a list of integers representing the result of the depth-first search.
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: n is an integer such that 3 <= n <= m, m is an integer such that n <= m <= min(n*(n-1)/2, 2*10^5) and m is at least m, i is m-1, graph is a dictionary with 2*m edges (u, v) and (v, u), edges is a list containing m tuples (w, u, v), dsu is an instance of the DSU class representing a disjoint-set data structure, _min_edge is a float representing the minimum edge weight, node_u and node_v are integers representing the vertices of the minimum edge, colors is a list of integers representing the colors of the vertices, and res is a list of integers representing the result of the depth-first search.
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
        
    #State: n is an integer such that 3 <= n <= m, m is an integer such that n <= m <= min(n*(n-1)/2, 2*10^5) and m is at least m, i is m-1, graph is a dictionary with 2*m edges (u, v) and (v, u), edges is an empty list, dsu is an instance of the DSU class representing a disjoint-set data structure with n+1 elements, _min_edge is a float representing the minimum edge weight, node_u and node_v are integers representing the vertices of the minimum edge, colors is a list of integers representing the colors of the vertices, and res is a list of integers representing the result of the depth-first search.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: the minimum edge weight, the number of nodes visited in the depth-first search starting from node_u
    print(*res)
    #This is printed: [node_u, ..., node_v] (where node_u and node_v are the vertices of the minimum edge and ... represents the nodes visited during the depth-first search)

#Overall this is what the function does:This function takes no arguments and returns no values. It constructs an undirected weighted graph with n vertices and m edges, finds the minimum edge weight, and performs a depth-first search starting from one of the vertices of the minimum edge. The function then prints the minimum edge weight and the number of nodes visited during the depth-first search, followed by the nodes visited in the depth-first search.

#State of the program right berfore the function call: curr is a node in the graph, parent is the parent node of curr in the current DFS path, path is the current DFS path, colors is a list of colors (0, 1, or 2) for each node in the graph, graph is an adjacency list representation of the graph, and node_v is a node in the graph.
    if (colors[curr] == 1) :
        return path
        #The program returns the current DFS path, which includes the current node 'curr' with color 1, its parent node 'parent', and all other nodes in the current DFS path, as well as the adjacency list representation of the graph and the node 'node_v' in the graph.
    #State: *curr is a node in the graph, parent is the parent node of curr in the current DFS path, path is the current DFS path, colors is a list of colors (0, 1, or 2) for each node in the graph, graph is an adjacency list representation of the graph, and node_v is a node in the graph. The color of the current node (curr) is not 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: Output State: *`curr` is a node in the graph, `parent` is the parent node of `curr` in the current DFS path, `path` is the current DFS path with `curr` appended, `colors` is a list of colors (0, 1, or 2) for each node in the graph with the color of `curr` changed to 1, `graph` is an adjacency list representation of the graph, and `node_v` is a node in the graph. If there exists a neighbor `nei` of `curr` such that `nei` is not the parent of `curr` and the color of `nei` is not 2, then the program returns the result of the DFS traversal starting from `nei` with `curr` as the parent, where `nei` is the last neighbor of `curr` in the list `graph[curr]` and the result of the DFS traversal contains `node_v`. Otherwise, the program does not return anything.*
    #
    #In natural language, the output state after the loop executes all the iterations is that the program has traversed all the neighbors of the current node `curr` in the graph, and if any of these neighbors have a color that is not 2 and are not the parent of `curr`, the program returns the result of the DFS traversal starting from that neighbor with `curr` as the parent, where the result contains the node `node_v`. If no such neighbor is found, the program does not return anything.
    colors[curr] = 2
    return []
    #The program returns an empty list

#Overall this is what the function does:This function performs a Depth-First Search (DFS) traversal in a graph, starting from a given node 'curr', with the goal of finding a path that includes a specific node 'node_v'. The function takes as input the current node 'curr', its parent node 'parent', the current DFS path, a list of colors for each node in the graph, the graph itself represented as an adjacency list, and the target node 'node_v'. The function returns the DFS path that includes 'node_v' if found, otherwise it returns an empty list. The function also updates the colors of the nodes in the graph during the traversal, marking visited nodes with color 1 and fully explored nodes with color 2.

#State of the program right berfore the function call: test_cases is a non-negative integer
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is a returned value of `func_1()` that must be greater than or equal to 0, `_` is `test_cases - 1`, and the function `func_6()` has been executed `test_cases` times.

#Overall this is what the function does:Executes the function `func_6()` a number of times equal to the non-negative value returned by `func_1()`.

