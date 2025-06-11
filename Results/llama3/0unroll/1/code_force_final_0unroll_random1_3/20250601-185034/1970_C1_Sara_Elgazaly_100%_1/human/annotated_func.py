#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer such that 2 <= n <= 2*10^5 and t is 1, then n-1 lines each containing two integers u and v such that 1 <= u, v <= n, and finally one integer u such that 1 <= u <= n.
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: Output State: x is an integer equal to the first input, y is an integer equal to the second input, lst is a dictionary where each key is a node and its corresponding value is a list of its children, rev is a dictionary where each key is a node and its corresponding value is a list of its parents, stdin contains one integer u.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: x is an integer equal to the first input, y is an integer equal to the second input, lst is a dictionary where each key is a node and its corresponding value is a list of its children, rev is a dictionary where each key is a node and its corresponding value is a list of its parents, z is an integer equal to the input u, tmp is an integer equal to the last node in the list of children of the node with key u in lst, one is False
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: tmp is an integer equal to the last parent of the input u, two is True if the input u has an even number of parents and False if it has an odd number of parents, rev is a dictionary where each key is a node and its corresponding value is a list of its parents with the last parent of the input u removed.
    print('Hermione' if two and one else 'Ron')
    #This is printed: 'Hermione' if two is True and one is True, 'Ron' otherwise

#Overall this is what the function does:Determines whether a given node in a directed graph has an even or odd number of parents and children, and prints 'Hermione' if both are even, 'Ron' otherwise.

