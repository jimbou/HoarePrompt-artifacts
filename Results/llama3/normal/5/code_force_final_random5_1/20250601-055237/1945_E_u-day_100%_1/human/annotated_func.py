#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a list of integers, where each integer is a value from the input list provided through stdin, and each integer is separated by a space.

#Overall this is what the function does:The function reads a space-separated list of integers from standard input, converts each integer to an integer type, and returns a map object containing the list of integers.

#State of the program right berfore the function call: func_1 is a function that returns an iterator of values of any type and value
    return list(func_1())
    #The program returns a list of values of any type returned by the iterator func_1.

#Overall this is what the function does:This function takes an iterator function `func_1` as input, iterates over its values, and returns them as a list. The returned list contains values of any type yielded by the iterator `func_1`.

#State of the program right berfore the function call: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of distinct integers from 1 to n in arbitrary order, and pos is the index of k in arr.
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of distinct integers from 1 to n in arbitrary order, i is n-1. If the current value of arr[i] is equal to k, then pos is n-1. Otherwise, pos remains -1.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: low is equal to high, st is a set containing all the values that were once mid, i is n-1, pos is either n-1 or -1 depending on whether the current value of arr[i] is equal to k.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: high + 1, 0 (where high is the high index of the search range and 0 is the value of pos + 1)
    #State: low is equal to high, st is a set containing all the values that were once mid, i is n-1, and pos is either n-1 or -1 depending on whether the current value of arr[i] is equal to k. If the current value of arr[low] is equal to k, then 0 is printed. Otherwise, 1 is printed, and low + 1 and pos + 1 are printed, where low is equal to high and pos is either n-1 or -1 depending on whether the current value of arr[i] is equal to k.

#Overall this is what the function does:Searches for a target value k in a list of distinct integers arr and returns the index of k if found, or the index where k should be inserted to maintain sorted order if not found. If k is found, prints 0. If k is not found, prints 1 and the index where k should be inserted, along with the index of k in the original list if it exists.

