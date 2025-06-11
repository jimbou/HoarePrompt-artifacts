#State of the program right berfore the function call: tree is a tree data structure with n vertices, s is the root of the tree, and x is a positive integer.
    stack = [(s, False)]
    good_components = {}
    remaining_size = {}
    while stack:
        v, postorder = stack.pop()
        
        if not postorder:
            stack.append((v, True))
            good_components[v] = 0
            remaining_size[v] = 1
            for u in tree.vertices[v].children:
                stack.append((u, False))
        elif postorder:
            for u in tree.vertices[v].children:
                good_components[v] += good_components[u]
                if remaining_size[u] >= x:
                    good_components[v] += 1
                else:
                    remaining_size[v] += remaining_size[u]
        
    #State: tree is a tree data structure with n vertices, s is the root of the tree, x is a positive integer, stack is an empty list, good_components is a dictionary where each key is a vertex in the tree and the value is the number of good components in the subtree rooted at that vertex, and remaining_size is a dictionary where each key is a vertex in the tree and the value is the sum of the sizes of the subtrees rooted at its children that have a size less than x.
    return good_components[s], remaining_size[s]
    #The program returns a tuple containing two values: the number of good components in the subtree rooted at the root 's' of the tree, and the sum of the sizes of the subtrees rooted at the children of 's' that have a size less than the positive integer 'x'.

#Overall this is what the function does:This function calculates and returns the number of good components and the total size of subtrees with a size less than a given threshold 'x' in a tree data structure rooted at 's'. A good component is a subtree with a size greater than or equal to 'x'. The function traverses the tree, aggregating the count of good components and the total size of smaller subtrees for each vertex, ultimately returning these values for the root vertex 's'.

#State of the program right berfore the function call: tree is a Tree object, v is a non-negative integer representing a vertex in the tree, and x is a non-negative integer representing the minimum size of each connected component.
    good_components = 0
    remaining_size = 1
    for u in tree.vertices[v].children:
        good_components_subtree, remaining_size_subtree = func_2(tree, u, x)
        
        good_components += good_components_subtree
        
        if remaining_size_subtree >= x:
            good_components += 1
        else:
            remaining_size += remaining_size_subtree
        
    #State: tree is a Tree object, v is a non-negative integer representing a vertex in the tree, x is a non-negative integer representing the minimum size of each connected component, good_components is the number of connected components in the subtree rooted at v with size at least x, remaining_size is the sum of the sizes of the connected components in the subtree rooted at v with size less than x.
    print(v, good_components, remaining_size)
    #This is printed: v (a non-negative integer representing a vertex in the tree), good_components (the number of connected components in the subtree rooted at v with size at least x), remaining_size (the sum of the sizes of the connected components in the subtree rooted at v with size less than x)
    return good_components, remaining_size
    #The program returns a tuple containing the number of connected components in the subtree rooted at vertex v with size at least x, and the sum of the sizes of the connected components in the subtree rooted at v with size less than x. The number of good components is good_components, and the remaining size is remaining_size.

#Overall this is what the function does:This function calculates and returns the number of connected components in the subtree rooted at a given vertex with a size of at least a specified minimum size, and the total size of the connected components in the subtree with a size less than the minimum size. It traverses the subtree, recursively processing the children of the given vertex, and aggregates the results to provide the total count of good components and the remaining size.

#State of the program right berfore the function call: tree is a Tree object, n is a positive integer representing the number of vertices in the tree, k is a non-negative integer less than n representing the number of edges to be removed, and x is a positive integer representing the minimum size of each connected component.
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True, indicating that the number of good components (connected components with size at least x) is greater than the number of edges to be removed (k).
    #State: *`tree` is a Tree object, `n` is a positive integer representing the number of vertices in the tree, `k` is a non-negative integer less than `n` representing the number of edges to be removed, `x` is a positive integer representing the minimum size of each connected component, `good_components` is the number of connected components in the tree with size at least `x`, and `remaining_size` is the total size of the remaining connected components with size less than `x`. The number of good components is less than or equal to `k`
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True, indicating that the number of good components is equal to k and the total size of the remaining connected components with size less than x is greater than or equal to x.
    #State: *`tree` is a Tree object, `n` is a positive integer representing the number of vertices in the tree, `k` is a non-negative integer less than `n` representing the number of edges to be removed, `x` is a positive integer representing the minimum size of each connected component, `good_components` is the number of connected components in the tree with size at least `x`, and `remaining_size` is the total size of the remaining connected components with size less than `x`. The number of good components is less than or equal to `k`, and either the number of good components is not equal to `k` or the remaining size is less than `x`.
    return False
    #The program returns False

#Overall this is what the function does:Determines whether a tree can be decomposed into connected components of a minimum size by removing a specified number of edges. The function takes a Tree object, the number of vertices, the number of edges to be removed, and the minimum size of each connected component as input. It returns True if the number of good components (connected components with size at least x) is greater than the number of edges to be removed, or if the number of good components is equal to the number of edges to be removed and the total size of the remaining connected components is greater than or equal to the minimum size. Otherwise, it returns False.

#State of the program right berfore the function call: tree is a valid tree data structure with n vertices, n is a positive integer representing the number of vertices in the tree, and k is a non-negative integer representing the number of edges to be removed, such that 0 <= k < n.
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: `tree` is a valid tree data structure with `n` vertices, `n` is a positive integer representing the number of vertices in the tree, `k` is a non-negative integer representing the number of edges to be removed, such that 0 <= `k` < `n`. `beg` is the smallest value for which `func_3(tree, n, k, beg)` returns True, `end` is `beg - 1`. If no such `beg` exists, `beg` is `n` and `end` is `n-1`.
    return beg
    #The program returns the smallest value 'beg' for which 'func_3(tree, n, k, beg)' returns True, where 'tree' is a valid tree data structure with 'n' vertices, 'n' is a positive integer representing the number of vertices in the tree, 'k' is a non-negative integer representing the number of edges to be removed, such that 0 <= 'k' < 'n'. If no such 'beg' exists, 'beg' is 'n'.

#Overall this is what the function does:This function performs a binary search to find the smallest value 'beg' for which a given condition 'func_3(tree, n, k, beg)' returns True, where 'tree' is a valid tree data structure with 'n' vertices and 'k' is the number of edges to be removed. If such a 'beg' exists, it returns the smallest value; otherwise, it returns 'n'. The function takes a tree, the number of vertices 'n', and the number of edges to be removed 'k' as input and returns the smallest valid 'beg' value or 'n' if no such value exists.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k < n <= 10^5.
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: n and k are positive integers such that 1 <= k < n <= 10^5, tree is a Tree object with n nodes and n-1 additional edges, i is n-1, stdin contains n-1 less input: n-1 space-separated pairs of integers.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: the result of func_4(tree, n, k) (where tree is a Tree object with n nodes and n-1 additional edges, n is a positive integer such that 1 <= k < n <= 10^5, and k is a positive integer such that 1 <= k < n <= 10^5)

#Overall this is what the function does:Constructs a tree with n nodes and n-1 edges, roots the tree at node 0, and then calls the func_4 function with the constructed tree, n, and k as arguments, printing the result.

