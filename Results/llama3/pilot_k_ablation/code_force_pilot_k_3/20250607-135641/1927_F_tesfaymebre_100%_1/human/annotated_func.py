#State of the program right berfore the function call: stdin contains one input: an integer
    return int(sys.stdin.readline().strip())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it.

#State of the program right berfore the function call: stdin is an open file object connected to an input stream.
    return sys.stdin.readline().strip()
    #The program returns a string that is the next line from the input stream, with leading and trailing whitespace removed.

#Overall this is what the function does:Reads the next line from the standard input stream, removes leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers that were read from the standard input as space-separated integers.

#Overall this is what the function does:Reads a line of space-separated integers from the standard input and returns a map object containing these integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers that were read from the standard input, where each integer was separated by a space.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains a string of space-separated values
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a space-separated value from the input string in stdin.

#Overall this is what the function does:Reads a line of space-separated values from standard input and returns them as a list of strings, splitting the input string at each space character.

#State of the program right berfore the function call: n and m are positive integers, graph is a dictionary where each key is a node and its corresponding value is a list of its neighboring nodes, edges is a list of tuples where each tuple contains the weight of an edge and the two nodes it connects, and DSU is a disjoint set union data structure with n+1 elements.
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: n is a positive integer, m is greater than or equal to 0, graph contains m edges between nodes u and v, edges contains m tuples (w, u, v), DSU is a disjoint set union data structure with n+1 elements, i is m-1, u, v, and w are assigned values returned by func_3()
    edges.sort(reverse=True)
    dsu = DSU(n + 1)
    _min_edge = float('inf')
    start = -1
    end = -1
    for (w, u, v) in edges:
        parent_u = dsu.find(u)
        
        parent_v = dsu.find(v)
        
        if parent_u == parent_v:
            _min_edge = w
            start = u
            end = v
        else:
            dsu.union(u, v)
        
    #State: n is a positive integer, m is 0, graph contains 0 edges between nodes u and v, edges is an empty list, DSU is a disjoint set union data structure with n+1 elements, i is -1, u, v, and w are assigned values returned by func_3(), dsu is a disjoint set union data structure with n+1 elements where all nodes are in the same set, parent_u is the parent of u in the dsu data structure which is the same as parent_v, _min_edge is the minimum edge weight, start is the node with the minimum edge weight, end is the node with the minimum edge weight.
    que = deque([start])
    prev = {start: -1}
    while que:
        node = que.popleft()
        
        if node == end:
            break
        
        for nei in graph[node]:
            if node == start and nei == end:
                continue
            if nei not in prev:
                prev[nei] = node
                que.append(nei)
        
    #State: Output State: `n` is a positive integer, `m` is 0, `graph` contains all edges connected to `node`, `edges` is an empty list, `DSU` is a disjoint set union data structure with `n+1` elements, `i` is -1, `u`, `v`, and `w` are assigned values returned by `func_3()`, `dsu` is a disjoint set union data structure with `n+1` elements where all nodes are in the same set, `parent_u` is the parent of `u` in the `dsu` data structure which is the same as `parent_v`, `_min_edge` is the minimum edge weight, `start` is the node with the minimum edge weight, `end` is the node with the minimum edge weight, `que` is an empty deque, `prev` is a dictionary with `start` node mapped to -1 and all neighbors of `node` mapped to `node`, and `node` is `end`.
    #
    #In natural language, the output state after the loop executes all the iterations is that the loop has finished exploring all nodes in the graph, and the `que` deque is empty. The `prev` dictionary contains the parent node for each node in the graph, and the `node` variable is set to the `end` node. All other variables remain unchanged.
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        
        curr = prev[curr]
        
    #State: path is a list containing all nodes in the path from end to start, and curr is -1.
    print(_min_edge, len(path))
    #This is printed: _min_edge (the minimum edge value in the path), len(path) (the number of nodes in the path from end to start)
    print(*path[::-1])
    #This is printed: the nodes in the path from start to end (where the nodes are the elements of the path list in reverse order)

#Overall this is what the function does:This function takes no input parameters and returns no output parameters. It performs the following actions:

#State of the program right berfore the function call: test_cases is a positive integer.
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is greater than or equal to 0, and the function `func_6()` has been executed `test_cases` times, and `_` is `test_cases - 1`.

#Overall this is what the function does:Executes the function `func_6()` a number of times equal to the value returned by `func_1()`, which is a non-negative integer.

