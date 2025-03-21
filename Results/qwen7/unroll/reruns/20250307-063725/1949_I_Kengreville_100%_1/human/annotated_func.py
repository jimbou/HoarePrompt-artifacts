#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of length n, where for each i (0 ≤ i < n), x[i], y[i], and r[i] are integers representing the x-coordinate, y-coordinate, and radius of the i-th disk respectively. visited is a boolean list of length n indicating whether each disk has been visited during the DFS process. coef is a list of length n used to store coefficients during the DFS process. tot is an integer used to count the number of connected components during the DFS process. bipartite is a boolean variable used to check if the current component is bipartite.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: `n` is assigned the value of the input integer, `y` is a list of length `n` where each element is an integer input from the user, `x` is a list of length `n` where each element is an integer input from the user, `r` is a list of length `n` where each element is an integer input from the user, `visited` is now a list of length `n` filled with `False`, `coef` is a list of length `n` filled with `None`, `tot` retains its original state, `bipartite` retains its original state.
    tot = 0
    bipartite = True
    ok = False
    for i in range(n):
        if not visited[i]:
            coef[i] = 1
            tot = 0
            bipartite = True
            dfs(i)
            ok = ok or bipartite and tot != 0
        
    #State: Output State: `bipartite` is now a boolean value determined by the `dfs` function calls, `n` is the same input integer, `y` is the same list of length `n` where each element is an integer input from the user, `x` is the same list of length `n` where each element is an integer input from the user, `r` is the same list of length `n` where each element is an integer input from the user, `visited` is a list of length `n` where each element is either `True` or `False` based on whether the corresponding node was visited, `coef` is a list of length `n` where each element is either `1` or `None` based on whether the corresponding node was visited and marked with a coefficient of `1`, `tot` is now `0`, `ok` is now `True` if any `bipartite` is `True` and `tot` is not `0` for the nodes visited during the DFS, otherwise `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `bipartite` is a boolean value determined by the `dfs` function calls, `n` is the same input integer, `y` is the same list of length `n` where each element is an integer input from the user, `x` is the same list of length `n` where each element is an integer input from the user, `r` is the same list of length `n` where each element is an integer input from the user, `visited` is a list of length `n` where each element is either `True` or `False` based on whether the corresponding node was visited, `coef` is a list of length `n` where each element is either `1` or `None` based on whether the corresponding node was visited and marked with a coefficient of `1`, `tot` is `0`, and `ok` is `True` if any `bipartite` is `True` and `tot` is not `0` for the nodes visited during the DFS, otherwise `False`.
#Overall this is what the function does:The function processes a set of disks represented by their coordinates and radii. It performs a depth-first search (DFS) on these disks to determine if any connected component forms a bipartite graph and if there are any non-zero connected components. If any connected component is found to be bipartite and contains more than one disk, it prints 'YES'. Otherwise, it prints 'NO'. The function does not return any value.

