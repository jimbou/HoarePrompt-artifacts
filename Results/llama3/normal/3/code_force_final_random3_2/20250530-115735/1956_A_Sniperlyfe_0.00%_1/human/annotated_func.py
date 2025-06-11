#State of the program right berfore the function call: n is a non-negative integer and p is a list of non-negative integers.
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is 0, p is a list of non-negative integers.
    return n
    #The program returns 0.

#Overall this is what the function does:The function takes a non-negative integer n and a list of non-negative integers p as input, and returns 0 after repeatedly subtracting the count of elements in p that are less than or equal to n from n, until n is less than the minimum value in p.

#State of the program right berfore the function call: n is a positive integer, p is a list of positive integers such that all elements in p are less than or equal to n and p is sorted in ascending order.
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        res = []
        
        for n in qs:
            res.append(func_1(n, p))
            print(' '.join(map(str, res)))
        
    #State: k is an integer, q is an integer, p is a list of positive integers, qs is an empty list, res is a list containing the results of func_1(n, p) for all n in the initial qs, t is 0, stdin is empty, and the results of func_1(n, p) for all n in the initial qs are printed as a string of space-separated integers.

#Overall this is what the function does:The function reads a series of inputs from the user, including a number of test cases, a pair of integers (k and q), a sorted list of positive integers (p), and a list of query integers (qs). It then iterates over each query integer, calls another function (func_1) with the query integer and the list of positive integers as arguments, appends the result to a list (res), and prints the list of results as a string of space-separated integers. After processing all test cases, the function leaves the input stream empty and the query list empty, with the results of the function calls stored in the result list.

