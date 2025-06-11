#State of the program right berfore the function call: stdin contains one input: an integer
    return int(sys.stdin.readline().strip())
    #The program returns an integer that was provided as input through stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it.

#State of the program right berfore the function call: stdin contains one input: a string
    return sys.stdin.readline().strip()
    #The program returns a string that was provided as input from stdin, with any leading or trailing whitespace removed.

#Overall this is what the function does:Reads a string from standard input, removes any leading or trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object that contains integers from the line of space-separated integers in stdin.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns a map object containing these integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers that were provided as input through stdin, where each integer was separated by a space.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains one input: a string of space-separated values
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a value from the input string of space-separated values.

#Overall this is what the function does:Reads a line of space-separated values from standard input and returns them as a list of strings, where each string is a value from the input.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5).
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: n is an integer such that 3 <= n <= m, m is an integer greater than or equal to n, m is less than or equal to min(n*(n-1)/2, 2*10^5), graph is a dictionary with two keys, u and v, each containing a list with the other key and the value returned by func_3 for u or v, and m-1 additional elements in each list, edges is a list containing m tuples (w, u, v) where w, u, and v are the values returned by func_3, i is m-1.
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
        
    #State: n is an integer such that 3 <= n <= m, m is an integer greater than or equal to n, m is less than or equal to min(n*(n-1)/2, 2*10^5), graph is a dictionary with two keys, u and v, each containing a list with the other key and the value returned by func_3 for u or v, and m-1 additional elements in each list, edges is an empty list, i is -1, dsu is a DSU object where all nodes are merged into a single set, node_u is u, node_v is v, and _min_edge is the minimum edge of the set containing u and v in the DSU.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: the minimum edge of the set containing u and v in the DSU, the length of the result of the dfs function call with arguments node_u, -1, and an empty list
    print(*res)
    #This is printed: the result of the dfs function call with arguments u, -1, and an empty list

#Overall this is what the function does:This function generates a graph with n nodes and m edges, where n and m are integers within certain bounds, and then finds the minimum edge in the graph using a disjoint set union (DSU) data structure. It then performs a depth-first search (DFS) from the node connected by the minimum edge and prints the minimum edge value and the length of the DFS result. Finally, it prints the DFS result.

#State of the program right berfore the function call: curr is a non-negative integer, parent is a non-negative integer, path is a list of non-negative integers, graph is a dictionary where each key is a non-negative integer and each value is a list of non-negative integers, colors is a list of integers with the same length as the number of vertices in the graph, and node_v is a non-negative integer.
    if (colors[curr] == 1) :
        return path
        #The program returns a list of non-negative integers representing the path, which includes the current node 'curr' with a color of 1, and other nodes that are connected to 'curr' through the graph, with their respective colors.
    #State: *curr is a non-negative integer, parent is a non-negative integer, path is a list of non-negative integers, graph is a dictionary where each key is a non-negative integer and each value is a list of non-negative integers, colors is a list of integers with the same length as the number of vertices in the graph, and node_v is a non-negative integer. The color of the current node (colors[curr]) is not equal to 1
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: curr is a non-negative integer, parent is a non-negative integer, path is a list of non-negative integers that includes the current node (curr), graph is a dictionary where each key is a non-negative integer and each value is a list of non-negative integers, colors is a list of integers with the same length as the number of vertices in the graph where the color of the current node (colors[curr]) is 1, node_v is a non-negative integer, nei is the last neighbor in the list, res is a list of integers, set_res is a set of integers. If colors[nei] is not equal to 2 and nei is not equal to parent, then the list res is empty or node_v is not in set_res. Otherwise, the state of the variables remains unchanged.
    colors[curr] = 2
    return []
    #The program returns an empty list.

#Overall this is what the function does:This function performs a depth-first search (DFS) on a graph to find a path that includes a specific node (node_v) and returns the path if found. The function takes as input the current node (curr), its parent node (parent), the current path, the graph, a list of colors representing the state of each node, and the target node (node_v). The function returns a list of non-negative integers representing the path if the target node is found, otherwise it returns an empty list. The function also updates the colors of the nodes it visits, marking them as visited (color 1) or fully explored (color 2).

#State of the program right berfore the function call: No specific precondition can be determined for the variables in the function signature as the function does not take any parameters. However, based on the problem description, it can be inferred that the function is part of a larger program that reads input from the user and processes it to find a simple cycle in a graph.
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is greater than or equal to the number of iterations of the loop, and the function `func_6()` has been executed the same number of times as the number of iterations of the loop, `_` is `test_cases - 1`.

#Overall this is what the function does:Executes a specified number of test cases by calling another function (`func_6`) for each test case, where the number of test cases is determined by the return value of `func_1`.

