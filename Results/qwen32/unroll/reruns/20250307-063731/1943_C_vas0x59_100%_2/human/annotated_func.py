#State of the program right berfore the function call: l is a list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the maximum value in the list `l`.
#Overall this is what the function does:The function accepts a list of integers and returns the index of the maximum value in the list.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the tree, where 1 <= n <= 2 * 10^3. u2vs is a list of lists where u2vs[i] contains the list of vertices directly connected to vertex i (0-indexed), representing the adjacency list of the tree.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: `u2vs` is a list of `n` lists, where each list at index `i` contains the indices of all nodes directly connected to node `i` in the graph.
    d, _ = bfs(0)
    a = func_1(d)
    d, previous = bfs(a)
    b = func_1(d)
    path_ba = [b]
    while True:
        n = previous[path_ba[-1]]
        
        if n == -1:
            break
        
        path_ba.append(n)
        
    #State: `path_ba` contains the indices of the nodes on the shortest path from node `0` to node `b` in reverse order.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: - The `ops` list will contain tuples where the first element is always `c` (the value at the middle index of `path_ba`), and the second element ranges from `0` to `ci`.
        #   - The length of `ops` will be `ci + 1`.
        #
        #Given the above, the output state will be:
        #
        #- `path_ba` remains unchanged.
        #- `ci` remains unchanged.
        #- `c` remains unchanged.
        #- `ops` will be a list of tuples `[(c, 0), (c, 1), ..., (c, ci)]`.
        #
        #Output State:
    else :
        ci2 = len(path_ba) // 2
        ci1 = ci2 - 1
        c1 = path_ba[ci1]
        c2 = path_ba[ci2]
        for i in range(1, len(path_ba) - ci1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: path_ba contains the indices of the nodes on the shortest path from node 0 to node b in reverse order; ops is [(c1, 1), (c2, 1), (c1, 3), (c2, 3)]; ci2 is the integer value of half the length of path_ba; ci1 is ci2 - 1; c1 is the value at index ci1 in path_ba; c2 is the value at index ci2 in path_ba.
    #State: `path_ba` contains the indices of the nodes on the shortest path from node 0 to node b in reverse order. If the length of `path_ba` is odd, `ops` will be a list of tuples `[(c, 0), (c, 1), ..., (c, ci)]`, where `c` is the value at the middle index of `path_ba` and `ci` is the middle index. Otherwise, `ops` will be `[(c1, 1), (c2, 1), (c1, 3), (c2, 3)]`, where `ci1` is the integer value of half the length of `path_ba` minus one, `ci2` is the integer value of half the length of `path_ba`, `c1` is the value at index `ci1` in `path_ba`, and `c2` is the value at index `ci2` in `path_ba`.
    print(len(ops))
    #This is printed: len(ops) (where len(ops) is (len(path_ba) // 2) + 1 if len(path_ba) is odd, or 4 if len(path_ba) is even)
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: Each line will be in the format `x+1 y` where `x` is the node index from `path_ba` and `y` is the operation code (0, 1, or 3) based on the length and middle indices of `path_ba`.
    return None
    #The program returns None
#Overall this is what the function does:The function reads an integer `n` representing the number of vertices in a tree and an adjacency list `u2vs` representing the tree's edges. It calculates the longest path in the tree and generates a series of operations based on the middle node(s) of this path. The function prints the number of operations and the operations themselves, where each operation is a tuple indicating a node index and an operation code. The function returns `None`.

