#State of the program right berfore the function call: l is a list of integers.
def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])
    #The program returns the index of the maximum value in the list `l`.
#Overall this is what the function does:The function accepts a list of integers and returns the index of the maximum value in the list.

#State of the program right berfore the function call: u2vs is a list of lists where each inner list contains integers representing the vertices connected to the vertex at the index of the outer list, n is an integer representing the number of vertices in the tree, u and v are integers representing the vertices connected by an edge in the tree, and 0 <= u, v < n.
def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = tuple(map(int, input().split()))
        
        u -= 1
        
        v -= 1
        
        u2vs[u].append(v)
        
        u2vs[v].append(u)
        
    #State: 
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
        
    #State: `d` is assigned the first value returned by `bfs(a)`, `a` is the result of `func_1(d)`, `previous` is the second value returned by `bfs(a)`, `b` is the result of `func_1(d)`, and `path_ba` is `[b, n1, n2, ..., nk]` where `n1, n2, ..., nk` are the values of `n` appended to `path_ba` before `n` becomes `-1`.
    ops = []
    if (len(path_ba) % 2 == 1) :
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
            
        #State: `d` is assigned the first value returned by `bfs(a)`, `a` is the result of `func_1(d)`, `previous` is the second value returned by `bfs(a)`, `b` is the result of `func_1(d)`, `path_ba` is `[b, n1, n2, ..., nk]` where `n1, n2, ..., nk` are the values of `n` appended to `path_ba` before `n` becomes `-1`, the length of `path_ba` is odd, `ops` is `[(c, 0), (c, 1)]`, `ci` is 1, `c` is the middle element of `path_ba`, `i` is 1.
    else :
        ci2 = len(path_ba) // 2
        ci1 = ci2 - 1
        c1 = path_ba[ci1]
        c2 = path_ba[ci2]
        for i in range(1, len(path_ba) - ci1, 2):
            ops.append((c1, i))
            
            ops.append((c2, i))
            
        #State: `d` is assigned the first value returned by `bfs(a)`, `a` is the result of `func_1(d)`, `previous` is the second value returned by `bfs(a)`, `b` is the result of `func_1(d)`, `path_ba` is a list with at least 3 elements `[b, n1, n2, ..., nk]`, the length of `path_ba` is even, `ci2` is the integer division of the length of `path_ba` by 2, `ci1` is `ci2 - 1`, `c1` is `path_ba[ci1]`, `c2` is `path_ba[ci2]`, `ops` is a list containing `L` elements `[(c1, 1), (c2, 1), (c1, 3), (c2, 3), ..., (c1, L-1), (c2, L-1)]`.
    #State: `d` is assigned the first value returned by `bfs(a)`, `a` is the result of `func_1(d)`, `previous` is the second value returned by `bfs(a)`, `b` is the result of `func_1(d)`, `path_ba` is a list with at least 3 elements `[b, n1, n2, ..., nk]` where `n1, n2, ..., nk` are the values of `n` appended to `path_ba` before `n` becomes `-1`. If the length of `path_ba` is odd, `ops` is `[(c, 0), (c, 1)]`, `ci` is 1, and `c` is the middle element of `path_ba`. If the length of `path_ba` is even, `ci2` is the integer division of the length of `path_ba` by 2, `ci1` is `ci2 - 1`, `c1` is `path_ba[ci1]`, `c2` is `path_ba[ci2]`, and `ops` is a list containing `L` elements `[(c1, 1), (c2, 1), (c1, 3), (c2, 3), ..., (c1, L-1), (c2, L-1)]`.
    print(len(ops))
    #This is printed: len(ops) (where len(ops) is 2 if the length of path_ba is odd, and calculated based on the length of path_ba if it is even)
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    #This is printed: If the length of `path_ba` is odd, the output will be:
    #```
    #c + 1 0
    #c + 1 1
    #```
    #where `c` is the middle element of `path_ba`.
    #
    #If the length of `path_ba` is even, the output will be:
    #```
    #c1 + 1 1
    #c2 + 1 1
    #c1 + 1 3
    #c2 + 1 3
    #...
    #c1 + 1 L-1
    #c2 + 1 L-1
    #```
    #where `c1` and `c2` are the middle elements of `path_ba`, and `L` is the length of `ops`.
    return None
    #The program returns None.
#Overall this is what the function does:The function reads input representing a tree, computes the longest path in the tree, and prints a series of operations based on the middle vertex or vertices of this path. The number of operations and their details depend on whether the path length is odd or even. The function does not return any value.

