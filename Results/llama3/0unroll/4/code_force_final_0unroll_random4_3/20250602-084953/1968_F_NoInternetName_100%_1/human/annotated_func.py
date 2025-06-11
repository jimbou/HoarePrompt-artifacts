#State of the program right berfore the function call: cast is a function that takes a string and returns a value of a specific type, and input() is a function that returns a string of space-separated values.
    return map(cast, input().split())
    #The program returns a map object that applies the cast function to each string in the list of space-separated values returned by the input() function. The cast function converts each string to a specific type, and the resulting values are returned as a map object.

#Overall this is what the function does:The function takes a string of space-separated values as input, applies a specified cast function to each value, and returns a map object containing the converted values.

#State of the program right berfore the function call: arr is a list of elements of any type and predicate is a function that takes one argument and returns a boolean value.
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: l is the index of the first element in arr for which predicate returns True, or the length of arr if no such element exists.
    if predicate(arr[l]) :
        return l
        #The program returns the index of the first element in the array 'arr' for which the predicate function returns True, or the length of 'arr' if no such element exists.
    #State: l is the index of the first element in arr for which predicate returns True, or the length of arr if no such element exists. Additionally, predicate(arr[l]) returns False.
    return None
    #The program returns None

#Overall this is what the function does:This function performs a binary search on a list 'arr' using a given predicate function. It returns the index of the first element in 'arr' for which the predicate function returns True, or the length of 'arr' if no such element exists. If the predicate function returns False for the found index, the function returns None.

#State of the program right berfore the function call: arr is a list of elements of any type and predicate is a function that takes one argument and returns a boolean value.
    return func_2(arr, predicate)
    #The program returns the result of the function `func_2` applied to the list `arr` and the function `predicate`. The function `func_2` is not defined in the given code, but based on the initial state, it is expected to take a list and a predicate function as arguments and return a value. The predicate function takes one argument and returns a boolean value. The list `arr` contains elements of any type.

#Overall this is what the function does:Applies a predicate function to a list of elements and returns the result of a secondary function (`func_2`) that takes the list and the predicate function as arguments.

#State of the program right berfore the function call: arr is a list of elements of any type and predicate is a function that takes one argument and returns a boolean value.
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` (which is the return value of `func_2(arr, predicate)`) plus 1, where `result` is not None, `arr` is a list of elements of any type, and `predicate` is a function that takes one argument and returns a boolean value.
    #State: *`arr` is a list of elements of any type, `predicate` is a function that takes one argument and returns a boolean value, `result` is the return value of `func_2(arr, predicate)`, and `result` is `None`
    return None
    #The program returns None.

#Overall this is what the function does:This function takes a list of elements and a predicate function as input, calls another function (`func_2`) with these inputs, and returns the result of that function call plus 1 if the result is not None. If the result is None, the function returns None.

#State of the program right berfore the function call: n and q are positive integers, a is a list of non-negative integers less than 2^30, l and r are positive integers such that 1 <= l < r <= n.
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: Output State: n and q are positive integers, a is a list of non-negative integers less than 2^30, x is a list of integers where each element is the XOR of the previous element and the corresponding element in a, inds is a dictionary where each key is an element in x and its corresponding value is a list of indices where that element appears in x.
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
        
    #State: Output State: The output state after the loop executes all the iterations is the same as the initial state, with no changes to the values of n, q, a, x, and inds. The loop only prints 'Yes' or 'No' based on the conditions inside the loop, but it does not modify any of the variables in the initial state.

#Overall this is what the function does:This function determines whether there exists a subarray within a given array 'a' of non-negative integers, such that the XOR of all elements in the subarray equals zero. It takes as input the length of the array 'n', the number of queries 'q', the array 'a', and 'q' pairs of indices 'l' and 'r' representing the subarray ranges to be queried. The function prints 'Yes' if a subarray with XOR equal to zero exists within the specified range, and 'No' otherwise. The function does not modify the input array or any other variables, and its output is solely based on the printed results of the queries.

