#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer between 2 and 200000 inclusive and t is 1, then n-1 lines each containing two integers u and v, where u and v are integers between 1 and n inclusive, and finally one integer u, where u is an integer between 1 and n inclusive.
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: The variable "i" is now equal to n - 1, the variable "nodes" is now a defaultdict of lists where each key is a node and its corresponding value is a list of its adjacent nodes, and the variable "stdin" is now empty.
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: Output State: The variable "i" is now equal to n - 1, the variable "nodes" is now a defaultdict of lists where each key is a node and its corresponding value is a list of its adjacent nodes, the variable "ends" is now a list of nodes that have only one adjacent node, and the variable "stdin" is now empty.
    s, e = list(ends)
    tree = [s]
    prev = s
    curr = nodes[s][0]
    while curr != e:
        tree.append(curr)
        
        if nodes[curr][0] == prev:
            prev = curr
            curr = nodes[curr][1]
        else:
            prev = curr
            curr = nodes[curr][0]
        
    #State: Output State: The variable "s" is still equal to the first node in the list "ends", the variable "e" is still equal to the second node in the list "ends", the variable "tree" is now a list containing all the nodes in the path from the first node in the list "ends" to the second node in the list "ends", the variable "prev" is now equal to the second node in the list "ends", and the variable "curr" is now equal to the second node in the list "ends". The variable "i" is still equal to n - 1, the variable "nodes" is still a defaultdict of lists where each key is a node and its corresponding value is a list of its adjacent nodes, the variable "ends" is still a list of nodes that have only one adjacent node, and the variable "stdin" is still empty.
    #
    #In natural language, the output state after the loop executes all the iterations is that the variable "tree" now contains all the nodes in the path from the first node in the list "ends" to the second node in the list "ends", and the variables "prev" and "curr" are now equal to the second node in the list "ends". The other variables remain unchanged.
    tree.append(e)
    start = int(input())
    idx = tree.index(start)
    moves = [idx, n - idx - 1]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: The variables "s", "e", "tree", "prev", "curr", "i", "nodes", "ends", and "stdin" retain their values as described in the precondition. The variable "start" is equal to the integer read from stdin, and the variable "idx" is equal to the index of the start node in the tree. The variable "moves" is a list containing the index of the start node and the number of moves required to reach the end of the tree from the start node. If at least one move in the list "moves" has an odd value, 'Ron' is printed. Otherwise, all moves in the list "moves" are even, and 'Hermione' is printed.

#Overall this is what the function does:Functionality: This function reads input from stdin, constructs a graph from the input, finds a path between two nodes with only one adjacent node, and determines whether a given start node is closer to the beginning or end of the path. It then prints 'Ron' if the number of moves to reach the end of the path from the start node is odd, and 'Hermione' otherwise.

