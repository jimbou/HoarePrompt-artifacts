#State of the program right berfore the function call: tree is a Tree object, s is an integer representing the root of the tree, and x is a positive integer representing the minimum size of each connected component.
    stack = [(s, False)]
    while stack:
        v, postorder = stack.pop()
        
        if not postorder:
            stack.append((v, True))
            for u in tree.vertices[v].children:
                stack.append((u, False))
        
        if postorder:
            for u in tree.vertices[v].children:
                tree.vertices[v].good_components += tree.vertices[u].good_components
                if tree.vertices[u].remaining_size >= x:
                    tree.vertices[v].good_components += 1
                else:
                    tree.vertices[v].remaining_size += tree.vertices[u].remaining_size
        
    #State: tree.vertices[s].good_components
    return tree.vertices[s].good_components, tree.vertices[s].remaining_size
    #The program returns tree.vertices[s].good_components and tree.vertices[s].remaining_size

#Overall this is what the function does:This function calculates the number of good components and the remaining size in a tree, where a good component is a connected component with a size greater than or equal to a given minimum size x. It traverses the tree in a post-order manner, aggregating the good components and remaining size from child nodes to their parents. The function returns the total number of good components and the remaining size for the root node of the tree.

#State of the program right berfore the function call: tree is a tree data structure with n vertices, v is a vertex in the tree, and x is a positive integer representing the minimum size of each connected component.
    good_components = 0
    remaining_size = 1
    for u in tree.vertices[v].children:
        good_components_subtree, remaining_size_subtree = func_2(tree, u, x)
        
        good_components += good_components_subtree
        
        if remaining_size_subtree >= x:
            good_components += 1
        else:
            remaining_size += remaining_size_subtree
        
    #State: Output State: tree is a tree data structure with n vertices, v is a vertex in the tree, x is a positive integer representing the minimum size of each connected component, good_components is the total number of good components in the subtree rooted at v, remaining_size is the total size of the remaining components in the subtree rooted at v.
    return good_components, remaining_size
    #The program returns the total number of good components in the subtree rooted at vertex v and the total size of the remaining components in the subtree rooted at vertex v.

#Overall this is what the function does:This function calculates and returns the total number of good components and the total size of the remaining components in the subtree rooted at a given vertex v in a tree data structure. A good component is a connected component with a size greater than or equal to a specified minimum size x. The function recursively traverses the subtree, counting good components and accumulating the size of remaining components.

#State of the program right berfore the function call: tree is a Tree data structure with n vertices, n and k are integers such that 1 <= k < n <= 10^5, and x is an integer representing the minimum size of each connected component.
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True, indicating that the number of good components in the tree is greater than k, where good components are connected components of size at least x in the tree rooted at 0, and k is an integer such that 1 <= k < n <= 10^5, and n is the number of vertices in the tree.
    #State: *`tree` is a Tree data structure with n vertices, `n` is an integer such that 1 <= k < n <= 10^5, `k` is an integer, `x` is an integer representing the minimum size of each connected component, `good_components` is a list of connected components of size at least `x` in `tree` rooted at 0, `remaining_size` is the total number of vertices in `tree` not in `good_components`, and the number of `good_components` is less than or equal to `k`
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns boolean value True
    #State: *`tree` is a Tree data structure with n vertices, `n` is an integer such that 1 <= k < n <= 10^5, `k` is an integer, `x` is an integer representing the minimum size of each connected component, `good_components` is a list of connected components of size at least `x` in `tree` rooted at 0, `remaining_size` is the total number of vertices in `tree` not in `good_components`, the number of `good_components` is less than or equal to `k`, and either the number of `good_components` is not equal to `k` or `remaining_size` is less than `x`
    return False
    #The program returns False

#Overall this is what the function does:This function determines whether a given tree has a sufficient number of connected components of a minimum size. It takes a tree data structure, an integer k, and an integer x as input, where x represents the minimum size of each connected component. The function returns True if the number of good components (connected components of size at least x) is greater than k, or if the number of good components is equal to k and the remaining vertices in the tree are sufficient to form another component of size at least x. Otherwise, it returns False.

#State of the program right berfore the function call: tree is a valid tree data structure with n vertices, n is a positive integer, and k is a non-negative integer such that 0 <= k < n.
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: beg = end = the smallest value of mid such that func_3(tree, n, k, mid) returns True
    return beg
    #The program returns the smallest value of mid such that func_3(tree, n, k, mid) returns True

#Overall this is what the function does:This function performs a binary search on a valid tree data structure with n vertices to find the smallest value of mid such that func_3(tree, n, k, mid) returns True. It takes a tree, a positive integer n, and a non-negative integer k as input and returns the smallest mid value satisfying the condition. The function iteratively narrows down the search range until it finds the smallest valid mid value, which is then returned as the result.

#State of the program right berfore the function call: n and k are integers such that 1 <= k < n <= 10^5, and the next n-1 lines of input contain two integers v and u (1 <= v, u <= n) representing the edges of the tree.
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: Output State: The tree object has been populated with n-1 edges, where each edge connects two nodes u and v, and the values of n and k remain unchanged.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: the result of the function func_4 applied to the tree object rooted at node 0, the value of n, and the value of k

#Overall this is what the function does:The function constructs a tree from the given input, roots it at node 0, and then applies the func_4 function to the rooted tree, the number of nodes (n), and the value of k, printing the result.

