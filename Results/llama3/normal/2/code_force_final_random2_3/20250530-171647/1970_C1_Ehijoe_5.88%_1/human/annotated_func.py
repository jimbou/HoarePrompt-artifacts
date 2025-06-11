#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t (2 <= n <= 2*10^5 and t = 1), then n-1 lines each containing two integers u and v (1 <= u, v <= n), and finally one integer u_1 (1 <= u_1 <= n).
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
        
    #State: `n` is an integer between 2 and 2*10^5 inclusive, `t` is 1, `tree` is a deque containing at least `n` elements, `empty` is False, `i` is `n-1`, `u` and `v` are integers that were read from the last line of `stdin` which is empty, and `stdin` is empty.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *n is an integer between 2 and 2*10^5 inclusive, t is 1, tree is a deque containing at least n elements, empty is False, i is n-1, u and v are integers, stdin is empty, start is an integer, idx is an integer, moves is a list containing two integers. If at least one of the integers in moves is odd, 'Ron' is being printed. If both elements of the moves list are even, 'Hermione' is being printed.

#Overall this is what the function does:This function reads input from stdin, constructs a tree from the input, and determines whether a given starting point is closer to the beginning or end of the tree. It then prints 'Ron' if the starting point is closer to the beginning or end of the tree by an odd number of moves, and 'Hermione' otherwise.

