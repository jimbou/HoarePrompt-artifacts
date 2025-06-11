#State of the program right berfore the function call: stdin contains one input: an integer
    return int(sys.stdin.readline().strip())
    #The program returns an integer that was provided as input through stdin.

#Overall this is what the function does:The function reads an integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: stdin is a file object that contains a string that can be stripped and returned.
    return sys.stdin.readline().strip()
    #The program returns a string that was read from the file object stdin and stripped of leading and trailing whitespace.

#Overall this is what the function does:Reads a line from the standard input (stdin) and returns the string after removing leading and trailing whitespace.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a space-separated integer from the line in stdin, and each integer has been converted from a string to an integer using the int() function.

#Overall this is what the function does:Reads a line of space-separated integers from standard input, converts each integer from a string to an integer, and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers, where each integer is a space-separated integer from the input line in stdin.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains a line of input: a string of space-separated values
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a space-separated value from the input line in stdin.

#Overall this is what the function does:Reads a line of input from stdin, splits it into space-separated values, and returns them as a list of strings.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), and the graph represented by the edges in the input is an undirected weighted graph with n vertices and m edges, where each edge has a weight between 1 and 10^6, and there is at most one edge between each pair of vertices, and the graph does not contain loops (edges from a vertex to itself).
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), graph is a dictionary with m number of edges where each edge is represented as a key-value pair with the key being a node and the value being a list of its adjacent nodes, edges is a list of m tuples, each tuple containing the weight and the two nodes of an edge.
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
        
    #State: n is an integer such that 3 <= n <= m, m is an integer such that n <= m <= min(n*(n-1)/2, 2*10^5), graph is a dictionary with m number of edges, edges is an empty list, dsu is a DSU object initialized with n + 1 elements where all elements are in the same set, _min_edge is the minimum weight of an edge in the graph, start and end are the nodes of the minimum weight edge. If the graph is empty, _min_edge is positive infinity, start is -1, and end is -1.
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
        
    #State: `n` is an integer such that 3 <= n <= m, `m` is an integer such that n <= m <= min(n*(n-1)/2, 2*10^5), `graph` is a dictionary with m number of edges, `edges` is an empty list, `dsu` is a DSU object initialized with n + 1 elements where all elements are in the same set, `_min_edge` is the minimum weight of an edge in the graph, `que` is an empty deque, `prev` is a dictionary with all nodes except the end node mapped to their respective parent nodes in the shortest path from the start node to the end node, `start` and `end` are the nodes of the minimum weight edge. If the graph is empty, _min_edge is positive infinity, start is -1, and end is -1. If there is no path from the start node to the end node, prev will not contain the end node.
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        
        curr = prev[curr]
        
    #State: `path` contains the shortest path from the start node to the end node in reverse order, `curr` is -1
    print(_min_edge, len(path))
    #This is printed: _min_edge (the minimum edge weight in the shortest path), len(path) (the number of nodes in the shortest path)
    print(*path[::-1])
    #This is printed: the nodes in the shortest path from the start node to the end node in the correct order

#Overall this is what the function does:This function takes no parameters and returns the minimum weight of an edge in the shortest path between two nodes in a weighted undirected graph, the number of nodes in this path, and the nodes in the path from start to end. If the graph is empty, it returns positive infinity as the minimum weight and -1 as the start and end nodes. If there is no path from the start node to the end node, it only returns the minimum weight and the number of nodes in the path (which will be 1).

#State of the program right berfore the function call: test_cases is a non-negative integer.
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is the value returned by `func_1()`, `func_6()` has been executed `test_cases` times.

#Overall this is what the function does:Executes a specified number of test cases by calling `func_6()` a number of times equal to the value returned by `func_1()`, without modifying the input variables.

