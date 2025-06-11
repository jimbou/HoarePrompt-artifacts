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
        
    #State: pos = len(sorted_indices), distance = number of iterations of the outer while loop, a contains the updated values after the loop execution, x remains unchanged, k remains unchanged, n remains unchanged, sorted_indices remains unchanged.
    return True
    #The program returns True

#Overall this is what the function does:This function determines whether it is possible to iteratively reduce a list of positive integers (a) to zero, based on a list of non-zero integers (x) and a positive integer (k). It returns True if the reduction is possible and False otherwise. The function modifies the list (a) in place, but leaves the lists (x) and the integer (k) unchanged.

#State of the program right berfore the function call: a is a list of non-negative integers, x is a list of non-zero integers, k is a non-negative integer, len(a) = len(x) = n, and n and k are the same as in the problem description.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: Output State: The loop will execute `t` times, and in each iteration, it will read two integers `n` and `k`, and two lists of integers `a` and `x` from the input. It will then print 'YES' if the function `func_1(a, x, k)` returns True, and 'NO' otherwise. The values of `n`, `k`, `a`, and `x` will be updated in each iteration, but the value of `t` will remain the same. After the loop finishes, the values of `n`, `k`, `a`, and `x` will be the ones read in the last iteration, and `t` will still be the same as in the initial state.

#Overall this is what the function does:Determines whether a given condition is met for a list of non-negative integers `a`, a list of non-zero integers `x`, and a non-negative integer `k`. Returns `True` if the condition is met, and `False` otherwise.

