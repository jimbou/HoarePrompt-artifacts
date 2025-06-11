#State of the program right berfore the function call: a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l <= r < len(a), and ops is a list of tuples of non-negative integers.
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: *a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l <= r < len(a), and ops is a list of tuples of non-negative integers. If a[l] is not equal to 0, ops is updated with an additional tuple (l, l), and the current value of l is equal to the current value of r.
        return
        #The program returns nothing
    #State: a is a list of non-negative integers, l and r are non-negative integers such that 0 <= l < r < len(a), and ops is a list of tuples of non-negative integers.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: The value of `a[l]` is now equal to `r - l + 1`, and all elements in the list `a` from index `l` to `r` (inclusive) have been updated to `r - l + 1`. The values of `l`, `r`, and `ops` remain unchanged.
        func_1(a, l + 1, r, ops)
    #State: *`a` is a list of non-negative integers, `l` is a non-negative integer, `r` is a non-negative integer such that `l < r < len(a)`, `ops` is a list of tuples of non-negative integers, and the function `func_1` has been called with arguments `a`, `l + 1`, `r`, and `ops`. If `a[l]` is not equal to `r - l + 1`, then the value of `a[l + 1]` is now equal to `r - (l + 1) + 1`, and all elements in the list `a` from index `l + 1` to `r` (inclusive) have been updated to `r - (l + 1) + 1`. The values of `l`, `r`, and `ops` remain unchanged.

#Overall this is what the function does:This function modifies a list of non-negative integers by iteratively updating elements within a specified range to match the length of that range. It also keeps track of the operations performed by appending tuples representing the modified ranges to a separate list. The function takes no return value, instead modifying the input list and operations list in-place.

#State of the program right berfore the function call: a is a list of non-negative integers
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns a tuple containing the sum of all non-negative integers in list 'a', the length of the empty list 'ops' which is 0, and the empty list 'ops' itself.

#Overall this is what the function does:This function calculates the sum of all non-negative integers in a given list 'a' and returns the sum along with the length and the contents of an empty list 'ops'. The function does not modify the input list 'a' and does not perform any operations that are stored in the 'ops' list. The purpose of the function is to provide the total sum of non-negative integers in the list 'a' and indicate that no operations were performed.

#State of the program right berfore the function call: l and r are non-negative integers such that 0 <= l <= r < len(a), a is a list of non-negative integers.
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: The subarray of a from index l to r (inclusive) has been modified to contain the value r - l + 1 at each index, while the values of l, r, s, and ops remain unchanged.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: *l and r are non-negative integers such that 0 <= l <= r < len(a), a is a list of non-negative integers. If the index of the maximum value in a from index l to r (inclusive) is not equal to l, then the sum of the elements in a from index l to pos - 1 (inclusive) is greater than (pos - 1 - l + 1) * (pos - 1 - l + 1), and the maximum value in a from index l to pos - 1 (inclusive) is the value at index pos in a, and a value has been returned. Otherwise, no changes have been made.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: The function either returns the result of the recursive call with arguments `pos + 1` and `r`, or does not make any changes, depending on whether the index of the maximum value in `a` from index `l` to `r` (inclusive) is equal to `r` or not. In both cases, the values of `l`, `r`, `a`, and `pos` remain unchanged, and the conditions regarding the sum and maximum value in `a` from index `l` to `pos - 1` (inclusive) are still satisfied.
    #State: `l` and `r` are non-negative integers such that 0 <= l <= r < len(a), `a` is a list of non-negative integers. If the sum of the elements in `a` from index `l` to `r` (inclusive) is less than or equal to the square of the length of the subarray, the subarray of `a` from index `l` to `r` (inclusive) is modified to contain the value `r - l + 1` at each index. Otherwise, the function either returns the result of the recursive call with arguments `pos + 1` and `r`, or does not make any changes, depending on whether the index of the maximum value in `a` from index `l` to `r` (inclusive) is equal to `r` or not. In both cases, the values of `l`, `r`, `a`, and `pos` remain unchanged, and the conditions regarding the sum and maximum value in `a` from index `l` to `pos - 1` (inclusive) are still satisfied.

#Overall this is what the function does:This function modifies a subarray of a given list `a` within a specified range `[l, r]` (inclusive) based on the sum of its elements. If the sum is less than or equal to the square of the subarray's length, it replaces all elements in the subarray with the length of the subarray. Otherwise, it recursively calls itself on the subarray split at the index of the maximum value within the range, potentially modifying the subarray if the maximum value is not at the start or end of the range. The function also keeps track of the operations performed by appending the modified range to the `ops` list.

#State of the program right berfore the function call: stdin contains two inputs: first an integer n and then a space-separated list of n integers. The integer n is a positive integer and less or equal than 18. The integers in the list are non-negative and less or equal than 10^7.
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s (where s is an integer), m (where m is an integer)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: Output State: The value of s and the value of m are printed, and the values of l and r are updated to the last pair of values in ops.

#Overall this is what the function does:The function reads two inputs from stdin: a positive integer n (n <= 18) and a space-separated list of n non-negative integers (each <= 10^7). It then processes this list, producing an integer s, an integer m, and a list of pairs (l, r). The function prints the values of s and m, followed by the values of l and r for each pair in the list.

