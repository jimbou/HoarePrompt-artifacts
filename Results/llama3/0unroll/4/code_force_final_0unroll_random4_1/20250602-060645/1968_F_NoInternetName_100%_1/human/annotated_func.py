#State of the program right berfore the function call: cast is a function that takes a string and returns a value of a specific type, and input() is a function that returns a string of space-separated values.
    return map(cast, input().split())
    #The program returns a map object that applies the cast function to each string in the list of space-separated values returned by input().split(), resulting in a sequence of values of a specific type.

#Overall this is what the function does:The function takes a string of space-separated values as input, applies a specified casting function to each value, and returns a sequence of values of the specified type.

#State of the program right berfore the function call: arr is a list of values of any type and predicate is a function that takes one argument and returns a boolean value.
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: l and r are equal and point to the first element in arr for which predicate returns True, or l is equal to r and points to the first element in arr for which predicate returns False.
    if predicate(arr[l]) :
        return l
        #The program returns the index of the first element in arr for which predicate returns True.
    #State: *l and r are equal and point to the first element in arr for which predicate returns True, or l is equal to r and points to the first element in arr for which predicate returns False. Additionally, predicate(arr[l]) is False
    return None
    #The program returns None.

#Overall this is what the function does:Searches for the first element in a list that satisfies a given predicate and returns its index if found, otherwise returns None.

#State of the program right berfore the function call: arr is a list of values and predicate is a function that takes a value and returns a boolean value.
    return func_2(arr, predicate)
    #The program returns the result of applying the function `func_2` to the list `arr` and the function `predicate`. The function `predicate` is applied to each value in the list `arr` and returns a boolean value. The result of `func_2` is determined by the values in `arr` and the boolean values returned by `predicate`.

#Overall this is what the function does:Applies a given predicate function to each value in a list and returns the result of a secondary function (`func_2`) based on the list values and the boolean results of the predicate function.

#State of the program right berfore the function call: arr is a list of elements of any type and predicate is a function that takes one argument and returns a boolean value.
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the output of `func_2(arr, predicate)` plus 1, where `func_2(arr, predicate)` is a function that takes a list `arr` and a function `predicate` as arguments and returns a value that is not None.
    #State: *`arr` is a list of elements of any type, `predicate` is a function that takes one argument and returns a boolean value, `result` is the output of `func_2(arr, predicate)`, and `result` is `None`
    return None
    #The program returns None.

#Overall this is what the function does:This function takes a list and a predicate function as input, applies the predicate function to the list using the `func_2` function, and returns the result of `func_2` plus 1 if it is not None. If the result of `func_2` is None, the function returns None.

#State of the program right berfore the function call: n and q are positive integers, a is a list of non-negative integers less than 2^30, and func_1 and func_4 are functions that return a list of integers and an integer respectively.
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: Output State: The list x contains a sequence of integers where each element is the XOR of the previous element and the corresponding element in list a. The dictionary inds contains the indices of the elements in list x, where each key is an element in x and its corresponding value is a list of indices where that element appears in x. The length of list x is equal to the length of list a plus one, and the length of the list of indices for each key in inds is equal to the number of times that key appears in x.
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
        
    #State: Output State: The loop has executed q iterations, and for each iteration, it has printed either 'Yes' or 'No' based on the conditions specified in the loop body. The state of the variables x, inds, and a remains unchanged, as they are not modified within the loop. The output state is the same as the initial state, with the addition of the printed results of the loop iterations.

#Overall this is what the function does:This function takes no parameters and returns no value. It performs the following actions: 

1. It calls the function func_1 twice to get two positive integers n and q, and a list of non-negative integers a. 
2. It generates a list x of XOR values of consecutive elements in list a, and a dictionary inds where each key is an element in x and its corresponding value is a list of indices where that element appears in x. 
3. It then iterates q times, each time taking two integers l and r as input from the function func_1. 
4. For each iteration, it checks if the XOR value at index l-1 is equal to the XOR value at index r. If they are equal, it prints 'Yes'. 
5. If the XOR values are not equal, it finds the smallest index greater than or equal to l where the XOR value is equal to the XOR value at index r, and the largest index less than or equal to r where the XOR value is equal to the XOR value at index l-1. 
6. If the largest index is greater than the smallest index, it prints 'Yes', otherwise it prints 'No'. 

The final state of the program is the same as the initial state, with the addition of the printed results of the loop iterations.

