#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer between 2 and 2*10^5 inclusive, and t is 1; then n-1 lines each containing two integers u and v, where u and v are integers between 1 and n inclusive; and finally one line containing one integer u, where u is an integer between 1 and n inclusive.
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
        
    #State: Output State: The variable t remains unchanged and is 1, the variable empty is False, and the variable tree is a deque containing a path from the root of the tree to the node u, where u is the node on the last line of the input.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *The variable t remains unchanged and is 1, the variable empty is False, the variable tree is a deque containing a path from the root of the tree to the node u, where u is the node on the last line of the input, the variable start is an integer read from stdin, the variable idx is the index of start in the deque tree, and the variable moves is a list containing two integers: the minimum of t and idx, and the minimum of t and the number of elements in tree minus idx minus 1. Stdin now contains one less input. If at least one of the moves in the list is an odd number, 'Ron' is printed. Otherwise, all elements in the list moves are even, and 'Hermione' is printed.

#Overall this is what the function does:This function reads input from stdin, constructs a tree path from the root to a given node, and determines whether a game character 'Ron' or 'Hermione' wins based on the parity of the minimum moves required to reach the node from the start of the path. The function prints the winner's name to the console.

