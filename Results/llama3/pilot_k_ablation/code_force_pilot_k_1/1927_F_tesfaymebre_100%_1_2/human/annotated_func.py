#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(sys.stdin.readline().strip())
    #The program returns an integer that was provided as input through stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it.

#State of the program right berfore the function call: The function func_2() reads a line from the standard input and returns it as a string, stripped of leading and trailing whitespace.
    return sys.stdin.readline().strip()
    #The program returns a string that is read from the standard input, stripped of leading and trailing whitespace.

#Overall this is what the function does:Reads a line from the standard input, removes leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: stdin contains a line of space-separated integers
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers, where each integer is a space-separated value from the line of input read from stdin.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns a map object containing these integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers that were read from the standard input, where each integer was separated by a space.

#Overall this is what the function does:Reads a line of space-separated integers from the standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains a string of space-separated values of any type and value
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of values of any type and value that were in the input string, split by spaces.

#Overall this is what the function does:Reads a line of input from standard input, splits it into a list of values separated by spaces, and returns the list. The list can contain values of any type and value that were present in the input string.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5). The function func_3() returns a tuple of two integers. The function func_3() returns a tuple of three integers. The class DSU is defined and has methods find() and union(). The graph is undirected and weighted, and there is at most one edge between each pair of vertices. The graph does not contain loops (edges from a vertex to itself).
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), graph is a defaultdict of lists representing an undirected and weighted graph with m edges, edges is a list of m edges, each edge represented as a tuple of (weight, vertex1, vertex2), i is m-1, u and v are the last two vertices added to the graph, w is the weight of the last edge added to the graph.
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
        
    #State: n is an integer such that 3 <= n <= m, m is an integer such that n <= m <= min(n*(n-1)/2, 2*10^5), graph is a defaultdict of lists representing an undirected and weighted graph with m edges, edges is an empty list, i is -1, u and v are the last two vertices added to the graph, w is the weight of the last edge added to the graph, dsu is a DSU object with n+1 elements where all elements are in the same set, _min_edge is the weight of the first edge that caused a cycle in the graph, start is the first vertex of the first edge that caused a cycle in the graph, and end is the second vertex of the first edge that caused a cycle in the graph. If no cycle is found, _min_edge is positive infinity, start is -1, and end is -1.
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
        
    #State: `n` is an integer such that 3 <= n <= m, `m` is an integer such that n <= m <= min(n*(n-1)/2, 2*10^5), `graph` is a defaultdict of lists representing an undirected and weighted graph with m edges, `edges` is an empty list, `i` is -1, `u` and `v` are the last two vertices added to the graph, `w` is the weight of the last edge added to the graph, `dsu` is a DSU object with n+1 elements where all elements are in the same set, `_min_edge` is the weight of the first edge that caused a cycle in the graph, `start` is the first vertex of the first edge that caused a cycle in the graph, `end` is the second vertex of the first edge that caused a cycle in the graph, `que` is an empty deque, `prev` is a dictionary mapping each vertex reachable from `start` (excluding `end`) to its previous vertex in the path from `start` to `end` (if a cycle was found), or `prev` is a dictionary with -1 mapped to -1 (if no cycle was found), `node` is `end`.
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        
        curr = prev[curr]
        
    #State: n is an integer such that 3 <= n <= m, m is an integer such that n <= m <= min(n*(n-1)/2, 2*10^5), graph is a defaultdict of lists representing an undirected and weighted graph with m edges, edges is an empty list, i is -1, u and v are the last two vertices added to the graph, w is the weight of the last edge added to the graph, dsu is a DSU object with n+1 elements where all elements are in the same set, _min_edge is the weight of the first edge that caused a cycle in the graph, start is the first vertex of the first edge that caused a cycle in the graph, end must not be -1, que is an empty deque, prev is a dictionary mapping each vertex reachable from start (excluding end) to its previous vertex in the path from start to end (if a cycle was found), or prev is a dictionary with -1 mapped to -1 (if no cycle was found), node is end, path is a list containing all vertices in the path from start to end in reverse order, curr is -1.
    print(_min_edge, len(path))
    #This is printed: _min_edge (the weight of the first edge that caused a cycle in the graph), len(path) (the length of the path from the start vertex to the end vertex)
    print(*path[::-1])
    #This is printed: the vertices in the path from start to end in reverse order (excluding the last vertex (end)), and the weight of the first edge that caused a cycle in the graph (_min_edge)

#Overall this is what the function does:This function constructs an undirected and weighted graph with a specified number of vertices and edges, detects the first edge that causes a cycle in the graph, and prints the weight of this edge and the length of the path from the start vertex to the end vertex. If a cycle is found, it also prints the vertices in the path from the start vertex to the end vertex. If no cycle is found, it prints the weight of the first edge that would cause a cycle (positive infinity) and the length of the path (which is undefined in this case).

#State of the program right berfore the function call: test_cases is a positive integer.
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is the return value of `func_1()`, `_` is `test_cases - 1`, and the function `func_6()` has been executed `test_cases` times. If `test_cases` is 0, the loop does not execute and the function `func_6()` is not executed at all.

#Overall this is what the function does:Executes the function `func_6()` a number of times equal to the return value of `func_1()`, which is a positive integer. If `func_1()` returns 0, the function `func_6()` is not executed at all.

