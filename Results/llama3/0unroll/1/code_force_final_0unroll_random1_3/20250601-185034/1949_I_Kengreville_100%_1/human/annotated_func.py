#State of the program right berfore the function call: stdin contains n+1 inputs: first an integer n (1 ≤ n ≤ 1000), then n lines each containing three integers x, y, and r (−10^9 ≤ x, y ≤ 10^9 and 1 ≤ r ≤ 10^9).
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: The values of x, y, and r are lists of n integers, where each integer is one of the three integers input from stdin for each iteration of the loop. The values of visited, coef, and stdin remain unchanged.
    tot = 0
    bipartite = True
    ok = False
    for i in range(n):
        if not visited[i]:
            coef[i] = 1
            tot = 0
            bipartite = True
            dfs(i)
            ok = ok or bipartite and tot != 0
        
    #State: Output State: The output state after the loop executes all the iterations is as follows: x, y, and r are lists of n integers, where each integer is one of the three integers input from stdin for each iteration of the loop. visited, coef, and stdin remain unchanged. tot is 0, bipartite is True, and ok is False.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *x, y, and r are lists of n integers, where each integer is one of the three integers input from stdin for each iteration of the loop. visited, coef, and stdin remain unchanged. tot is 0, bipartite is True. If ok is True, 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads n+1 inputs from stdin, where n is an integer followed by n lines each containing three integers x, y, and r. It then processes these inputs and checks for a specific condition. If the condition is met, it prints 'YES', otherwise it prints 'NO'. The function does not modify the input values or any external state, and its output is solely based on the input values.

