#State of the program right berfore the function call: a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l <= r < len(a), and ops is a list of tuples of non-negative integers.
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: *a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l <= r < len(a) and l is equal to r, ops is a list of tuples of non-negative integers. If a[l] is not equal to 0, a[l] is set to 0 and an additional tuple (l, l) is added to ops. Otherwise, no changes are made.
        return
        #The program returns nothing, as there is no explicit return statement. The state of the variables remains unchanged, with 'a' being a list of non-negative integers, 'l' and 'r' being non-negative integers such that 0 <= l <= r < len(a) and l is equal to r, and 'ops' being a list of tuples of non-negative integers.
    #State: *a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l < r < len(a), and ops is a list of tuples of non-negative integers.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: The list `a` has been modified such that all elements from index `l` to `r` (inclusive) have been set to `r - l + 1`. The values of `l`, `r`, and `ops` remain unchanged.
        func_1(a, l + 1, r, ops)
    #State: *`a` is a list of non-negative integers, `l` is a non-negative integer, `r` is a non-negative integer such that `l < r < len(a)`, `ops` is a list of tuples of non-negative integers. If `a[l]` is not equal to `r - l + 1`, then all elements from index `l + 1` to `r` (inclusive) in list `a` have been set to `r - (l + 1) + 1`. Otherwise, the list `a` remains unchanged. The values of `l`, `r`, and `ops` remain unchanged.

#Overall this is what the function does:This function modifies a list of non-negative integers `a` by setting all elements within a specified range (`l` to `r`) to the length of that range (`r - l + 1`), if the first element of the range does not already match this value. It also keeps track of the operations performed by appending tuples representing the modified ranges to a list `ops`. The function recursively processes the list, starting from the first element of the range and moving towards the end. If the range consists of a single element, it sets that element to 0 if it is not already 0, and appends the corresponding operation to `ops`.

#State of the program right berfore the function call: a is a list of non-negative integers.
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns a tuple containing the sum of all non-negative integers in list 'a', the length of the empty list 'ops' which is 0, and the empty list 'ops' itself.

#Overall this is what the function does:This function calculates the sum of all non-negative integers in a given list 'a' and returns the sum along with the length and contents of an empty list 'ops'. The function does not modify the input list 'a' and does not perform any operations that affect external state. The returned tuple contains the sum of the non-negative integers in 'a', the length of the empty list 'ops' (which is always 0), and the empty list 'ops' itself.

#State of the program right berfore the function call: l and r are integers such that 0 <= l <= r < len(a), a is a list of non-negative integers.
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `a` is a list of non-negative integers, `l` and `r` are integers such that 0 <= `l` <= `r` < len(`a`), `s` is the sum of the integers in `a` from index `l` to `r` (inclusive), `s` is less than or equal to the square of the number of elements in the subarray from `l` to `r` (inclusive), and `ops` is a list containing the tuple (`l`, `r`).
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: *l is an integer such that 0 <= l <= r < len(a), r is an integer such that 0 <= l <= r < len(a), a is a list of non-negative integers, s is the sum of the integers in a from index l to r (inclusive), s is greater than (r - l + 1) * (r - l + 1), mx is the maximum value in the sublist a[l:r+1], and pos is the index of mx in the original list a. If the current value of pos is not equal to l, the function recursive_maximize_sum has been called with arguments l and pos - 1, and its return value has been returned. Otherwise, no further action has been taken.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: *`l` is an integer such that 0 <= l <= r < len(a), `r` is an integer such that 0 <= l <= r < len(a), `a` is a list of non-negative integers, `s` is the sum of the integers in `a` from index `l` to `r` (inclusive), `s` is greater than (r - l + 1) * (r - l + 1), `mx` is the maximum value in the sublist `a[l:r+1]`, and `pos` is the index of `mx` in the original list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum` has been called with arguments `pos + 1` and `r`, and its return value has been returned. If `pos` is equal to `r`, no further action has been taken.
    #State: *`a` is a list of non-negative integers, `l` and `r` are integers such that 0 <= `l` <= `r` < len(`a`), `s` is the sum of the integers in `a` from index `l` to `r` (inclusive). If `s` is less than or equal to the square of the number of elements in the subarray from `l` to `r` (inclusive), then `ops` is a list containing the tuple (`l`, `r`). Otherwise, `s` is greater than the square of the number of elements in the subarray from `l` to `r` (inclusive), `mx` is the maximum value in the sublist `a[l:r+1]`, and `pos` is the index of `mx` in the original list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum` has been called with arguments `pos + 1` and `r`, and its return value has been returned. If `pos` is equal to `r`, no further action has been taken.

#Overall this is what the function does:This function, `recursive_maximize_sum`, takes a list of non-negative integers `a` and two integers `l` and `r` as input, where `0 <= l <= r < len(a)`. It calculates the sum `s` of the integers in `a` from index `l` to `r` (inclusive) and checks if `s` is less than or equal to the square of the number of elements in the subarray from `l` to `r` (inclusive). If true, it calls `func_1(a, l, r, ops)`, appends the tuple `(l, r)` to `ops`, and sets all elements in `a` from index `l` to `r` to `r - l + 1`. If `s` is greater than the square of the number of elements in the subarray from `l` to `r` (inclusive), it finds the maximum value `mx` in the sublist `a[l:r+1]` and its index `pos` in the original list `a`. If `pos` is not equal to `l`, it recursively calls itself with arguments `l` and `pos - 1`. If `pos` is not equal to `r`, it recursively calls itself with arguments `pos + 1` and `r`. The function modifies the input list `a` and the list `ops` based on the conditions met.

#State of the program right berfore the function call: stdin contains two inputs: first an integer n and then a space-separated list of n integers. The integer n is a positive integer and less or equal than 18. The integers in the list are non-negative and less or equal than 10^7.
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s (the first output value of func_2(a)) and m (the second output value of func_2(a))
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: Output State: The values of l and r have been updated to the last pair of values in ops, and the values of l + 1 and r + 1 have been printed for each pair of values in ops. The values of n, a, s, and m remain unchanged.

#Overall this is what the function does:This function reads input from stdin, expecting a positive integer n (1 ≤ n ≤ 18) followed by a space-separated list of n non-negative integers (each ≤ 10^7). It then processes this list using the func_2 function, which returns three values: s, m, and ops. The function prints the values of s and m, followed by the pairs of values in ops, where each pair is incremented by 1. The function does not modify the input values n, a, s, or m, and its output consists of the printed values of s, m, and the incremented pairs from ops.

