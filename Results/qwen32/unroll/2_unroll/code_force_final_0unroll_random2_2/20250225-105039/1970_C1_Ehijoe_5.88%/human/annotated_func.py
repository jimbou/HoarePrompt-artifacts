#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t=1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) with 1 ≤ u_1, ..., u_t ≤ n, representing the starting node of the stone for each round.
def func_1():
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
        
    #State: `tree` is a deque representing the path from one leaf to the other in the tree, and `empty` is False.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `tree` is a deque representing the path from one leaf to the other in the tree, `empty` is False, `start` is an input integer, `idx` is the index of `start` in `tree`, `moves` is a list containing `[min(t, idx), min(t, n - idx - 1)]`. At least one of the values in `moves` is odd if the if condition is met; otherwise, both elements in `moves` are even numbers.
#Overall this is what the function does:The function determines the winner of a game based on the movement of a stone on a tree with exactly two leaves. It accepts the number of nodes `n` in the tree, an integer `t` which is always 1, a list of `n-1` edges representing the tree structure, and a starting node for the stone. The function prints either 'Ron' or 'Hermione' depending on whether the stone can reach a leaf in an odd or even number of moves, respectively.

