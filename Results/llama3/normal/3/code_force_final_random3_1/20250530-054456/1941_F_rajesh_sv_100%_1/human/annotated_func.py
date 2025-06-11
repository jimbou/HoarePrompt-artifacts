#State of the program right berfore the function call: func is a function
    d = {}
    return wrapper
    #The program returns the wrapper function.

#Overall this is what the function does:The function returns a wrapper function, which is the only action it performs.

#State of the program right berfore the function call: args is a variable number of arguments of any type and value, d is a dictionary that stores the results of previous function calls with the same arguments, and func is a function that takes a variable number of arguments and returns a value.
    if (args not in d) :
        d[args] = func(*args)
    #State: *args is a variable number of arguments of any type and value, d is a dictionary that stores the results of previous function calls with the same arguments, and func is a function that takes a variable number of arguments and returns a value. If args is not in d, then d now contains the current value of args as a key, and its corresponding value is the result of calling func with the current value of args. Otherwise, the state of d and args remains unchanged.
    return d[args]
    #The program returns the result of a previous function call with the same arguments, which is stored in dictionary d with the current value of args as the key. If args is not in d, it returns the result of calling func with the current value of args, which is now stored in d.

#Overall this is what the function does:This function caches and returns the result of a function call with given arguments. If the arguments have been used before, it returns the cached result; otherwise, it calls the function with the given arguments, stores the result in the cache, and returns it. The cache is stored in a dictionary where the keys are the function arguments and the values are the corresponding results.

#State of the program right berfore the function call: No precondition can be extracted from the function signature as it does not contain any parameters. The function only reads a line from the standard input and returns it as a string.
    return sys.stdin.readline().strip()
    #The program returns a string that is read from the standard input, with leading and trailing whitespace removed.

#Overall this is what the function does:Reads a line from the standard input and returns it as a string with leading and trailing whitespace removed.

#State of the program right berfore the function call: func_2() returns a string that can be converted to an integer
    return int(func_2())
    #The program returns an integer that is converted from a string returned by func_2()

#Overall this is what the function does:Converts a string returned by func_2() to an integer and returns the result.

#State of the program right berfore the function call: delimiter is a string
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers that are the result of splitting the string returned by func_2() using the delimiter string, and then converting each split part to an integer.

#Overall this is what the function does:This function takes a delimiter string as input and returns a list of integers. It achieves this by splitting a string returned by another function (func_2) using the provided delimiter, and then converting each resulting part into an integer. The function effectively transforms a string into a list of integers based on a specified delimiter.

#State of the program right berfore the function call: No precondition can be determined from the given function signature as it does not contain any parameters.
    return func_2()
    #The program returns the value returned by the function `func_2()`. No specific value can be determined as the function `func_2()` is not defined in the given code snippet.

#Overall this is what the function does:This function calls and returns the result of another function named `func_2()`, without performing any additional actions or modifications to any input variables, as it does not accept any parameters. The final state of the program is determined solely by the outcome of `func_2()`.

#State of the program right berfore the function call: n, m, and k are positive integers, A is a list of n distinct non-negative integers in ascending order, D is a sorted list of distinct non-negative integers, and F is a list of non-negative integers.
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
        
    #State: n is a positive integer, m is a positive integer, k is a positive integer, A is a list of n distinct non-negative integers in ascending order, D is a sorted list of distinct non-negative integers, F is a list of non-negative integers, max_diff is the maximum difference between any two consecutive elements in A, next_max_diff is the second maximum difference between any two consecutive elements in A, index is the index of the maximum difference in A, and i is n-1.
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
        
    #State: l is equal to h, ans is the minimum of its previous value and the maximum of D[l] + f - left and right - D[l] - f, f is the last value in F, mid is the average of l and h, mid_sum is D[mid] + f, and mid_next_sum is D[mid + 1] + f.
    print(max(ans, next_max_diff))
    #This is printed: The maximum value between the minimum of the previous value of ans and the maximum of D[l] + f - left and right - D[l] - f, and next_max_diff

#Overall this is what the function does:This function calculates the maximum difference between consecutive elements in a sorted list A, and then iterates through a list F to find the minimum difference between the maximum difference and the difference between elements in a sorted list D and the elements in F. It returns the maximum value between the minimum difference found and the second maximum difference between consecutive elements in A.

#State of the program right berfore the function call: testcases is a positive integer
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` is at least 3, and the function `func_6()` has been executed three times.

#Overall this is what the function does:Executes the function `func_6()` a number of times equal to the value returned by `func_3()`, which is at least 3.

