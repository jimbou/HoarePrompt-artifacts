#State of the program right berfore the function call: func is a function
    d = {}
    return wrapper
    #The program returns a function named wrapper

#Overall this is what the function does:The function returns a function named wrapper.

#State of the program right berfore the function call: args is a tuple of values of any type and d is a dictionary that maps tuples of values to their corresponding results.
    if (args not in d) :
        d[args] = func(*args)
    #State: *args is a tuple of values of any type and d is a dictionary that maps tuples of values to their corresponding results. If args is not in d, then d is updated with a new key-value pair where the key is the current value of args and the value is the result of calling the function func with the arguments *args. Otherwise, the dictionary d remains unchanged.
    return d[args]
    #The program returns the result of calling the function func with the arguments *args, or the corresponding result from the dictionary d if args is already a key in d.

#Overall this is what the function does:Memoizes the result of calling a function `func` with arguments `*args` and returns the result. If the arguments are already in the dictionary `d`, it returns the cached result; otherwise, it calls the function, stores the result in the dictionary, and returns it.

#State of the program right berfore the function call: No precondition can be extracted from this function as it does not take any parameters. It reads a line from standard input and returns it as a string.
    return sys.stdin.readline().strip()
    #The program returns a string that is read from the standard input, with leading and trailing whitespace removed.

#Overall this is what the function does:Reads a line from standard input and returns it as a string with leading and trailing whitespace removed.

#State of the program right berfore the function call: func_2() returns a string that represents an integer
    return int(func_2())
    #The program returns an integer that is represented by the string returned by func_2()

#Overall this is what the function does:Converts a string representation of an integer returned by func_2() to an integer and returns it.

#State of the program right berfore the function call: delimiter is a string, func_2() returns a string containing a space-separated list of integers.
    return list(map(int, func_2().split(delimiter)))
    #The program returns a list of integers, where each integer is a part of the string returned by func_2() and separated by the string delimiter.

#Overall this is what the function does:This function takes a delimiter string as input and returns a list of integers. It achieves this by calling another function, func_2(), which returns a string containing space-separated integers. The function then splits this string into substrings based on the provided delimiter, converts each substring to an integer, and returns the resulting list of integers.

#State of the program right berfore the function call: No precondition can be determined as the function does not have any parameters.
    return func_2()
    #The program returns the value returned by the function `func_2()`, but the specific value or type of this return value cannot be determined without more information about the function `func_2()`.

#Overall this is what the function does:This function calls another function named `func_2()` and returns its result, without modifying or using any external state or parameters. The specific outcome depends on the behavior of `func_2()`.

#State of the program right berfore the function call: n, m, and k are positive integers, A is a list of n distinct non-negative integers in ascending order, D is a sorted list of m distinct non-negative integers, and F is a list of k non-negative integers.
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
        
    #State: n, m, and k are positive integers, A is a list of n distinct non-negative integers in ascending order, D is a sorted list of m distinct non-negative integers, F is a list of k non-negative integers, max_diff is the maximum difference between two consecutive elements in A, next_max_diff is the next maximum difference between two consecutive elements in A excluding the maximum difference, and index is the index of the maximum difference in A.
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
        
    #State: ans is the minimum of its previous value and the maximum of D[l] + f - left and right - D[l] - f, f is the last element in the list F, l is the insertion point for left - f in D to maintain sorted order, h is the insertion point for right - f in D to maintain sorted order minus 1, mid is l + (h - l) // 2, mid_sum is D[l + (h - l) // 2] + f, mid_next_sum is D[l + (h - l) // 2 + 1] + f.
    print(max(ans, next_max_diff))
    #This is printed: max(ans, next_max_diff) (where ans is the minimum of its previous value and the maximum of D[l] + f - left and right - D[l] - f, and next_max_diff is another difference value)

#Overall this is what the function does:This function calculates the minimum maximum difference between two consecutive elements in a sorted list A, considering a list of non-negative integers F and a sorted list of distinct non-negative integers D. It first finds the maximum difference between two consecutive elements in A and the next maximum difference, excluding the maximum difference. Then, for each element in F, it finds the insertion point in D to maintain sorted order and updates the minimum maximum difference. Finally, it returns the maximum of the minimum maximum difference and the next maximum difference.

#State of the program right berfore the function call: testcases is a positive integer
    testcases = func_3()
    for _ in range(testcases):
        func_6()
        
    #State: `testcases` is the return value of `func_3()` that must be greater than or equal to 0, and `func_6()` has been executed `testcases` times.

#Overall this is what the function does:Executes `func_6()` a number of times equal to the return value of `func_3()`, which must be a non-negative integer.

