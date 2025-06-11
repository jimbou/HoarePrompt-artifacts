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
        
    #State: pos is equal to the length of sorted_indices, distance is equal to the maximum absolute value of the elements in x plus one, and the elements of a are either zero or positive integers.
    return True
    #The program returns True

#Overall this is what the function does:This function determines whether it is possible to reduce all elements in list 'a' to zero by iteratively subtracting a certain amount 'k' from the elements in 'a', where the order of subtraction is determined by the absolute values of the corresponding elements in list 'x'. The function returns True if all elements in 'a' can be reduced to zero, and False otherwise.

#State of the program right berfore the function call: a is a list of non-negative integers, x is a list of non-zero integers, k is a non-negative integer such that len(a) == len(x) and 0 <= k <= 2 * 10^9.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: Output State: `t` number of lines, each containing either 'YES' or 'NO'.

#Overall this is what the function does:Determines whether a given list of non-negative integers `a` and a list of non-zero integers `x` can be combined in a way that satisfies a certain condition related to the non-negative integer `k`, returning `True` if possible and `False` otherwise.

