#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer greater than or equal to 2 and t is 1, then n-1 lines each containing two integers u and v, where u and v are integers greater than or equal to 1 and less than or equal to n, and finally one integer u, where u is an integer greater than or equal to 1 and less than or equal to n.
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
        
    #State: n is an integer greater than or equal to 2, t is 1, tree is a deque with at least n elements, empty is False, i is n - 1, u is an integer greater than or equal to 1 and less than or equal to n, v is an integer greater than or equal to 1 and less than or equal to n, and stdin is empty.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *n is an integer greater than or equal to 2, t is 1, tree is a deque with at least n elements, empty is False, i is n - 1, u is an integer greater than or equal to 1 and less than or equal to n, v is an integer greater than or equal to 1 and less than or equal to n, start is an integer, idx is an integer, moves is a list with two elements, and stdin is empty. If the list of moves contains at least one odd number, 'Ron' is printed. Otherwise, if all elements of the moves list are even, 'Hermione' is printed.

#Overall this is what the function does:This function reads input from stdin, constructs a tree from the input, and determines whether a given starting point is closer to the beginning or end of the tree. It then prints 'Ron' if the minimum number of moves to reach the start from either end is odd, and 'Hermione' if it's even.

