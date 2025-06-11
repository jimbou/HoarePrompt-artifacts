#State of the program right berfore the function call: func is a function
    d = {}
    return wrapper
    #The program returns a variable named wrapper, but the value of wrapper is not defined in the initial state.

#Overall this is what the function does:The function returns a variable named wrapper, but the value of wrapper is not defined in the initial state.

#State of the program right berfore the function call: args is a tuple of values of any type and value, d is a dictionary where keys are tuples of values of any type and value and values are results of the function func for the corresponding keys, func is a function that takes a tuple of values of any type and value as input and returns a result.
    if (args not in d) :
        d[args] = func(*args)
    #State: *`d` is a dictionary where keys are tuples of values of any type and value and values are results of the function `func` for the corresponding keys. If `args` is not in `d`, then `args` is added to `d` as a key with the result of `func(*args)` as its value. Otherwise, `d` remains unchanged.
    return d[args]
    #The program returns the result of the function `func` for the corresponding key `args`, which is stored in the dictionary `d`. If `args` is not in `d`, then the result of `func(*args)` is returned, otherwise the existing value associated with `args` in `d` is returned.

#Overall this is what the function does:This function memoizes the result of another function `func` by storing its results in a dictionary `d` for given input arguments `args`. It returns the result of `func` for the given `args`, either by retrieving it from the dictionary if it already exists, or by computing it, storing it in the dictionary, and then returning it. The function modifies the dictionary `d` by adding a new key-value pair if the input `args` is not already present.

#State of the program right berfore the function call: No precondition can be extracted from this function as it only reads a line from the standard input and does not use any variables in its signature.
    return sys.stdin.readline().strip()
    #The program returns a string that is the first line of input from the standard input, with any leading or trailing whitespace removed.

#Overall this is what the function does:Reads the first line of input from the standard input, removes any leading or trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: func_2() returns a string that can be converted to an integer
    return int(func_2())
    #The program returns an integer that is the result of converting the string returned by func_2() to an integer.

#Overall this is what the function does:Converts the string returned by func_2() to an integer and returns the result.

#State of the program right berfore the function call: delimiter is a string, func_2() returns a string containing space-separated integers.
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers. These integers are obtained by splitting the string returned by func_2() into substrings separated by the delimiter string, and then converting each substring to an integer.

#Overall this is what the function does:This function takes a delimiter string as input and returns a list of integers. It achieves this by splitting a string of space-separated integers (obtained from another function, func_2()) into substrings based on the provided delimiter, and then converting each substring into an integer. The resulting list of integers is then returned.

#State of the program right berfore the function call: No precondition can be determined from this function signature as it does not take any parameters.
    return func_2()
    #The program returns the value returned by the function `func_2()`

#Overall this is what the function does:This function calls and returns the result of another function named `func_2()`, effectively acting as a proxy or wrapper for `func_2()`. It does not perform any additional actions or modifications on the input variables, as there are no input parameters. The function's sole purpose is to delegate its execution to `func_2()` and return its result.

#State of the program right berfore the function call: n, m, and k are positive integers, A is a list of n distinct non-negative integers in ascending order, D is a sorted list of m distinct non-negative integers, F is a list of k non-negative integers, and inf is a negative infinity value.
    n, m, k = func_4()
    A = func_4()
    D = sorted(set(func_4()))
    F = func_4()
    max_diff, next_max_diff, index = -inf, -inf, None
    for i in range(1, n):
        diff = A[i] - A[i - 1]
        
        if diff > max_diff:
            max_diff = diff
            index = i
        elif diff > next_max_diff:
            next_max_diff = diff
        
    #State: n is a positive integer, m is a positive integer, k is a positive integer, A is a list of n distinct non-negative integers in ascending order, D is a sorted list of distinct non-negative integers, F is a list of k non-negative integers, max_diff is the maximum difference between consecutive elements in A, next_max_diff is the second maximum difference between consecutive elements in A, and index is the index of the maximum difference in A.
    left, right = A[index - 1], A[index]
    ans = max_diff
    for f in F:
        l = bisect_right(D, left - f)
        
        h = bisect_left(D, right - f) - 1
        
        while l < h:
            mid = l + (h - l) // 2
            mid_sum, mid_next_sum = D[mid] + f, D[mid + 1] + f
            if mid_sum - left < right - mid_next_sum:
                l = mid + 1
            else:
                h = mid
        
        if l == h:
            ans = min(ans, max(D[l] + f - left, right - D[l] - f))
        
    #State: ans is the minimum of its initial value and the maximum of D[l] + f - left and right - D[l] - f, l is the insertion point of left - f in D to maintain sorted order, h is the insertion point of right - f in D to maintain sorted order minus 1, mid is the average of l and h, mid_sum is D[mid] + f, mid_next_sum is D[mid + 1] + f, f is the last value in F, index is the index of the maximum difference in A, left is the element before the maximum difference in A, right is the element after the maximum difference in A, max_diff is the maximum difference between consecutive elements in A, next_max_diff is the second maximum difference between consecutive elements in A, A is a list of n distinct non-negative integers in ascending order, D is a sorted list of distinct non-negative integers, F is an empty list of non-negative integers, k is a positive integer, m is a positive integer, n is a positive integer.
    print(max(ans, next_max_diff))
    #This is printed: the maximum of the minimum of ans and the maximum of D[l] + f - left and right - D[l] - f, and the second maximum difference between consecutive elements in A

#Overall this is what the function does:This function calculates the minimum of the maximum difference between consecutive elements in a sorted list A and the maximum difference between elements in A and a sorted list D, considering a list of non-negative integers F. It returns the maximum of this minimum value and the second maximum difference between consecutive elements in A.

#State of the program right berfore the function call: testcases is a non-negative integer
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` is at least 3, and the function `func_6()` has been executed `testcases` times.

#Overall this is what the function does:Executes the function `func_6()` a certain number of times, where the number of executions is determined by the return value of `func_3()`, which is expected to be a non-negative integer.

