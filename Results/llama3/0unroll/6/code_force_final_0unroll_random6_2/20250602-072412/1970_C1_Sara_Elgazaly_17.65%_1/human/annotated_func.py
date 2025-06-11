#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer between 2 and 2*10^5 inclusive and t is 1, then n-1 lines each containing two integers u and v, where u and v are integers between 1 and n inclusive, and finally one integer u_1, where u_1 is an integer between 1 and n inclusive.
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: Output State: x is an integer equal to 1, y is 1, lst is a dictionary containing n-1 key-value pairs, where each key is an integer between 1 and n inclusive, and each value is a list containing one or more integers between 1 and n inclusive, and stdin contains one integer u_1, where u_1 is an integer between 1 and n inclusive.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: x is an integer equal to 1, y is an integer between 1 and n inclusive, lst is a dictionary containing n-1 key-value pairs, where each key is an integer between 1 and n inclusive, and each value is an empty list, stdin is empty, and s is False.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Hermione

#Overall this is what the function does:This function reads input from stdin, constructs an undirected graph with n nodes and n-1 edges, and then performs a depth-first search (DFS) traversal of the graph starting from node 1. The DFS traversal alternates between two states (True and False) at each step. After the traversal is complete, the function prints 'Hermione' if the final state is True and 'Ron' if the final state is False.

