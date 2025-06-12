#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(sys.stdin.readline().strip())
    #The program returns an integer that was provided as input through stdin.

#Overall this is what the function does:The function reads an integer from standard input (stdin) and returns it as an integer value.

#State of the program right berfore the function call: No precondition can be extracted from this function as it does not have any parameters.
    return sys.stdin.readline().strip()
    #The program returns a string that is the first line of input from standard input, with leading and trailing whitespace removed.

#Overall this is what the function does:Reads and returns the first line of input from standard input, removing leading and trailing whitespace.

#State of the program right berfore the function call: stdin contains a line of space-separated integers
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object that contains integers, which are the result of converting the space-separated integers from the input line in stdin.

#Overall this is what the function does:Reads a line of space-separated integers from standard input, converts them to integers, and returns a map object containing the converted integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers that were read from the standard input, where each integer was separated by a space.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin is a stream of input containing a string of space-separated values
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings where each string is a space-separated value from the input stream stdin.

#Overall this is what the function does:Reads a line of input from the standard input stream, splits it into space-separated values, and returns them as a list of strings.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), graph is a dictionary where each key is a vertex and its corresponding value is a list of its neighboring vertices, edges is a list of tuples where each tuple contains the weight of an edge and the two vertices it connects.
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), graph is a dictionary with m pairs of nodes, edges is a list of m tuples (w, u, v).
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
        
    #State: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), graph is a dictionary with m pairs of nodes, edges is an empty list, dsu is a DSU object initialized with n + 1 elements where all nodes are in the same set, _min_edge is the weight of the minimum edge that connects two nodes that were initially in the same set, start and end are the nodes connected by the minimum edge. If no such edge exists, _min_edge is positive infinity, start is -1, end is -1.
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
        
    #State: `n` and `m` are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), `graph` is a dictionary with m pairs of nodes, `edges` is an empty list, `dsu` is a DSU object initialized with n + 1 elements where all nodes are in the same set, `_min_edge` is the weight of the minimum edge that connects two nodes that were initially in the same set, `start` and `end` are the nodes connected by the minimum edge and `start` is not -1, `que` is an empty deque, `prev` is a dictionary mapping each node reachable from `start` (excluding `end`) to its previous node in the path from `start` to `end`.
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        
        curr = prev[curr]
        
    #State: n is an integer, m is an integer, graph is a dictionary with m pairs of nodes, edges is an empty list, dsu is a DSU object initialized with n + 1 elements where all nodes are in the same set, _min_edge is the weight of the minimum edge that connects two nodes that were initially in the same set, start is a node, end is a node, que is an empty deque, prev is a dictionary mapping each node reachable from start (excluding end) to its previous node in the path from start to end, path is a list containing all nodes in the path from start to end in reverse order, curr is -1
    print(_min_edge, len(path))
    #This is printed: _min_edge (the weight of the minimum edge that connects two nodes that were initially in the same set), len(path) (the number of nodes in the path from start to end in reverse order)
    print(*path[::-1])
    #This is printed: the nodes in the path from start to end in the correct order, excluding the end node (where the path is obtained by reversing the list of nodes in the path from start to end)

#Overall this is what the function does:This function takes no parameters and returns no values. It constructs a graph with n nodes and m edges, where n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), and each edge has a weight. The function then finds the minimum edge that connects two nodes that were initially in the same set, and if such an edge exists, it prints the weight of this edge and the number of nodes in the path from the start node to the end node in reverse order. Finally, it prints the nodes in the path from the start node to the end node in the correct order, excluding the end node. If no such edge exists, it prints positive infinity as the weight and -1 as the start and end nodes.

#State of the program right berfore the function call: No precondition can be extracted from this function as it does not have any parameters.
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is assigned the value returned by `func_1()`, the function `func_6` has been executed `test_cases` times.

#Overall this is what the function does:Executes the function `func_6` a number of times determined by the return value of `func_1`, without modifying or returning any values.

