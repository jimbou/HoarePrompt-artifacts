#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t (2 <= n <= 2*10^5, t=1), then n-1 lines each containing two integers u and v (1 <= u, v <= n), and finally one integer u_1 (1 <= u_1 <= n).
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: x is an integer equal to 1, y is an integer equal to the second input, lst is a dictionary with a single key-value pair where the key is a and the value is a list containing b, u, and the two integers u, rev is a dictionary with a single key-value pair where the key is b and the value is a list containing a, u, and the two integers u, stdin contains no lines.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: x is 1, y is an integer equal to the second input, lst is a dictionary with a key-value pair where the key is equal to the first input and the value is an empty list, rev is a dictionary with a single key-value pair where the key is b and the value is a list containing a, u, and the two integers u, z is an integer equal to the first input, tmp is an integer equal to the last element of the list that was the value of the key-value pair in lst with key equal to the first input, one is False, stdin contains 1 input: an integer.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: x is 1, y is an integer equal to the second input, lst is a dictionary with a key-value pair where the key is equal to the first input and the value is an empty list, rev is a dictionary with a single key-value pair where the key is b and the value is an empty list, two is True, one is False, tmp is the last element of the list associated with the key b in the dictionary rev, stdin contains 1 input: an integer, z is an integer equal to the first input.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Ron

#Overall this is what the function does:This function reads input from stdin, constructs a directed graph from the input, and then performs a depth-first search (DFS) traversal of the graph in both forward and backward directions. The function then prints 'Hermione' if the DFS traversal in both directions visits the same nodes in the same order, and 'Ron' otherwise. The function effectively determines whether the graph is a directed path or not.

