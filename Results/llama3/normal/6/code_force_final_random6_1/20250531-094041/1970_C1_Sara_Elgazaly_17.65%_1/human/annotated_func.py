#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t (n is an integer between 2 and 200000 inclusive, t is 1), then n-1 lines each containing two integers u and v (1 <= u, v <= n), and finally one integer u_1 (1 <= u_1 <= n).
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: x is 1, y is 1, lst is a dictionary with default value of empty list where lst[a] contains b and lst[b] contains a, and also lst[u] contains v and lst[v] contains u, and also lst[a] contains b and lst[b] contains a, and so on for all pairs of integers in stdin, stdin contains one integer u_1
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: x is an integer, y is an integer, lst is a dictionary with default value of empty list where lst[a] contains b and lst[b] contains a, and also lst[u] contains v and lst[v] contains u, and so on for all pairs of integers, lst[x] is empty, s is True, stdin contains no input.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Ron

#Overall this is what the function does:This function reads input from stdin, constructs an undirected graph from the input, and then traverses the graph in a specific manner, ultimately printing 'Hermione' or 'Ron' to the console based on the final state of the traversal. The function does not return any value, and its primary purpose is to determine and print the result of the graph traversal.

