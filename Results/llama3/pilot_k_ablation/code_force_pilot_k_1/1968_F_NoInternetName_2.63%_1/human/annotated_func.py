#State of the program right berfore the function call: cast is a function that takes a string and returns a value of a specific type, and input() is a function that returns a string containing a sequence of values separated by spaces.
    return map(cast, input().split())
    #The program returns a map object that applies the cast function to each string in the input sequence, where the input sequence is a string containing a sequence of values separated by spaces, and the cast function takes a string and returns a value of a specific type.

#Overall this is what the function does:The function takes a string of space-separated values as input, applies a specified casting function to each value, and returns a map object containing the casted values.

#State of the program right berfore the function call: arr is a list of elements of any type and predicate is a function that takes one argument and returns a boolean value.
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: `l` and `r` are equal, and `l` is the index of the first element in `arr` for which the `predicate` function returns True, or `l` is equal to the length of `arr` if no such element exists.
    if predicate(arr[l]) :
        return l
        #The program returns the index of the first element in `arr` for which the `predicate` function returns True, or the length of `arr` if no such element exists, which is equal to `r`.
    #State: *`l` and `r` are equal, and `l` is the index of the first element in `arr` for which the `predicate` function returns True, or `l` is equal to the length of `arr` if no such element exists. The `predicate` function returns False for the element at index `l` in `arr`.
    return None
    #The program returns None

#Overall this is what the function does:Searches for the first element in a list that satisfies a given predicate function and returns its index, or the length of the list if no such element exists. If the predicate function returns False for the first matching element, returns None.

#State of the program right berfore the function call: n and q are positive integers, a is a list of non-negative integers less than 2^30, l and r are positive integers such that 1 <= l < r <= n.
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: n is a positive integer, q is a positive integer, a is a list of non-negative integers less than 2^30, x is a list of integers where each element is the result of the XOR operation between the previous element and the corresponding element in a, inds is a dictionary where each key is an element in x and its corresponding value is a list of indices where that element appears in x.
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
        
    #State: n is a positive integer, q is 0, i is q, a is a list of non-negative integers less than 2^30, x is a list of integers where each element is the result of the XOR operation between the previous element and the corresponding element in a, inds is a dictionary where each key is an element in x and its corresponding value is a list of indices where that element appears in x.

#Overall this is what the function does:This function determines whether there exists a subarray within a given range [l, r] in the list 'a' such that the XOR of all elements in the subarray is equal to 0. It takes as input a list 'a' of non-negative integers less than 2^30 and a number of queries 'q', each query specifying a range [l, r]. The function iterates over each query, checking if the XOR of the elements in the specified range is 0. If it is, the function prints 'Yes'. Otherwise, it checks if there exists a subarray within the range that has an XOR of 0 by searching for a pair of indices in the 'inds' dictionary that satisfy the condition. If such a pair is found, the function prints 'Yes'; otherwise, it prints 'No'. The function repeats this process for all queries, ultimately returning no value but modifying the input variables 'n' and 'q' to 0.

