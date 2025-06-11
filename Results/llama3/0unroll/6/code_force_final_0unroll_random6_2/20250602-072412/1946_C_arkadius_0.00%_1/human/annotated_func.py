#State of the program right berfore the function call: tree is a Tree object, s is a non-negative integer such that 0 <= s < len(tree.vertices), and x is a non-negative integer.
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

#Overall this is what the function does:This function calculates and returns the total number of good components and the total remaining size of a subtree rooted at a given vertex s in a tree, where a good component is a subtree with a size greater than or equal to a given threshold x. The function traverses the tree in a post-order manner, aggregating the good components and remaining sizes of child vertices to their parent vertices.

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
        
    #State: Output State: tree is a tree data structure with n vertices, v is a vertex in the tree, x is a positive integer representing the minimum size of each connected component, good_components is the total number of good components in the subtrees rooted at the children of v, remaining_size is the total size of the remaining components in the subtrees rooted at the children of v that are not good components.
    return good_components, remaining_size
    #The program returns the total number of good components in the subtrees rooted at the children of vertex v, and the total size of the remaining components in the subtrees rooted at the children of v that are not good components, where a good component is a connected component with a size of at least x.

#Overall this is what the function does:This function calculates the total number of good components and the total size of remaining components in the subtrees rooted at the children of a given vertex in a tree data structure. A good component is a connected component with a size of at least a specified minimum size. The function returns two values: the total number of good components and the total size of the remaining components that are not good components.

#State of the program right berfore the function call: tree is a Tree object, n is a positive integer representing the number of vertices in the tree, k is a positive integer representing the number of edges to be removed, and x is a positive integer representing the minimum size of each remaining connected component.
    good_components, remaining_size = func_1(tree, 0, x)
    if (good_components > k) :
        return True
        #The program returns True, indicating that the number of connected components with size at least `x` in the tree is greater than the number of edges to be removed `k`.
    #State: *`tree` is a Tree object, `n` is a positive integer representing the number of vertices in the tree, `k` is a positive integer representing the number of edges to be removed, `x` is a positive integer representing the minimum size of each remaining connected component, `good_components` is the number of connected components with size at least `x` in the tree, `remaining_size` is the total size of all connected components with size at least `x` in the tree, and `good_components` is less than or equal to `k`.
    if (good_components == k and remaining_size >= x) :
        return True
        #The program returns True, indicating that the number of connected components with size at least x in the tree equals the number of edges to be removed, and the total size of all connected components with size at least x is greater than or equal to x.
    #State: *`tree` is a Tree object, `n` is a positive integer representing the number of vertices in the tree, `k` is a positive integer representing the number of edges to be removed, `x` is a positive integer representing the minimum size of each remaining connected component, `good_components` is the number of connected components with size at least `x` in the tree, `remaining_size` is the total size of all connected components with size at least `x` in the tree, `good_components` is less than or equal to `k`, and either `good_components` is not equal to `k` or `remaining_size` is less than `x`.
    return False
    #The program returns False

#Overall this is what the function does:Determines if a tree can be decomposed into connected components with a minimum size, given the number of edges to be removed.

#State of the program right berfore the function call: tree is a tree data structure with n vertices, n is a positive integer representing the number of vertices in the tree, and k is a non-negative integer representing the number of edges to be removed from the tree, such that 0 <= k < n.
    beg = 1
    end = n
    while beg < end:
        mid = (beg + end + 1) // 2
        
        if func_3(tree, n, k, mid):
            beg = mid
        else:
            end = mid - 1
        
    #State: beg = end = the minimum number of edges that need to be removed from the tree to satisfy the condition checked by func_3, tree remains unchanged, n remains unchanged, k remains unchanged.
    return beg
    #The program returns the minimum number of edges that need to be removed from the tree to satisfy the condition checked by func_3

#Overall this is what the function does:This function determines the minimum number of edges that need to be removed from a tree data structure with n vertices to satisfy a specific condition checked by another function (func_3). It takes no parameters and returns the minimum number of edges to be removed. The function performs a binary search to find this minimum number, iteratively adjusting the search range until it converges on the solution. The tree data structure and the number of vertices (n) remain unchanged throughout the process. The function's purpose is to provide the minimum number of edge removals required to meet the condition specified by func_3, without actually modifying the tree.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k < n <= 10^5.
    [n, k] = map(int, input().split())
    tree = Tree(n)
    for i in range(1, n):
        [u, v] = map(int, input().split())
        
        tree.add_edge(u - 1, v - 1)
        
    #State: Output State: The tree has n nodes and n-1 edges, with each edge connecting two distinct nodes, and k is still a positive integer such that 1 <= k < n <= 10^5.
    tree.root_tree_non_recursive(0, -1)
    print(func_4(tree, n, k))
    #This is printed: the result of the function func_4 applied to the tree with n nodes, the number of nodes n, and the positive integer k (where 1 <= k < n <= 10^5)

#Overall this is what the function does:Constructs a tree with n nodes and n-1 edges from user input, and then applies the func_4 function to the tree, the number of nodes n, and a positive integer k, printing the result.

