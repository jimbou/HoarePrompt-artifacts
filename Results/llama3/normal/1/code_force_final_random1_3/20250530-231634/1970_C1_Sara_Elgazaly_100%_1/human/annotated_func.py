#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t (n is an integer such that 2 <= n <= 2*10^5 and t is 1), then n-1 lines each containing two integers u and v (1 <= u, v <= n), and finally one integer u_1 (1 <= u_1 <= n).
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: x is an integer equal to 1, y is 1, lst is a dictionary with one key-value pair where the key is a and the value is a list containing b x-1 times, rev is a dictionary with one key-value pair where the key is b and the value is a list containing a x-1 times, stdin contains one integer u_1
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: x is an integer equal to 2, y is 1, lst is a dictionary with one key-value pair where the key is a and the value is an empty list, rev is a dictionary with one key-value pair where the key is b and the value is a list containing a x-1 times, z is an integer equal to u_1, tmp is a, one is True, stdin is empty
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: x is 2, y is 1, lst is a dictionary with one key-value pair where the key is a and the value is an empty list, rev is a dictionary with one key-value pair where the key is b and the value is an empty list, z is an integer equal to u_1, tmp is None, two is True, one is True, stdin is empty
    print('Hermione' if two and one else 'Ron')
    #This is printed: Hermione

#Overall this is what the function does:This function reads input from stdin, constructs two directed graphs (lst and rev) from the input, and then performs a series of operations on these graphs. It iterates through the graphs in a specific order, toggling a boolean value (one and two) at each step. Finally, it prints 'Hermione' if both boolean values are True after the iterations, otherwise it prints 'Ron'. The function does not return any value, and its only output is the printed string.

