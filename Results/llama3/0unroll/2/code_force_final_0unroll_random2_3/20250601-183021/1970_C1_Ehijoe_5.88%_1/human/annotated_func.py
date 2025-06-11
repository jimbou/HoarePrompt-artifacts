#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t (n is an integer such that 2 <= n <= 2*10^5 and t is 1), then n-1 lines each containing two integers u and v (1 <= u, v <= n), and finally one integer u_1 (1 <= u_1 <= n).
    n, t = map(int, input().split())
    tree = deque()
    empty = True
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        if empty:
            tree.append(u)
            tree.append(v)
            empty = False
        elif v == tree[0]:
            tree.appendleft(u)
        elif v == tree[-1]:
            tree.append(u)
        elif u == tree[0]:
            tree.appendleft(v)
        elif u == tree[-1]:
            tree.append(v)
        
    #State: tree is a deque containing a path of length n from u_1 to all other nodes in the tree, empty is False, t is 1, and n is an integer between 2 and 2*10^5 inclusive.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *tree is a deque containing a path of length n from u_1 to all other nodes in the tree, empty is False, t is 1, n is an integer between 2 and 2*10^5 inclusive, start is an integer, idx is an integer, and moves is a list containing two integers. If at least one of the integers in moves is odd, 'Ron' is being printed. Otherwise, if both integers in moves are even, 'Hermione' is being printed.

#Overall this is what the function does:Determines the winner of a game based on the parity of the minimum number of moves required to reach a target node in a tree structure. The function reads input from stdin, constructs a tree path, and calculates the minimum moves to the start node. If at least one of the minimum moves is odd, it prints 'Ron'; otherwise, it prints 'Hermione'.

