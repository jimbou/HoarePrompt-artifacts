#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer greater than or equal to 2 and t is equal to 1, then n-1 lines each containing two integers u and v, where u and v are integers greater than or equal to 1 and less than or equal to n, and finally one integer u, where u is an integer greater than or equal to 1 and less than or equal to n.
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: n is an integer greater than or equal to 2, t is 1, edges is an empty list, empty is True, nodes is a defaultdict with a default value of an empty list where nodes[u] contains v and nodes[v] contains u for all u and v read from stdin, stdin contains one integer u, and i is n-1.
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: `n` is an integer greater than or equal to 2, `t` is 1, `edges` is an empty list, `empty` is True, `nodes` is a defaultdict with a default value of an empty list where `nodes[u]` contains `v` and `nodes[v]` contains `u` for all `u` and `v` read from stdin and `nodes` has at least `n-1` key-value pairs, `i` is `n-1`, stdin contains one integer `u`. If the length of `nodes[key]` is 1, `ends` is a list containing all keys in the nodes where the length of `nodes[key]` is 1. Otherwise, `ends` is an empty list.
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
        
    #State: n is an integer greater than or equal to 2, t is 1, edges is an empty list, empty is True, nodes is a defaultdict with a default value of an empty list where nodes[u] contains v and nodes[v] contains u for all u and v read from stdin and nodes has at least n-1 key-value pairs, i is n-1, stdin is empty, s is a key in nodes where the length of nodes[key] is 1, e is a key in nodes where the length of nodes[key] is 1, tree is a list containing s, e, and all the nodes between s and e, prev is e, and curr is e.
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
    #State: n is an integer greater than or equal to 2, t is 1, edges is an empty list, empty is True, nodes is a defaultdict with a default value of an empty list where nodes[u] contains v and nodes[v] contains u for all u and v read from stdin and nodes has at least n-1 key-value pairs, i is n-1, stdin is empty, s is a key in nodes where the length of nodes[key] is 1, e is a key in nodes where the length of nodes[key] is 1, tree is a list containing s, e, and all the nodes between s and e, and e, prev is e, curr is e, start is an integer read from stdin, idx is the index of start in tree, and moves is a list containing idx and n - idx - 1. If at least one move in moves is an odd number, 'Ron' is printed. Otherwise, all the moves in the list moves are even, and 'Hermione' is printed.

#Overall this is what the function does:This function reads input from stdin, constructs a tree from the input, and determines whether a given starting point is closer to one end of the tree or the other. It then prints 'Ron' if the number of moves to one end is odd, and 'Hermione' if the number of moves to both ends is even.

