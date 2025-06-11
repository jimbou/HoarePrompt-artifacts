#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer between 2 and 2*10^5 inclusive and t is 1, then n-1 lines each containing two integers between 1 and n inclusive, and finally one integer between 1 and n inclusive.
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: The variable t remains 1, the variable edges remains an empty list, the variable empty remains True, the variable nodes is a dictionary where each key is an integer between 1 and n inclusive, and each value is a list of integers between 1 and n inclusive, representing the adjacency list of a graph with n vertices and n-1 edges, and the variable stdin is empty.
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: Output State: The variable t remains 1, the variable edges remains an empty list, the variable empty remains True, the variable nodes is a dictionary where each key is an integer between 1 and n inclusive, and each value is a list of integers between 1 and n inclusive, representing the adjacency list of a graph with n vertices and n-1 edges, the variable ends is a list of integers between 1 and n inclusive, representing the nodes with degree 1 in the graph, and the variable stdin is empty.
    s, e = list(ends)
    tree = [s]
    prev = s
    curr = nodes[s][0]
    while curr != e:
        tree.append(curr)
        
        if nodes[curr][0] == prev:
            prev = curr
            curr = nodes[curr][1]
        else:
            prev = curr
            curr = nodes[curr][0]
        
    #State: tree = [s, nodes[s][1], nodes[nodes[s][1]][1], ..., e], curr = e, prev = nodes[e][0].
    tree.append(e)
    start = int(input())
    idx = tree.index(start)
    moves = [idx, n - idx - 1]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *tree is [s, nodes[s][1], nodes[nodes[s][1]][1], ..., e, e], curr is e, prev is nodes[e][0], start is an integer, idx is the index of start in tree, moves is [idx, n - idx - 1], stdin contains no input. If at least one move in moves is odd, 'Ron' is printed. Otherwise, all elements in moves are even, and 'Hermione' is printed.

#Overall this is what the function does:This function reads input from stdin, constructs an adjacency list representation of a graph with n vertices and n-1 edges, identifies the nodes with degree 1, finds a path between these nodes, and determines whether a given starting node is closer to the first or last node in the path. Based on this, it prints either 'Ron' or 'Hermione' to the console, depending on whether the number of moves to the closest end of the path is odd or even.

