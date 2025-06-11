#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer between 2 and 2*10^5 and t is 1, then n-1 lines each containing two integers u and v, where 1 <= u, v <= n, and finally one integer u_1, where 1 <= u_1 <= n.
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: x is an integer between 2 and 2*10^5, y is 1, lst is a dictionary with x-1 keys each containing a list of adjacent nodes, stdin contains one integer u_1.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: x is the last non-empty node in the graph, y is the last node popped from the list of adjacent nodes, lst remains unchanged except for the nodes that were popped, and s is False if the graph has an even number of nodes and True if it has an odd number of nodes.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: 'Hermione' if the graph has an even number of nodes, 'Ron' if the graph has an odd number of nodes

#Overall this is what the function does:Determines whether a graph represented by a list of adjacent nodes has an even or odd number of nodes and prints 'Hermione' for even and 'Ron' for odd.

