#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer between 2 and 2 * 10^5 inclusive, and t is 1; then n-1 lines each containing two integers u and v, where 1 <= u, v <= n; and finally one integer u_1, where 1 <= u_1 <= n.
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: x is an integer between 2 and 2 * 10^5 inclusive, y is 1, lst is a dictionary where each key is a node and its corresponding value is a list of its children, rev is a dictionary where each key is a node and its corresponding value is a list of its parents, stdin contains one integer u_1.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: one is False, tmp is the last node in the path from z to a leaf node, lst is a dictionary where each key is a node and its corresponding value is a list of its children with the path from z to a leaf node removed, rev is unchanged, x is unchanged, y is unchanged, z is unchanged, stdin is unchanged.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: two is False, tmp is None, rev is unchanged, one is False, lst is unchanged, x is unchanged, y is unchanged, z is unchanged, stdin is unchanged.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Ron

#Overall this is what the function does:This function determines whether a given node in a tree is even or odd distance from a leaf node in both the forward and backward directions, and prints 'Hermione' if the node is even distance from a leaf node in both directions, and 'Ron' otherwise. The function accepts no parameters and returns no value, but instead prints the result to the console. The input tree is provided through standard input, with the first line containing the number of nodes and a dummy value, followed by the edges of the tree, and finally the node to check. The function modifies the input tree by removing the path from the given node to a leaf node in both the forward and backward directions.

