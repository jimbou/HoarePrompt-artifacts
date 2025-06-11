#State of the program right berfore the function call: n is a non-negative integer and p is a list of non-negative integers such that all elements in p are less than or equal to n.
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is 0 and p remains unchanged.
    return n
    #The program returns 0

#Overall this is what the function does:The function reduces a non-negative integer `n` to 0 by repeatedly subtracting the count of elements in list `p` that are less than or equal to `n`, until `n` is less than the minimum value in `p`, and returns the final value of `n`, which is always 0. The list `p` remains unchanged throughout the process.

#State of the program right berfore the function call: n is a positive integer and p is a list of positive integers such that for all i, j in p, i < j and 1 <= i <= 100.
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        res = []
        
        for n in qs:
            res.append(func_1(n, p))
            print(' '.join(map(str, res)))
        
    #State: The output state after the loop executes all the iterations is that the list `p` is updated with new values from the input, and the variable `res` contains the results of applying the function `func_1` to each element in the list `qs` with the updated list `p`. The values of `n` and `t` remain unchanged.

#Overall this is what the function does:This function reads input from the user, processes it, and prints the results. It takes no arguments and returns no values. The function iterates over a specified number of test cases, where each case involves reading a list of positive integers and a list of query values. For each query value, the function applies another function (`func_1`) to the query value and the list of positive integers, and appends the result to a list of results. The function then prints the list of results. The function does not modify the input values, but it does update the list of positive integers for each test case.

