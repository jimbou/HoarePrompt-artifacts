#State of the program right berfore the function call: cast is a function that takes a string and returns a value of a specific type, and input() is a function that returns a string of space-separated values.
    return map(cast, input().split())
    #The program returns a map object that applies the cast function to each string in the list of space-separated values returned by the input() function, converting them to a specific type.

#Overall this is what the function does:The function takes a string of space-separated values as input, splits it into individual strings, applies a specified cast function to each string to convert it to a specific type, and returns a map object containing the converted values.

#State of the program right berfore the function call: arr is a list of values of any type and predicate is a function that takes one argument and returns a boolean value.
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: `arr` is a list of values of any type, `predicate` is a function that takes one argument and returns a boolean value, `l` is equal to `r`, `r` is the length of `arr`. If there exists an index `i` in `arr` such that `predicate(arr[i])` is True and for all indices `j` less than `i`, `predicate(arr[j])` is False, then `l` and `r` are equal to `i+1`. Otherwise, `l` and `r` are equal to the length of `arr`.
    if predicate(arr[l]) :
        return l
        #The program returns an index in the list `arr` such that `predicate(arr[l])` is True. This index is either equal to the length of `arr` or it is equal to `i+1` where `i` is an index in `arr` such that `predicate(arr[i])` is True and for all indices `j` less than `i`, `predicate(arr[j])` is False.
    #State: *`arr` is a list of values of any type, `predicate` is a function that takes one argument and returns a boolean value, `l` is equal to `r`, `r` is the length of `arr`. If there exists an index `i` in `arr` such that `predicate(arr[i])` is True and for all indices `j` less than `i`, `predicate(arr[j])` is False, then `l` and `r` are equal to `i+1`. Otherwise, `l` and `r` are equal to the length of `arr`. Additionally, `predicate(arr[l])` is False.
    return None
    #The program returns None

#Overall this is what the function does:Searches for the first index in a list where a given predicate is true, returning the index if found or None if not. If the predicate is never true, returns the length of the list.

#State of the program right berfore the function call: n and q are positive integers, a is a list of non-negative integers less than 2^30, l and r are positive integers such that 1 <= l < r <= n.
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: n is a positive integer, q is a positive integer, a is a list of non-negative integers less than 2^30, x is a list containing the cumulative bitwise XOR of all elements in a, inds is a dictionary where each key is an element in x and its corresponding value is a list of indices where that element appears in x, l and r are positive integers such that 1 <= l < r <= n.
    for i in range(q):
        l, r = func_1(int)
        
        if x[l - 1] == x[r]:
            print('Yes')
            continue
        
        lower = func_2(inds[x[r]], lambda arg: arg < l) or -1
        
        upper = func_2(inds[x[l - 1]], lambda arg: arg <= r)
        
        lower = inds[x[r]][lower + 1]
        
        upper = inds[x[l - 1]][upper]
        
        if upper > lower and l <= upper <= r and l <= lower <= r:
            print('Yes')
        else:
            print('No')
        
    #State: n is a positive integer, q is 0, a is a list of non-negative integers less than 2^30, x is a list containing the cumulative bitwise XOR of all elements in a, inds is a dictionary where each key is an element in x and its corresponding value is a list of indices where that element appears in x, l and r are positive integers such that 1 <= l < r <= n, i is q.

#Overall this is what the function does:This function determines whether there exists a subarray within a given range [l, r] in the input list 'a' such that the cumulative bitwise XOR of the subarray is equal to the cumulative bitwise XOR of the entire list 'a' from index 0 to 'r'. It iterates over a series of queries, each specifying a range [l, r], and prints 'Yes' if such a subarray exists and 'No' otherwise. The function takes no explicit parameters but relies on external functions 'func_1' and 'func_2' to obtain input values.

