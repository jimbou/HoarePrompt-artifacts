#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer (2 <= n <= 2*10^5) and t is 1, then n-1 lines each containing two integers u and v (1 <= u, v <= n), and finally one line containing one integer u (1 <= u <= n).
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: x is an integer equal to 1, y is 1, lst is a dictionary with default value of empty list and lst[a] is a list containing all the values of b, rev is a dictionary with default value of empty list and rev[b] is a list containing all the values of a, stdin contains no lines.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: Output State: x is 1, y is 1, lst is a dictionary with default value of empty list and lst[a] is a list containing all the values of b and lst[tmp] is an empty list, rev is a dictionary with default value of empty list and rev[b] is a list containing all the values of a, z is an integer, tmp is an integer equal to the last value in lst[tmp], one is True, stdin contains no lines.
    #
    #The output state after the loop executes all the iterations is the same as the initial state, except for the values of the variables in the loop head and body. The loop continues to execute until lst[tmp] is empty, at which point it terminates. The final state of the variables is as follows:
    #
    #* x and y remain unchanged at 1.
    #* lst remains a dictionary with default value of empty list, and lst[a] remains a list containing all the values of b. However, lst[tmp] is now an empty list, as the loop has popped all the values from it.
    #* rev remains a dictionary with default value of empty list, and rev[b] remains a list containing all the values of a.
    #* z remains an integer, but its value is not specified.
    #* tmp is an integer equal to the last value in lst[tmp], which is now empty.
    #* one is True, as the loop has executed an even number of times (since lst[tmp] is empty).
    #* stdin contains no lines, as it was not affected by the loop.
    #
    #In summary, the loop has executed until lst[tmp] is empty, and the final state of the variables reflects this.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: x is 1, y is 1, lst is a dictionary with default value of empty list and lst[a] is a list containing all the values of b, rev is a dictionary with default value of empty list and rev[b] is an empty list, z is equal to b, tmp is an integer equal to one value of a, two is True, one is True, stdin contains no lines.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Hermione

#Overall this is what the function does:Determines whether a given graph is bipartite by traversing it from a specified starting node, and prints 'Hermione' if the graph is bipartite and 'Ron' otherwise.

