#State of the program right berfore the function call: n is a non-negative integer and p is a list of non-negative integers such that all elements in p are less than or equal to n.
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is 0 and p remains unchanged.
    return n
    #The program returns 0.

#Overall this is what the function does:This function takes a non-negative integer n and a list of non-negative integers p as input, and repeatedly subtracts the count of elements in p that are less than or equal to n from n, until n is less than the minimum value in p. The function returns 0, leaving the input list p unchanged.

#State of the program right berfore the function call: n is a positive integer and p is a list of positive integers such that for all i, 1 <= p[i] <= n.
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        res = []
        
        for n in qs:
            res.append(func_1(n, p))
            print(' '.join(map(str, res)))
        
    #State: The output state is the same as the initial state, with the values of `k`, `q`, `p`, `qs`, and `res` changed after each iteration of the loop. The final output state will have the values of `k`, `q`, `p`, `qs`, and `res` from the last iteration of the loop. The values of `n` and `t` remain unchanged.

#Overall this is what the function does:This function takes no arguments and returns no values. It reads input from the user, processes it, and prints the results. The input consists of a number of test cases, each containing a positive integer k, a positive integer q, a list of positive integers p, and a list of positive integers qs. For each test case, the function calls another function func_1 with each element of qs and the list p as arguments, appends the result to a list res, and prints the current state of res after each call. The function does not modify the input values or have any side effects beyond printing the results.

