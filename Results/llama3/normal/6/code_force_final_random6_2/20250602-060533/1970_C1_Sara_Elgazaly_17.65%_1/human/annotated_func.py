#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer between 2 and 200000 (inclusive) and t is 1, then n-1 lines each containing two integers between 1 and n (inclusive), and finally one integer between 1 and n (inclusive).
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: x is an integer greater than 1, y is 1, lst is a dictionary where each key is a node in a graph and its corresponding value is a list of its neighbors, stdin is empty
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: Output State: `x` is an integer greater than 1, `y` is the last element that was in `lst[x]`, `lst` is a dictionary where each key is a node in a graph and its corresponding value is a list of its neighbors, `lst[x]` is empty, `s` is True if the number of iterations is even, False if the number of iterations is odd, stdin is empty.
    #
    #In natural language, the output state after the loop executes all the iterations is that `x` remains an integer greater than 1, `y` is the last element that was in the list of neighbors of `x`, the graph represented by `lst` remains unchanged, the list of neighbors of `x` is empty, and the value of `s` alternates between True and False depending on whether the number of iterations is even or odd.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Hermione (if the number of iterations is odd) or Ron (if the number of iterations is even)

#Overall this is what the function does:This function reads input from stdin representing a graph, traverses the graph in a specific manner, and prints 'Hermione' if the number of iterations is odd or 'Ron' if the number of iterations is even. The graph is represented as a dictionary where each key is a node and its corresponding value is a list of its neighbors. The function does not modify the graph structure but empties the list of neighbors of the last visited node.

