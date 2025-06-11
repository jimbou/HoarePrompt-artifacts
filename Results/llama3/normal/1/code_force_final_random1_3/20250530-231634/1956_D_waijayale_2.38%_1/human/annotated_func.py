#State of the program right berfore the function call: a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l <= r < len(a), ops is a list of tuples of two integers.
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: *a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l <= r < len(a), ops is a list of tuples of two integers. If a[l] is not equal to 0, then the last tuple in ops is (l, l).
        return
        #The program returns nothing
    #State: a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l < r < len(a), ops is a list of tuples of two integers.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `a` is a list of non-negative integers where `a[l]` is equal to `r - l + 1`, `a[l + 1]` is equal to `r - l + 1`, ..., `a[r]` is equal to `r - l + 1`, `l` is a non-negative integer, `r` is a non-negative integer such that `l` < `r` < `len(a)`, `ops` is a list of tuples of two integers including the new tuple `(l, r)`, `func_1` has been called with arguments `a`, `l + 1`, `r`, and `ops`, `i` is `r`.
        func_1(a, l + 1, r, ops)
    #State: *`a` is a list of non-negative integers, `l` is a non-negative integer, `r` is a non-negative integer such that `l` < `r` < `len(a)`, `ops` is a list of tuples of two integers. If `a[l]` is not equal to `r - l + 1`, then `a[l]` is equal to `r - l + 1`, `a[l + 1]` is equal to `r - l + 1`, ..., `a[r]` is equal to `r - l + 1`, `ops` includes the new tuple `(l, r)`, `i` is `r`, and the function `func_1` has been called with arguments `a`, `l + 1`, `r`, and `ops`.

#Overall this is what the function does:This function modifies a list of non-negative integers `a` and a list of operations `ops` based on the range defined by non-negative integers `l` and `r`. If `l` equals `r`, it checks if the element at index `l` in `a` is not zero, and if so, it appends an operation `(l, l)` to `ops` and sets the element at index `l` in `a` to zero. If `l` is less than `r`, it recursively calls itself with the range `l + 1` to `r`. If the element at index `l` in `a` is not equal to `r - l + 1`, it appends an operation `(l, r)` to `ops`, sets all elements in the range `l` to `r` in `a` to `r - l + 1`, and then recursively calls itself again with the same range. The function does not return any value.

#State of the program right berfore the function call: a is a list of non-negative integers
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all non-negative integers in list 'a', the length of the empty list 'ops' which is 0, and the empty list 'ops'.

#Overall this is what the function does:This function takes a list of non-negative integers as input, calculates the sum of all integers in the list, and returns the sum along with an empty list and its length (which is 0). The function does not modify the input list.

#State of the program right berfore the function call: l and r are non-negative integers such that 0 <= l <= r < len(a), and a is a list of non-negative integers.
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: l and r are non-negative integers such that 0 <= l < r + 1 < len(a), a is a list of non-negative integers where all elements from index l to r (inclusive) are r - l + 1, s is the sum of the integers in a from index l to r (inclusive) minus the original sum of the integers in a from index l to r (inclusive) plus (r - l + 1)^2, s is less than or equal to the square of the number of elements in the subarray from l to r (inclusive), ops is a list containing a tuple (l, r), i is r.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: l and r are non-negative integers such that 0 <= l <= r < len(a), a is a list of non-negative integers, s is the sum of the integers in a from index l to r (inclusive), mx is the maximum value in a from index l to r (inclusive), and pos is the index of mx in a. If pos is not equal to l, the function recursive_maximize_sum(l, pos - 1) has been called and its return value has been returned. Otherwise, no further action has been taken.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: *l and r are non-negative integers such that 0 <= l <= r < len(a), a is a list of non-negative integers, s is the sum of the integers in a from index l to r (inclusive), mx is the maximum value in a from index l to r (inclusive), and pos is the index of mx in a. If pos is not equal to r, the function recursive_maximize_sum(pos + 1, r) has been called and its return value has been returned. Otherwise, no further action has been taken.
    #State: *`l` and `r` are non-negative integers such that 0 <= l <= r < len(a), `a` is a list of non-negative integers, and `s` is the sum of the integers in `a` from index `l` to `r` (inclusive). If `s` is less than or equal to the square of the number of elements in the subarray from `l` to `r` (inclusive), all elements from index `l` to `r` (inclusive) are set to `r - l + 1`, `s` is updated to be the sum of the integers in `a` from index `l` to `r` (inclusive) minus the original sum of the integers in `a` from index `l` to `r` (inclusive) plus `(r - l + 1)^2`, and `ops` is a list containing a tuple `(l, r)`. Otherwise, if the maximum value in `a` from index `l` to `r` (inclusive) is not at index `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called and its return value has been returned. Otherwise, no further action has been taken.

#Overall this is what the function does:This function maximizes the sum of a subarray within a given list of non-negative integers. It takes two parameters, `l` and `r`, representing the start and end indices of the subarray, and modifies the original list in-place. If the sum of the subarray is less than or equal to the square of the number of elements in the subarray, it sets all elements in the subarray to the length of the subarray and appends the indices to an operations list. Otherwise, it recursively calls itself on the left and right halves of the subarray, centered around the maximum value in the subarray. The function returns no value but modifies the original list and operations list accordingly.

#State of the program right berfore the function call: stdin contains two inputs: first an integer n and then a space-separated list of n integers. The integer n is a positive integer and less or equal than 18. The integers in the list are non-negative integers and less or equal than 10^7.
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s (which is the sum of the elements in the list a), m (which is the maximum element in the list a)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: n is a positive integer less or equal than 18, a is a list of n non-negative integers less or equal than 10^7, s is the sum of the elements in a, m is the maximum element in a, ops is an empty collection of pairs (l, r), stdin is empty, the sum of the elements in a which is s and the maximum element in a which is m are printed, and the value of l + 1 and r + 1 are printed for each pair (l, r) in ops.

#Overall this is what the function does:This function reads two inputs from stdin: a positive integer n (less than or equal to 18) and a space-separated list of n non-negative integers (each less than or equal to 10^7). It then calculates the sum and maximum value of the integers in the list, and prints these values. Additionally, it prints pairs of values (l+1, r+1) for each pair (l, r) in an empty collection of pairs, although since the collection is empty, no such pairs are actually printed. The function does not modify the input list or perform any other actions beyond reading input and printing output.

