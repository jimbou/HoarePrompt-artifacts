#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t (2 <= n <= 2*10^5, t=1), then n-1 lines each containing two integers u and v (1 <= u, v <= n), and finally one integer u_1 (1 <= u_1 <= n).
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: n is an integer between 2 and 2*10^5, t is 1, edges is an empty list, empty is True, nodes is a dictionary with n-1 keys, each containing a list with n-1 elements, stdin contains one integer u_1, i is n-2
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: `n` is an integer between 2 and 2*10^5, `t` is 1, `edges` is an empty list, `empty` is True, `nodes` is a dictionary with `n-1` keys, each containing a list with `n-1` elements, `i` is `n-2`, stdin contains one integer `u_1`, `ends` is a list containing all keys in the nodes dictionary that have a list of length 1.
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
        
    #State: n is an integer between 2 and 2*10^5, t is 1, edges is an empty list, empty is True, nodes is a dictionary with n-1 keys, each containing a list with n-1 elements, i is n-2, stdin is empty, ends is a list containing all keys in the nodes dictionary that have a list of length 1, s is the first element in ends, e is the second element in ends, tree is a list containing all elements from s to e, prev is e, and curr is e.
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
    #State: *n is an integer between 2 and 2*10^5, t is 1, edges is an empty list, empty is True, nodes is a dictionary with n-1 keys, each containing a list with n-1 elements, i is n-2, stdin is empty, ends is a list containing all keys in the nodes dictionary that have a list of length 1, s is the first element in ends, e is the second element in ends, tree is a list containing all elements from s to e and including e, prev is e, curr is e, tree contains an additional element e, start is an integer read from stdin, idx is the index of start in tree, moves is a list containing idx and n - idx - 1. If at least one element in moves is odd, 'Ron' is printed. Otherwise, all elements in moves are even, and 'Hermione' is printed.

#Overall this is what the function does:This function reads input from stdin, constructs a tree from the input, and determines whether a given starting point is closer to one end of the tree or the other. It then prints 'Ron' if the starting point is closer to one end, or 'Hermione' if it is equidistant from both ends. The function assumes the input is well-formed and does not perform any error checking.

