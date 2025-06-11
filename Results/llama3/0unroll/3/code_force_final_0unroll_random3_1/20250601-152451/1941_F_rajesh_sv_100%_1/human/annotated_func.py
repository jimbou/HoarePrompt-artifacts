#State of the program right berfore the function call: func is a function
    d = {}
    return wrapper
    #The program returns the variable 'wrapper' which has not been defined or described in the initial state.

#Overall this is what the function does:The function returns a variable named 'wrapper' without modifying or utilizing any input parameters, and its purpose and behavior are undefined.

#State of the program right berfore the function call: args is a tuple of values of any type and d is a dictionary where keys are tuples of values of any type and values are the results of func applied to these tuples.
    if (args not in d) :
        d[args] = func(*args)
    #State: *`args` is a tuple of values of any type, `d` is a dictionary where keys are tuples of values of any type and values are the results of `func` applied to these tuples. If `args` is not in `d`, `d[args]` is the result of `func` applied to the current value of `*args`. Otherwise, no changes are made to `d`.
    return d[args]
    #The program returns the result of `func` applied to the current value of `*args`, which is stored in dictionary `d` with key `args`. If `args` is not in `d`, the result is computed and stored in `d[args]`.

#Overall this is what the function does:The function takes a tuple of values and a dictionary as input, checks if the tuple is a key in the dictionary, and if not, computes the result of applying a given function to the tuple and stores it in the dictionary. The function then returns the result associated with the tuple in the dictionary, either newly computed or previously stored.

#State of the program right berfore the function call: stdin contains a string
    return sys.stdin.readline().strip()
    #The program returns a string that was provided as input through stdin, with any leading or trailing whitespace removed.

#Overall this is what the function does:Reads a line of input from standard input, removes any leading or trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: func_2() returns a string that represents an integer.
    return int(func_2())
    #The program returns an integer that is represented by the string returned by func_2()

#Overall this is what the function does:Converts a string representation of an integer returned by func_2() to an integer and returns it.

#State of the program right berfore the function call: delimiter is a string, func_2() returns a string of space-separated integers.
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers, where the integers are obtained by splitting the string returned by func_2() into substrings separated by the delimiter string, and then converting each substring to an integer.

#Overall this is what the function does:The function takes a delimiter string as input and returns a list of integers. It achieves this by splitting a string of space-separated integers (obtained from another function, func_2()) into substrings based on the provided delimiter, and then converting each substring to an integer. The resulting list of integers is then returned.

#State of the program right berfore the function call: No precondition can be determined as the function does not have any parameters.
    return func_2()
    #The program returns the value returned by the function `func_2()`.

#Overall this is what the function does:This function calls and returns the result of another function named `func_2()`, effectively acting as a proxy or wrapper for `func_2()`. It does not modify or utilize any external state or parameters, solely relying on the outcome of `func_2()` to determine its return value.

#State of the program right berfore the function call: n, m, and k are positive integers, A is a list of n distinct non-decreasing integers, D is a sorted list of distinct non-negative integers, and F is a list of non-negative integers.
    n, m, k = func_4()
    A = func_4()
    D = sorted(set(func_4()))
    F = func_4()
    max_diff, next_max_diff, index = -inf, -inf, None
    for i in range(1, n):
        diff = A[i] - A[i - 1]
        
        if diff > max_diff:
            next_max_diff = max_diff
            max_diff = diff
            index = i
        elif diff > next_max_diff:
            next_max_diff = diff
        
    #State: Output State: n, m, and k are positive integers returned by func_4(), A is a list of n distinct non-decreasing integers returned by func_4(), D is a sorted list of distinct non-negative integers returned by func_4(), F is a list of non-negative integers returned by func_4(), max_diff is the maximum difference between any two consecutive elements in A, next_max_diff is the second maximum difference between any two consecutive elements in A, and index is the index of the maximum difference in A.
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
        
    #State: Output State: n, m, and k are positive integers returned by func_4(), A is a list of n distinct non-decreasing integers returned by func_4(), D is a sorted list of distinct non-negative integers returned by func_4(), F is a list of non-negative integers returned by func_4(), max_diff is the maximum difference between any two consecutive elements in A, next_max_diff is the second maximum difference between any two consecutive elements in A, index is the index of the maximum difference in A, left is the value of A at index - 1, right is the value of A at index, and ans is the minimum of the maximum difference between any two consecutive elements in A and the minimum of the maximum difference between any two consecutive elements in A and the maximum difference between any two consecutive elements in A after subtracting the value of f from the left and right elements for all f in F.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum of the maximum difference between any two consecutive elements in A and the minimum of the maximum difference between any two consecutive elements in A after subtracting the value of f from the left and right elements for all f in F, and next_max_diff is the second maximum difference between any two consecutive elements in A)

#Overall this is what the function does:This function calculates the maximum difference between any two consecutive elements in a list of distinct non-decreasing integers, and then updates this maximum difference by considering the minimum of the maximum difference between any two consecutive elements after subtracting a value from the left and right elements for all values in a list of non-negative integers. The function returns the maximum of the updated maximum difference and the second maximum difference between any two consecutive elements in the original list.

#State of the program right berfore the function call: No precondition can be extracted from this function as it does not take any parameters.
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: Output State: The function `func_6()` has been called `testcases` times.

#Overall this is what the function does:Executes the function `func_6()` a number of times equal to the value returned by `func_3()`, without taking any input parameters or returning any output.

