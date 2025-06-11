#State of the program right berfore the function call: a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l <= r < len(a), and ops is a list of tuples of two non-negative integers.
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: *a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l <= r < len(a) and l is equal to r, ops is a list of tuples of two non-negative integers. If the value at index l is not 0, the last tuple in ops is (l, l).
        return
        #The program returns nothing because there is no return statement in the code snippet.
    #State: a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l < r < len(a), and ops is a list of tuples of two non-negative integers.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `a` is a list of non-negative integers, `l` is a non-negative integer, `r` is a non-negative integer such that `l` < `r` < `len(a)`, `ops` is a list of tuples of two non-negative integers, `ops` contains the tuple `(l, r)`, `a[l]` is equal to `r - l + 1`, `a[l + 1]` is equal to `r - l + 1`, ..., `a[r]` is equal to `r - l + 1`, `i` is `r`.
        func_1(a, l + 1, r, ops)
    #State: *`a` is a list of non-negative integers, `l` is a non-negative integer, `r` is a non-negative integer such that `l` < `r` < `len(a)`, `ops` is a list of tuples of two non-negative integers. If `a[l]` is not equal to `r - l + 1`, then `ops` contains the tuple `(l, r)`, `a[l]` is equal to `r - l + 1`, `a[l + 1]` is equal to `r - l + 1`, ..., `a[r]` is equal to `r - l + 1`, `i` is `r`, and the function `func_1` has been called with arguments `a`, `l + 1`, `r`, and `ops`. Otherwise, no changes are made.

#Overall this is what the function does:This function modifies a list of non-negative integers by recursively checking and updating segments of the list. It takes four parameters: a list `a`, and three non-negative integers `l`, `r`, and `ops`. The function ensures that all elements in the list between indices `l` and `r` (inclusive) are equal to the length of this segment (`r - l + 1`). If any element in this range does not match this condition, the function records the operation in the `ops` list and updates the elements in the range to the correct value. The function returns no value, as it modifies the input list in-place.

#State of the program right berfore the function call: a is a list of non-negative integers.
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns a tuple containing the sum of all non-negative integers in list 'a', the length of the empty list 'ops' which is 0, and the empty list 'ops' itself.

#Overall this is what the function does:This function calculates the sum of all non-negative integers in a given list 'a' and returns the sum along with an empty list 'ops' and its length, which is 0. The function does not modify the input list 'a' or perform any operations that affect external state. It solely computes and returns the sum and the empty list information.

#State of the program right berfore the function call: l and r are non-negative integers such that 0 <= l <= r < len(a), and a is a list of non-negative integers.
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `l` and `r` are non-negative integers such that `l` is less than or equal to `r`, `i` is `r`, `a` is a list of non-negative integers where all elements from index `l` to `r` (inclusive) are `r - l + 1`, `s` is the sum of the elements in `a` from index `l` to `r` (inclusive) plus `r - l + 1 - a[l]`, and `ops` is a list of tuples where the last tuple is (`l`, `r`).
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: *`l` and `r` are non-negative integers such that 0 <= l <= r < len(a), `a` is a list of non-negative integers, `s` is the sum of the elements in `a` from index `l` to `r` (inclusive), `s` is greater than (r - l + 1) * (r - l + 1), `mx` is the maximum value in the sublist of `a` from index `l` to `r` (inclusive), and the current value of `pos` is the index of `mx` in the entire list `a`. If `pos` is not equal to `l`, a recursive call to `recursive_maximize_sum` with arguments `l` and `pos - 1` has been made, and the value returned by this recursive call has been returned.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: *`l` and `r` are non-negative integers such that 0 <= l <= r < len(a), `a` is a list of non-negative integers, `s` is the sum of the elements in `a` from index `l` to `r` (inclusive), `s` is greater than (r - l + 1) * (r - l + 1), `mx` is the maximum value in the sublist of `a` from index `l` to `r` (inclusive), and the current value of `pos` is the index of `mx` in the entire list `a`. If `pos` is not equal to `r`, a recursive call to `recursive_maximize_sum` with arguments `pos + 1` and `r` has been made, and the value returned by this recursive call has been returned. If `pos` is equal to `r`, no further recursive calls are made.
    #State: *`l` and `r` are non-negative integers such that 0 <= l <= r < len(a), `a` is a list of non-negative integers. If the sum of the elements in `a` from index `l` to `r` (inclusive) is less than or equal to (r - l + 1) * (r - l + 1), then all elements from index `l` to `r` (inclusive) are set to `r - l + 1`, `s` is updated to the sum of the elements in `a` from index `l` to `r` (inclusive) plus `r - l + 1 - a[l]`, and `ops` is updated with the tuple (`l`, `r`). Otherwise, if the sum of the elements in `a` from index `l` to `r` (inclusive) is greater than (r - l + 1) * (r - l + 1), then `mx` is the maximum value in the sublist of `a` from index `l` to `r` (inclusive), and the current value of `pos` is the index of `mx` in the entire list `a`. If `pos` is not equal to `r`, a recursive call to `recursive_maximize_sum` with arguments `pos + 1` and `r` has been made, and the value returned by this recursive call has been returned. If `pos` is equal to `r`, no further recursive calls are made.

#Overall this is what the function does:This function, `recursive_maximize_sum`, takes a list of non-negative integers `a` and two indices `l` and `r` as input, where `0 <= l <= r < len(a)`. It modifies the list `a` by either setting all elements from index `l` to `r` to `r - l + 1` if the sum of these elements is less than or equal to `(r - l + 1) * (r - l + 1)`, or recursively maximizing the sum of the elements in the sublists `a[l:pos]` and `a[pos+1:r+1]` if the sum is greater than `(r - l + 1) * (r - l + 1)`, where `pos` is the index of the maximum value in the sublist `a[l:r+1]`. The function also keeps track of the operations performed by appending the tuple `(l, r)` to the list `ops` when setting all elements to `r - l + 1`. The function returns no value, but modifies the input list `a` and the list `ops` in place.

#State of the program right berfore the function call: stdin contains two inputs: first an integer and then a space-separated list of integers. The integer is a positive integer and is equal to the length of the list. The list contains non-negative integers.
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s (which is the sum of the elements in the list a), m (which is the maximum element in the list a)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: n is a positive integer, a is a list of non-negative integers, s is the sum of the elements in a, m is the maximum element in a, ops is a list of pairs of integers, stdin is empty, the sum of the elements in a which is s and the maximum element in a which is m are being printed, and all pairs of integers in ops have been printed.

#Overall this is what the function does:The function reads a positive integer and a list of non-negative integers from standard input, calculates the sum and maximum of the list, and prints these values along with pairs of integers. The function does not return any values, but rather prints the results directly.

