#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object containing integers from the input list.

#Overall this is what the function does:The function reads a space-separated list of integers from standard input, converts each integer to an integer type, and returns a map object containing these integers.

#State of the program right berfore the function call: func_1 is a function that returns an iterator of values
    return list(func_1())
    #The program returns a list of values returned by the iterator func_1.

#Overall this is what the function does:The function takes no parameters and returns a list of values produced by the iterator func_1.

#State of the program right berfore the function call: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of n distinct integers from 1 to n in arbitrary order, and k is an element in arr.
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is a positive integer greater than 0, `k` is a positive integer such that 1 <= k <= n, `arr` is a list of n distinct integers from 1 to n in arbitrary order, and `k` is an element in `arr`. `pos` is the index of `k` in `arr`, and `i` is equal to `n`.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: low is equal to high, mid is equal to low, st is a set containing all the mid values from previous iterations.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: high + 1, pos + 1 (where high is the value of high and pos is the position of the desired value k in the array)
    #State: *low is equal to high, mid is equal to low, st is a set containing all the mid values from previous iterations. If the current value of arr[low] is equal to k, then 0 is printed. Otherwise, the value at index low in the array arr is not equal to k, and 1 is printed, and the value of low + 1 and pos + 1 are printed.

#Overall this is what the function does:Searches for a target value k in a list of distinct integers arr and prints the result. If k is found at the index low, prints 0. If k is not found at index low, prints 1 and the indices low + 1 and pos + 1, where pos is the actual position of k in the array.

