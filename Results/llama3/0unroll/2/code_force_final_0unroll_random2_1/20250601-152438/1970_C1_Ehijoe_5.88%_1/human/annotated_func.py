#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t (n >= 2, t = 1), then n-1 lines each containing two integers u and v (1 <= u, v <= n), and finally one integer u_1 (1 <= u_1 <= n).
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
        
    #State: Output State: The variable t remains 1, the variable empty is False, the variable n remains unchanged, and the deque tree contains a sequence of integers representing a path in a tree, where each pair of adjacent integers in the sequence represents an edge in the tree. The sequence starts with the integer u_1, and each subsequent integer is either the left or right child of the previous integer in the tree.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: The variables t, empty, n, start, idx, and moves retain their initial values, and the deque tree remains unchanged. The sequence in the deque tree still represents a path in a tree, where each pair of adjacent integers represents an edge in the tree. If at least one of the integers in the moves list is odd, 'Ron' is printed. Otherwise, all elements in the moves list are even, and 'Hermione' is printed.

#Overall this is what the function does:This function reads input from stdin, constructs a tree path from the input, and determines whether a sequence of moves is possible. It takes no parameters and returns no value, but instead prints 'Ron' if at least one move in the sequence is odd, and 'Hermione' if all moves are even. The function assumes that the input is well-formed and does not perform any error checking.

