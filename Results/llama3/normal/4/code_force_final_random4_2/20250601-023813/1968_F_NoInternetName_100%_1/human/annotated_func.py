#State of the program right berfore the function call: cast is a function that takes a string and returns a value of a specific type, and input() is a function that returns a string of space-separated values.
    return map(cast, input().split())
    #The program returns a map object that applies the cast function to each string in the list of space-separated values returned by the input() function, converting each string to a specific type.

#Overall this is what the function does:The function takes a string of space-separated values as input, splits it into individual strings, applies a specified casting function to each string, and returns a map object containing the converted values.

#State of the program right berfore the function call: arr is a list of elements of any type and predicate is a function that takes one argument and returns a boolean value.
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: `arr` is a list of elements of any type, `predicate` is a function that takes one argument and returns a boolean value, `l` and `r` are integers, `l` equals `r`.
    if predicate(arr[l]) :
        return l
        #The program returns an integer `l` that is equal to `r`, and the value of `predicate(arr[l])` is True.
    #State: *`arr` is a list of elements of any type, `predicate` is a function that takes one argument and returns a boolean value, `l` and `r` are integers, `l` equals `r`. The result of applying the `predicate` function to the element of `arr` at index `l` is false.
    return None
    #The program returns None

#Overall this is what the function does:This function performs a binary search on a list of elements using a given predicate function. It returns the index of the first element in the list for which the predicate function returns True, or None if no such element is found.

#State of the program right berfore the function call: arr is a list of values of any type and predicate is a function that takes a value and returns a boolean
    return func_2(arr, predicate)
    #The program returns the result of the function func_2, which takes a list of values of any type (arr) and a function that returns a boolean (predicate) as arguments. The exact output depends on the implementation of func_2, but it will be based on the values in arr and the boolean results returned by predicate.

#Overall this is what the function does:This function takes a list of values and a predicate function as input, applies the predicate function to the list using the func_2 function, and returns the result. The exact output depends on the implementation of func_2, but it is based on the values in the input list and the boolean results returned by the predicate function.

#State of the program right berfore the function call: arr is a list of elements of any type and predicate is a function that takes one argument and returns a boolean value.
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the output of `func_2` with arguments `arr` and `predicate` plus one, where `arr` is a list of elements of any type and `predicate` is a function that takes one argument and returns a boolean value.
    #State: *`arr` is a list of elements of any type, `predicate` is a function that takes one argument and returns a boolean value, `result` is the output of `func_2` with arguments `arr` and `predicate`, and `result` is `None`
    return None
    #The program returns None

#Overall this is what the function does:This function takes a list of elements and a predicate function as input, applies the predicate function to the list using `func_2`, and returns the result plus one if it is not None. If the result is None, the function returns None.

#State of the program right berfore the function call: n and q are positive integers, a is a list of non-negative integers less than 2^30, and the function func_1 returns a list of integers when given an integer, and the function func_3 and func_4 return indices of a list given a list and a function.
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: n is an integer, q is an integer, a is a list of integers, x is a list containing len(a) + 1 elements, inds is a dictionary with a single key 0 and a list containing len(a) + 1 elements.
    for i in range(q):
        l, r = func_1(int)
        
        if x[l - 1] == x[r]:
            print('Yes')
            continue
        
        lower = inds[x[r]][func_4(inds[x[r]], lambda arg: arg < l) or 0]
        
        upper = inds[x[l - 1]][func_3(inds[x[l - 1]], lambda arg: arg <= r)]
        
        if upper > lower:
            print('Yes')
        else:
            print('No')
        
    #State: n is an integer, q is an integer, a is a list of integers, x is a list containing len(a) + 1 elements, inds is a dictionary with a single key 0 and a list containing len(a) + 1 elements, i is q - 1, l and r are returned by func_1(n), lower is the value at index func_4(inds[x[r]], lambda arg: arg < l) or 0 in the list inds[x[r]], upper is the value at index func_3(inds[x[l - 1]], lambda arg: arg <= r) in the list inds[x[l - 1]]. If upper is greater than lower, 'Yes' is printed. Otherwise, 'No' is printed.

#Overall this is what the function does:This function takes no parameters and returns no value. It generates a list of integers 'a' and two positive integers 'n' and 'q' using the function func_1. It then creates a list 'x' containing cumulative XOR values of the elements in 'a' and a dictionary 'inds' to store indices of 'x'. The function then iterates 'q' times, each time taking two integers 'l' and 'r' using func_1. It checks if the XOR value at index 'l-1' is equal to the XOR value at index 'r'. If they are equal, it prints 'Yes'. Otherwise, it finds the lower and upper bounds of the range [l, r] in the list 'inds' using functions func_3 and func_4, and prints 'Yes' if the upper bound is greater than the lower bound, and 'No' otherwise.

