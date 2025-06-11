#State of the program right berfore the function call: n is a non-negative integer and p is a list of non-negative integers such that all elements in p are less than or equal to n.
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is a non-negative integer and is equal to n - count where count is the number of elements in p that are less than or equal to the initial value of n, p is a non-empty list of non-negative integers such that the minimum value in p is less than or equal to the initial value of n.
    return n
    #The program returns a non-negative integer n that is equal to the difference between the initial value of n and the count of elements in list p that are less than or equal to the initial value of n.

#Overall this is what the function does:This function takes a non-negative integer `n` and a list of non-negative integers `p` as input, and returns a non-negative integer `n` that is equal to the difference between the initial value of `n` and the count of elements in list `p` that are less than or equal to the initial value of `n`. The function effectively subtracts the count of elements in `p` that are less than or equal to `n` from `n` itself, until `n` is less than the minimum value in `p`.

#State of the program right berfore the function call: n is a positive integer and p is a list of distinct positive integers such that all elements in p are less than or equal to n.
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        res = []
        
        for n in qs:
            res.append(func_1(n, p))
            print(' '.join(map(str, res)))
        
    #State: `n` is the last element in the list `qs`, `p` is a list of distinct positive integers such that all elements in `p` are less than or equal to `n`, `t` is 0, `k` is an integer, `q` is an integer, `p` is a list of integers, `qs` is an empty list, `res` is a list containing the result of `func_1(n, p)` for each element in `qs`, and `stdin` is empty.

#Overall this is what the function does:The function accepts a list of distinct positive integers `p` and a list of positive integers `qs`, and for each integer `n` in `qs`, it calls another function `func_1(n, p)` and appends the result to a list `res`. The function then prints the list `res` containing the results of `func_1(n, p)` for each element in `qs`. After execution, the function leaves the input variables unchanged, with `p` remaining a list of distinct positive integers, `qs` becoming an empty list, and `res` containing the results of `func_1(n, p)` for each element in `qs`.

