#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer between 2 and 2 * 10^5 inclusive, and t is 1. Then n-1 lines each containing two integers u and v, where u and v are integers between 1 and n inclusive. Then one line containing one integer u, where u is an integer between 1 and n inclusive.
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: lst is a dictionary where each key is a node in a graph and its corresponding value is a list of its children, and rev is a dictionary where each key is a node in the graph and its corresponding value is a list of its parents.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: lst[tmp] is an empty list, one is False if the initial value of z is even and True if the initial value of z is odd, tmp is the last node visited in the graph, rev and z remain unchanged.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: two is True if the initial value of z is even and False if the initial value of z is odd, tmp is equal to the last element of rev[z], rev remains unchanged, z remains unchanged, one remains unchanged.
    print('Hermione' if two and one else 'Ron')
    #This is printed: 'Hermione' if the initial value of z is even and one is True, otherwise 'Ron'

#Overall this is what the function does:This function reads input from stdin, constructs a graph from the input, and then traverses the graph in both forward and backward directions from a given node. It keeps track of whether the number of nodes visited in each direction is even or odd and prints 'Hermione' if both counts are even and 'Ron' otherwise.

