#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(sys.stdin.readline().strip())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it.

#State of the program right berfore the function call: stdin contains one input: a string
    return sys.stdin.readline().strip()
    #The program returns a string that was provided as input from stdin, with any leading or trailing whitespace removed.

#Overall this is what the function does:Reads a string from standard input, removes any leading or trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a value from the input line of space-separated integers read from stdin.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers that were read from the standard input, where each integer was separated by a space.

#Overall this is what the function does:Reads a line of space-separated integers from the standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains a string of space-separated values
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a space-separated value from the input string in stdin.

#Overall this is what the function does:Reads a line of space-separated values from standard input and returns them as a list of strings, splitting the input string into individual values based on spaces.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5). The function func_3() returns a tuple of two integers, and the function DSU(n+1) returns a DSU object. The graph is an undirected weighted graph with n vertices and m edges, and there is at most one edge between each pair of vertices. The graph does not contain loops (edges from a vertex to itself). The graph is not necessarily connected.
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: Output State: The graph is a defaultdict of lists where each key is a node and its corresponding value is a list of its neighbors, edges is a list of tuples where each tuple contains the weight and the two nodes of an edge, and the other variables remain unchanged.
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
        
    #State: Output State: The graph remains unchanged, edges is an empty list, dsu is a DSU object where all elements are in the same set, _min_edge is the weight of the minimum edge in the graph, start and end are the two nodes of the minimum edge, and the other variables remain unchanged.
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
        
    #State: The loop ends with que being an empty list, prev being a dictionary containing all nodes in the graph except the end node, each mapped to its previous node in the shortest path from the start node to itself, and the other variables remaining unchanged.
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        
        curr = prev[curr]
        
    #State: path contains the shortest path from the start node to the end node in reverse order, curr is -1, and que remains empty.
    print(_min_edge, len(path))
    #This is printed: _min_edge (the minimum edge weight or cost in the shortest path), len(path) (the number of nodes in the shortest path)
    print(*path[::-1])
    #This is printed: the shortest path from the start node to the end node

#Overall this is what the function does:This function constructs an undirected weighted graph from a given number of vertices and edges, finds the minimum-weight edge in the graph, and then prints the weight of this edge and the shortest path between the two nodes connected by this edge. The function also prints the nodes in the shortest path in the correct order.

#State of the program right berfore the function call: test_cases is a positive integer.
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: The output state is the return value of `func_6()` repeated `test_cases` times.

#Overall this is what the function does:Executes `func_6()` a specified number of times, equal to the return value of `func_1()`, and returns the repeated output of `func_6()`.

