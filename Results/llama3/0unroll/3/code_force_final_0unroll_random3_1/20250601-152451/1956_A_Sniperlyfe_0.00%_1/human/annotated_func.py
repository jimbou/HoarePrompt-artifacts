#State of the program right berfore the function call: n is a non-negative integer and p is a list of non-negative integers such that all elements in p are less than or equal to n.
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is 0 and p remains unchanged.
    return n
    #The program returns the value of n, which is 0.

#Overall this is what the function does:This function takes a non-negative integer n and a list of non-negative integers p as input, and returns 0 after repeatedly subtracting the count of elements in p that are less than or equal to n from n, until n is less than the minimum value in p. The list p remains unchanged throughout the process.

#State of the program right berfore the function call: n is a positive integer and p is a list of positive integers such that all elements in p are less than or equal to n and p is sorted in ascending order.
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        res = []
        
        for n in qs:
            res.append(func_1(n, p))
            print(' '.join(map(str, res)))
        
    #State: The output state after the loop executes all the iterations is that the list `p` has been updated with new values from the input, and the variable `res` contains the results of applying the function `func_1` to each element in the list `qs` with the updated list `p`. The values of `n` and `t` remain unchanged.

#Overall this is what the function does:The function takes a positive integer `n` and a sorted list of positive integers `p` as input, and returns a list of results by applying the function `func_1` to each element in the list `qs` with the updated list `p`. The function updates the list `p` with new values from the input and prints the results after each iteration. The values of `n` and `t` remain unchanged.

