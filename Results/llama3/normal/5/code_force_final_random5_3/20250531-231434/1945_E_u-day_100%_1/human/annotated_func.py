#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a result of converting a space-separated string from the standard input into an integer.

#Overall this is what the function does:The function reads a space-separated list of integers from the standard input, converts each string into an integer, and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: func_1 is a function that returns an iterator of values.
    return list(func_1())
    #The program returns a list of values returned by the iterator func_1

#Overall this is what the function does:The function takes no parameters and returns a list of values produced by the iterator func_1. The function does not modify any input variables and only consumes the iterator func_1 to produce the output list.

#State of the program right berfore the function call: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of distinct integers from 1 to n in arbitrary order, func_1() returns a tuple of two positive integers, and func_2() returns a list of distinct integers from 1 to n in arbitrary order.
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of distinct integers from 1 to n in arbitrary order, i is n-1. If the current value of arr[i] is equal to k, then pos is n-1. Otherwise, the state of pos remains unchanged.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: low equals high, st is a set containing all integers from 0 to n-1, and pos is either n-1 or its original value depending on whether arr[i] equals k.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: high + 1, pos + 1 (where high is the value of high and pos is the original value of pos)
    #State: *low equals high, st is a set containing all integers from 0 to n-1, and pos is either n-1 or its original value depending on whether arr[i] equals k. If the current value of arr[low] is equal to k, then 0 is printed. Otherwise, 1 is printed, low + 1 (where low equals high) and pos + 1 (where pos is either n-1 or its original value depending on whether arr[i] equals k) are printed.

#Overall this is what the function does:This function determines the position of a target value k in a list of distinct integers arr. It first attempts to find the position of k in arr through a linear search. If k is found, the function prints 0. If k is not found, the function performs a binary search on arr to find the position where k should be inserted to maintain the list's sorted order. The function then prints 1, followed by the position where k should be inserted (low + 1) and the position of k if it were present in the list (pos + 1).

