#State of the program right berfore the function call: stdin contains one input: an integer
    return int(sys.stdin.readline().strip())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it.

#State of the program right berfore the function call: stdin contains a string
    return sys.stdin.readline().strip()
    #The program returns a string that was read from the standard input (stdin) with leading and trailing whitespace removed.

#Overall this is what the function does:Reads a line of input from the standard input (stdin), removes leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers that were read from the standard input as a line of space-separated integers.

#Overall this is what the function does:Reads a line of space-separated integers from the standard input and returns a map object containing these integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers that were read from the standard input, where each integer was separated by a space.

#Overall this is what the function does:Reads a line of space-separated integers from the standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains one input: a string of space-separated values
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings where each string is a space-separated value from the input string in stdin.

#Overall this is what the function does:Reads a line of input from stdin, splits it into space-separated values, and returns them as a list of strings.

#State of the program right berfore the function call: n and m are positive integers, and the function func_3() returns a tuple of two positive integers, and the function DSU() is a class that implements the disjoint-set data structure.
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: n is a positive integer, m is a positive integer greater than or equal to m, i is m-1, graph is a dictionary with m keys, each containing a list with m-1 keys, edges is a list containing m tuples (w, u, v) where w, u, and v are the values returned by func_3(), and the function DSU() remains unchanged.
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
        
    #State: n is a positive integer, m is a positive integer greater than or equal to n, i is m-1, graph is a dictionary with m keys, each containing a list with m-1 keys, edges is an empty list, dsu is an instance of the DSU class with n+1 as the input. If the parent of u and the parent of v in the dsu are the same, then _min_edge is w, start is u, and end is v. Otherwise, u and v are now in the same set in the dsu, and _min_edge, start, and end are either updated or remain the same as their previous values.
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
        
    #State: Output State: `n` is a positive integer, `m` is a positive integer greater than or equal to `n`, `i` is `m`, `graph` is a dictionary with `m` keys, each containing a list with at least `m` keys that must have at least `m` neighbors for the node, `edges` is an empty list, `dsu` is an instance of the DSU class with `n+1` as the input, `que` is empty, `prev` is a dictionary with `m` elements, `node` is `end`, and `nei` is the last neighbor in the list.
    #
    #In natural language, the output state after the loop executes all the iterations is that the queue is empty, and the `prev` dictionary contains all the nodes in the graph as keys, with their corresponding previous nodes as values. The `node` variable is set to the `end` node, and the `nei` variable is set to the last neighbor of the `end` node. The other variables remain unchanged.
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        
        curr = prev[curr]
        
    #State: Output State: n is a positive integer, m is a positive integer greater than or equal to n, i is m, graph is a dictionary with m keys, each containing a list with at least m keys that must have at least m neighbors for the node, edges is an empty list, dsu is an instance of the DSU class with n+1 as the input, que is empty, prev is a dictionary with m elements, node is end, and nei is the last neighbor in the list, path is a list containing all the values of curr from the start to the end of the loop, and curr is -1.
    #
    #In natural language, the output state after the loop executes all the iterations is that the path list contains all the values of curr from the start to the end of the loop, and curr is -1, indicating that the loop has finished executing. The other variables remain unchanged.
    print(_min_edge, len(path))
    #This is printed: the minimum edge and the length of the path (where the minimum edge is the minimum edge in the graph and the length of the path is the number of nodes in the path)
    print(*path[::-1])
    #This is printed: the elements of the path list in reverse order, starting from -1

#Overall this is what the function does:This function constructs a graph from a set of edges, finds the minimum edge in the graph, and then finds the shortest path between the two nodes connected by the minimum edge. It prints the weight of the minimum edge and the length of the shortest path, followed by the nodes in the shortest path in reverse order.

#State of the program right berfore the function call: test_cases is a positive integer
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is a value returned by `func_1()` that must be greater than or equal to the number of iterations and `func_6()` has been executed the same number of times as the number of iterations.

#Overall this is what the function does:Executes a loop a number of times equal to the value returned by `func_1()`, calling `func_6()` in each iteration.

