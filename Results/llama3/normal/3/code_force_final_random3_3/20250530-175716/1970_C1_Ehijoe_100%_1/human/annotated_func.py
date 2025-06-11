#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer between 2 and 2*10^5 and t is 1, then n-1 lines each containing two integers u and v, where 1 <= u, v <= n, and finally one integer u, where 1 <= u <= n.
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: n is an integer between 2 and 2*10^5, t is 1, edges is an empty list, empty is True, nodes is a defaultdict of lists with n-1 nodes, where each node is connected to every other node, stdin contains one integer u, i is n-2
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: n is an integer between 2 and 2*10^5, t is 1, edges is an empty list, empty is True, nodes is a defaultdict of lists with n-1 nodes, key is the last key in the nodes dictionary, i is n-2, stdin contains one integer u. If the length of the list of any key in the nodes dictionary is 1, then ends is a list containing all keys in the nodes dictionary with a list length of 1. Otherwise, ends is an empty list.
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
        
    #State: n is an integer between 2 and 2*10^5, t is 1, edges is an empty list, empty is True, nodes is a defaultdict of lists with n-1 nodes, key is the last key in the nodes dictionary, i is n-2, s is the first key in the ends list, e is the second key in the ends list, stdin is empty, ends is a list containing all keys in the nodes dictionary with a list length of 1, tree is a list containing all keys in the nodes dictionary with a list length of 1, prev is the second key in the ends list, curr is the second key in the ends list.
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
    #State: *n is an integer between 2 and 2*10^5, t is 1, edges is an empty list, empty is True, nodes is a defaultdict of lists with n-1 nodes, key is the last key in the nodes dictionary, i is n-2, s is the first key in the ends list, e is the second key in the ends list, stdin is empty, ends is a list containing all keys in the nodes dictionary with a list length of 1, tree is a list containing all keys in the nodes dictionary with a list length of 1 and the second key in the ends list, prev is the second key in the ends list, curr is the second key in the ends list, start is an integer read from stdin, idx is the index of start in the tree list, moves is a list containing idx and n - idx - 1. If at least one move in the moves list is odd, 'Ron' is printed. If all elements in the moves list are even, 'Hermione' is printed.

#Overall this is what the function does:This function determines the winner of a game based on the number of moves required to reach a target node in a tree-like graph. The function reads input from stdin, constructs the graph, identifies the start node, calculates the number of moves to the target node, and prints the winner's name ('Ron' if at least one move is odd, 'Hermione' if all moves are even).

