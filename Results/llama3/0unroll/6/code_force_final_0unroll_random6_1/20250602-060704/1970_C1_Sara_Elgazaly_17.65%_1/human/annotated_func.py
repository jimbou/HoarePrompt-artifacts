#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer (2 <= n <= 2*10^5) and t is 1, then n-1 lines each containing two integers u and v (1 <= u, v <= n), and finally one integer u_1 (1 <= u_1 <= n).
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: Output State: x is an integer equal to 1, y is 1, lst is a dictionary where each key is a node in the graph and its corresponding value is a list of its neighbors, stdin is empty.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: x is an integer equal to 1, y is 1, lst is a dictionary where each key is a node in the graph and its corresponding value is an empty list, s is True, stdin is empty.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Ron

#Overall this is what the function does:This function reads input from stdin, constructs an undirected graph from the input, and then performs a traversal of the graph. The function prints 'Hermione' if the graph has an even number of nodes with odd degrees, and 'Ron' otherwise.

