#State of the program right berfore the function call: a is a list of positive integers, x is a list of non-zero integers, k is a positive integer, and len(a) = len(x).
    n = len(a)
    sorted_indices = sorted(range(n), key=lambda i: abs(x[i]))
    distance = 0
    pos = 0
    while pos != len(sorted_indices):
        if abs(x[sorted_indices[pos]]) == distance:
            return False
        
        rest = k
        
        while rest != 0 and pos != len(sorted_indices):
            delta = min(rest, a[sorted_indices[pos]])
            rest -= delta
            a[sorted_indices[pos]] -= delta
            if a[sorted_indices[pos]] == 0:
                pos += 1
        
        distance += 1
        
    #State: `a` is a list of non-negative integers, `x` is a list of non-zero integers, `k` is a positive integer, `n` is a positive integer equal to the length of `a`, `sorted_indices` is a list of indices of `a` sorted by the absolute values of the corresponding elements in `x`, `distance` is a positive integer, `pos` is equal to the length of `sorted_indices`.
    return True
    #The program returns a boolean value of True.

#Overall this is what the function does:This function determines whether it is possible to reduce all elements in list `a` to zero by iteratively subtracting a maximum of `k` from the elements in `a`, where the order of subtraction is determined by the absolute values of the corresponding elements in list `x`. The function returns `True` if all elements in `a` can be reduced to zero, and `False` otherwise.

#State of the program right berfore the function call: a is a list of non-negative integers, x is a list of non-zero integers, k is a positive integer, and len(a) = len(x) = n.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: a is a list of n non-negative integers, x is a list of n non-zero integers, k is a positive integer, n is a positive integer, stdin is empty, and either 'YES' or 'NO' is printed depending on the return value of func_1(a, x, k), and either 'YES' or 'NO' is printed depending on the return value of func_1(a, x, k), t is greater than or equal to 0.

#Overall this is what the function does:Determines whether a given condition is met for a list of non-negative integers 'a' and a list of non-zero integers 'x' with a positive integer 'k' as a parameter, and returns a boolean value indicating whether the condition is satisfied or not.

