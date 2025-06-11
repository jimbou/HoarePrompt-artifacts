#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer (2 <= n <= 2 * 10^5) and t is 1, then n-1 lines each containing two integers u and v, where 1 <= u, v <= n, and finally one integer u_1, where 1 <= u_1 <= n.
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: x is an integer equal to 1, y is 1, lst is a dictionary where each key is an integer and its corresponding value is a list of integers, stdin is empty
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: `x` is an integer, `y` is an integer, `lst` is a dictionary where each key is an integer and its corresponding value is a list of integers, `lst[1]` is empty, `s` is True, stdin is empty.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Ron

#Overall this is what the function does:Determines the winner of a game based on the structure of a graph and the order of node removals. The function reads input from stdin, constructs a graph, and then simulates a process of removing nodes from the graph. The function prints 'Hermione' if the graph is removed in an even number of steps and 'Ron' if it is removed in an odd number of steps.

