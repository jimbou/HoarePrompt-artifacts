#State of the program right berfore the function call: a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l <= r < len(a), ops is a list of tuples of non-negative integers.
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: *a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l <= r < len(a) and l is equal to r, ops is a list of tuples of non-negative integers. If a[l] is not equal to 0, ops has an additional tuple (l, l) appended to it.
        return
        #The program returns nothing, as there is no return statement with a value. The state of the variables remains unchanged. The list 'a' still contains non-negative integers, 'l' and 'r' are still non-negative integers such that 0 <= l <= r < len(a) and l is equal to r, and 'ops' is still a list of tuples of non-negative integers. If a[l] is not equal to 0, ops still has an additional tuple (l, l) appended to it.
    #State: a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l < r < len(a), ops is a list of tuples of non-negative integers.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `a` is a list of non-negative integers, `l` is a non-negative integer, `r` is a non-negative integer such that `l` < `r` < `len(a)`, `ops` is a list of tuples of non-negative integers, `ops` now includes the tuple `(l, r)`, all elements in the sublist `a[l:r+1]` are equal to `r - l + 1`, `i` is `r`.
        #
        #In natural language, after the loop executes all the iterations, the sublist of `a` from index `l` to `r` (inclusive) will have all elements set to `r - l + 1`, and the loop counter `i` will be equal to `r`. The other variables `l`, `r`, and `ops` remain unchanged.
        func_1(a, l + 1, r, ops)
    #State: *`a` is a list of non-negative integers, `l` is a non-negative integer, `r` is a non-negative integer such that `l` < `r` < `len(a)`, `ops` is a list of tuples of non-negative integers. If `a[l]` is not equal to `r - l + 1`, then `ops` includes the tuple `(l, r)`, all elements in the sublist `a[l+1:r+1]` are equal to `r - l`, and `i` is `r`. Otherwise, no changes are made to `a`, `l`, `r`, `ops`, or `i`.

#Overall this is what the function does:This function modifies a list of non-negative integers `a` and a list of tuples `ops` based on the input parameters `l` and `r`. If `l` is equal to `r`, it checks if the element at index `l` in `a` is not equal to 0, and if so, appends a tuple `(l, l)` to `ops` and sets the element at index `l` in `a` to 0. If `l` is not equal to `r`, it recursively calls itself with `l + 1` and `r`, and then checks if the element at index `l` in `a` is not equal to `r - l + 1`. If this condition is true, it appends a tuple `(l, r)` to `ops` and sets all elements in the sublist `a[l:r+1]` to `r - l + 1`, and then recursively calls itself again with `l + 1` and `r`. The function does not return any value.

#State of the program right berfore the function call: a is a list of non-negative integers.
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all non-negative integers in list 'a', the length of an empty list 'ops' which is 0, and the empty list 'ops' itself.

#Overall this is what the function does:This function calculates the sum of all non-negative integers in a given list 'a' and returns the sum along with an empty list 'ops' and its length, which is 0. The function does not modify the input list 'a' or perform any operations that affect external state. It solely computes and returns the sum of non-negative integers in 'a' and an empty list 'ops' with its length.

#State of the program right berfore the function call: l and r are non-negative integers such that 0 <= l <= r < len(a), and a is a list of non-negative integers.
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `l` and `r` are non-negative integers such that 0 <= l <= r < len(a), `a` is a list of non-negative integers, all elements in `a` from index `l` to `r` (inclusive) are equal to `r - l + 1`, `s` is equal to `(r - l + 1)^2`, `ops` is a list containing a tuple of `(l, r)`, `i` is `r`.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: l and r are non-negative integers such that 0 <= l <= r < len(a), a is a list of non-negative integers, s is the sum of the elements in a from index l to r (inclusive), mx is the maximum value in the sublist a[l:r + 1], and the current value of pos is the index of mx in the original list a. If pos is not equal to l, the function recursive_maximize_sum(l, pos - 1) has been called and returned.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: l and r are non-negative integers such that 0 <= l <= r < len(a), a is a list of non-negative integers, s is the sum of the elements in a from index l to r (inclusive), mx is the maximum value in the sublist a[l:r + 1], and the function has recursively maximized the sum for the sublists a[l:pos - 1] and a[pos + 1:r + 1] if pos is not equal to r, otherwise no further recursive calls are made.
    #State: *`l` and `r` are non-negative integers such that 0 <= l <= r < len(a), `a` is a list of non-negative integers, and `s` is the sum of the elements in `a` from index `l` to `r` (inclusive). If `s` is less than or equal to `(r - l + 1)^2`, all elements in `a` from index `l` to `r` (inclusive) are equal to `r - l + 1`, `s` is equal to `(r - l + 1)^2`, `ops` is a list containing a tuple of `(l, r)`, and `i` is `r`. Otherwise, the function has recursively maximized the sum for the sublists `a[l:pos - 1]` and `a[pos + 1:r + 1]` if `pos` is not equal to `r`, or no further recursive calls are made if `pos` is equal to `r`, and `mx` is the maximum value in the sublist `a[l:r + 1]`.

#Overall this is what the function does:This function, `recursive_maximize_sum`, takes a list of non-negative integers `a` and two non-negative integers `l` and `r` as input, where `0 <= l <= r < len(a)`. It modifies the list `a` by either setting all elements from index `l` to `r` to `r - l + 1` if the sum of elements in this range is less than or equal to `(r - l + 1)^2`, or recursively maximizing the sum for the sublists `a[l:pos - 1]` and `a[pos + 1:r + 1]` if the sum is greater. The function also keeps track of the operations performed by appending a tuple of `(l, r)` to the list `ops`. The final state of the program is that the list `a` has been modified to maximize the sum of its elements in the range from `l` to `r`, and the list `ops` contains a record of the operations performed.

#State of the program right berfore the function call: stdin contains two inputs: first an integer and then a space-separated list of integers. The integer is a positive integer and represents the length of the list. The list contains non-negative integers.
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s (the sum of the elements in list a), m (the maximum element in list a)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: n is a positive integer, a is a list of non-negative integers, s is the sum of the elements in a, m is the maximum element in a, ops is a list of pairs of elements, stdin is empty, l is the first element of the last pair in ops, r is the second element of the last pair in ops, and the value of l + 1 and r + 1 are being printed

#Overall this is what the function does:This function reads input from stdin, expecting a positive integer followed by a space-separated list of non-negative integers. It calculates the sum and maximum element of the list, and performs some operation (not specified in the provided code snippet) that results in a list of pairs of elements. The function then prints the sum, maximum element, and the pairs of elements (with indices incremented by 1).

