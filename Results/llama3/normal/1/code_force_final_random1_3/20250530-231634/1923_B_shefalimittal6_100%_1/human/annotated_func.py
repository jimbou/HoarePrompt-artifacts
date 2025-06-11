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
        
    #State: `a` is a list of non-negative integers, `x` is a list of non-zero integers, `k` is a positive integer, `n` is a positive integer equal to the length of `a` (and `x`), `sorted_indices` is a list of indices of elements in `x` sorted by their absolute values, `distance` is a non-negative integer, and `pos` is equal to the length of `sorted_indices`.
    return True
    #The program returns True

#Overall this is what the function does:This function takes as input a list of positive integers `a`, a list of non-zero integers `x`, and a positive integer `k`, where the lengths of `a` and `x` are equal. It modifies the list `a` by iteratively reducing the values of its elements based on the sorted absolute values of the elements in `x` and the value of `k`. The function returns `True` if it successfully iterates through all elements in `a` without encountering an element in `x` with an absolute value equal to the current distance, and `False` otherwise. The function also returns `True` if it successfully iterates through all elements in `a` without encountering an element in `x` with an absolute value equal to the current distance, and `False` otherwise.

#State of the program right berfore the function call: a is a list of non-negative integers, x is a list of non-zero integers, k is a non-negative integer, and len(a) = len(x) = n.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: a is a list of n non-negative integers, x is a list of n non-zero integers, k is a non-negative integer, n is a positive integer, stdin is empty, and either 'YES' or 'NO' is printed depending on the return value of func_1(a, x, k)

#Overall this is what the function does:Determines whether a given condition is met for the input lists 'a' and 'x' and integer 'k', and prints 'YES' if the condition is met, otherwise prints 'NO'. The function does not modify the input lists 'a' and 'x' or the integer 'k'.

