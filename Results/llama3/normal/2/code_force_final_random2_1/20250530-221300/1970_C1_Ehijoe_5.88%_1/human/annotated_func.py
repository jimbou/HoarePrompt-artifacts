#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer greater than or equal to 2 and t is 1, then n-1 lines each containing two integers u and v, where 1 <= u, v <= n, and finally one integer u, where 1 <= u <= n.
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
        
    #State: n is an integer greater than or equal to 2, t is 1, empty is False, i is n-1, u and v are integers where 1 <= u, v <= n, stdin is empty. If empty was True, then tree is a deque containing n integers. If empty was False, then tree is updated based on the values of u and v as follows: if v is equal to the first element of tree, then tree is a deque with an additional element u at the beginning. If v is equal to the last element of tree, then tree is a deque with an additional element u at the end. If u is equal to the first element of tree, then tree is a deque with v as the first element. If u is equal to the last element of tree, then tree is updated by appending v to it. If v is equal to the second element of tree, then tree is a deque with at least three elements. If v is equal to the second last element of tree, then tree is a deque with at least three elements. If u is equal to the first element of tree, then tree is a deque with at least three elements, u is equal to the second element of tree and v is the first element of tree. If u is equal to the last element of tree, then tree is a deque with an additional element v at the end and an additional element u at the beginning. Otherwise, tree remains unchanged but with an additional element u at the beginning or tree remains unchanged but with an additional element v at the end.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *n is an integer greater than or equal to 2, t is 1, empty is False, i is n-1, u and v are integers where 1 <= u, v <= n, stdin is empty, start is an integer, idx is an integer, moves is a list containing two integers. If at least one of the integers in the list moves is odd, 'Ron' is being printed. If all elements in the list moves are even, 'Hermione' is being printed.

#Overall this is what the function does:This function reads input from stdin, constructs a tree based on the input, and determines whether Ron or Hermione wins a game. The function accepts no parameters and returns no value, but instead prints 'Ron' or 'Hermione' to the console based on the parity of the minimum moves required to reach the start node from both ends of the tree. The function assumes that the input is well-formed and does not perform any error checking.

