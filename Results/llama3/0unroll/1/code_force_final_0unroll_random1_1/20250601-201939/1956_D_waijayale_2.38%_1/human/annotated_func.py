#State of the program right berfore the function call: a is a list of non-negative integers, l and r are integers such that 0 <= l <= r < len(a), and ops is a list of tuples of integers.
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: *a is a list of non-negative integers, l and r are integers such that 0 <= l <= r < len(a) and l is equal to r, ops is a list of tuples of integers. If a[l] is not equal to 0, ops is updated with an additional tuple (l, l).
        return
        #The program returns nothing.
    #State: a is a list of non-negative integers, l and r are integers such that 0 <= l < r < len(a), and ops is a list of tuples of integers.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: The value of `a` has been modified such that all elements from index `l` to `r` (inclusive) are now equal to `r - l + 1`. The values of `l`, `r`, and `ops` remain unchanged.
        func_1(a, l + 1, r, ops)
    #State: *`a` is a list of non-negative integers, `l` is an integer such that 0 <= l < len(a), `r` is an integer such that l < r < len(a), `ops` is a list of tuples of integers. If `a[l]` is not equal to `r - l + 1`, then all elements from index `l + 1` to `r` (inclusive) in `a` are now equal to `r - l`. Otherwise, the values of `a`, `l`, `r`, and `ops` remain unchanged.

#Overall this is what the function does:This function modifies a list of non-negative integers (`a`) by setting all elements within a specified range (`l` to `r`) to the length of that range (`r - l + 1`), but only if the first element of that range does not already match the range length. It also keeps track of the operations performed by appending tuples representing the modified ranges to a list (`ops`). The function recursively processes the list, starting from the first element of the specified range and moving forward. If the first element of the range is not equal to the range length, it updates the range in the list and records the operation. The function returns no value.

#State of the program right berfore the function call: a is a list of non-negative integers.
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all non-negative integers in list 'a', the length of the empty list 'ops' which is 0, and the empty list 'ops'.

#Overall this is what the function does:This function calculates the sum of all non-negative integers in a given list 'a' and returns the sum along with an empty list 'ops' and its length (which is 0). The function does not modify the input list 'a' and does not perform any operations that are stored in the 'ops' list. The purpose of the function is to provide the total sum of non-negative integers in the list 'a'.

#State of the program right berfore the function call: l and r are non-negative integers such that 0 <= l <= r < len(a), and a is a list of non-negative integers.
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: The list 'a' has been modified such that all elements from index 'l' to 'r' (inclusive) are now equal to 'r - l + 1'. The values of 'l', 'r', and 's' remain unchanged.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: *l and r are non-negative integers such that 0 <= l <= r < len(a), a is a list of non-negative integers, s is the sum of the elements in a from index l to r (inclusive), and s is greater than (r - l + 1) * (r - l + 1), mx is the maximum value in the sublist a[l:r + 1], pos is the index of mx in the original list a. If pos is not equal to l, the function recursive_maximize_sum has been called with arguments l and pos - 1. Otherwise, no further action has been taken.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: *`l` and `r` are non-negative integers such that 0 <= `l` <= `r` < len(`a`), `a` is a list of non-negative integers, `s` is the sum of the elements in `a` from index `l` to `r` (inclusive), and `s` is greater than (`r` - `l` + 1) * (`r` - `l` + 1), `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the index of `mx` in the original list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum` has been called with arguments `pos + 1` and `r`, and previously it has been called with arguments `l` and `pos - 1`. Otherwise, no further action has been taken.
    #State: *`l` and `r` are non-negative integers such that 0 <= `l` <= `r` < len(`a`), `a` is a list of non-negative integers, `s` is the sum of the elements in `a` from index `l` to `r` (inclusive). If `s` is less than or equal to (`r` - `l` + 1) * (`r` - `l` + 1), all elements in `a` from index `l` to `r` (inclusive) are now equal to `r - l + 1`, and the values of `l`, `r`, and `s` remain unchanged. If `s` is greater than (`r` - `l` + 1) * (`r` - `l` + 1), `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the index of `mx` in the original list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum` has been called with arguments `pos + 1` and `r`, and previously it has been called with arguments `l` and `pos - 1`. Otherwise, no further action has been taken.

#Overall this is what the function does:Modifies a list of non-negative integers by either replacing a sub-range with a uniform value or recursively maximizing the sum of sub-ranges.

#State of the program right berfore the function call: stdin contains two inputs: first an integer and then a space-separated list of integers. The integer is a positive integer and represents the length of the list. The list contains non-negative integers.
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s (which is an integer), m (which is an integer)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: Output State: The output state is the same as the initial state, with the values of l and r changed in each iteration of the loop. In each iteration, l and r are assigned the next pair of values from the ops list. The values of n, a, s, m, and stdin remain unchanged. The output of the loop is a series of pairs of numbers, where each pair consists of l + 1 and r + 1, printed to the console.

#Overall this is what the function does:This function reads input from the standard input, processes it, and prints the results to the console. It accepts two inputs: a positive integer 'n' representing the length of a list, and a space-separated list of non-negative integers 'a' of length 'n'. The function then calls another function 'func_2' with 'a' as an argument, which returns three values: 's', 'm', and 'ops'. The function prints 's' and 'm' to the console, followed by a series of pairs of numbers, where each pair consists of 'l + 1' and 'r + 1', derived from the 'ops' list. The function does not modify the input values or the standard input state.

