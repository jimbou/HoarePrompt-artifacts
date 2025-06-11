#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a value from the space-separated list of integers provided in the standard input (stdin).

#Overall this is what the function does:Reads a space-separated list of integers from standard input, converts each integer to an integer type, and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: func_1 is a function that returns an iterator.
    return list(func_1())
    #The program returns a list containing all the values yielded by the iterator returned by func_1()

#Overall this is what the function does:The function takes no parameters and returns a list containing all the values yielded by the iterator returned by func_1. It effectively converts the iterator into a list, providing a collection of all values produced by func_1.

#State of the program right berfore the function call: n and k are positive integers, arr is a list of distinct integers from 1 to n, and k is an element in arr.
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: Output State: The value of pos is the index of k in arr, and the values of n, arr, and k remain unchanged.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: low is the index of k in arr, high is low + 1, st is a set of indices of elements in arr that are greater than k, pos is the index of k in arr, n, arr, and k remain unchanged.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: high (which is low + 1), pos + 1 (which is the index of the element after k)
    #State: *low is the index of k in arr, high is low + 1, st is a set of indices of elements in arr that are greater than k, pos is the index of k in arr, n, arr, and k remain unchanged. If the current value of arr[low] is equal to k, 0 is printed. Otherwise, 1 is printed, and low + 1 and pos + 1 are printed, where low + 1 is equal to high and pos + 1 is equal to the index of k in arr + 1.

#Overall this is what the function does:Searches for the index of a given element `k` in a sorted list `arr` of distinct integers from 1 to `n`, and prints the result. If `k` is found, prints 0. If `k` is not found, prints 1 followed by the index of the next element in `arr` that is greater than `k`, and the index of `k` in `arr` plus one. The function does not modify the input variables `n`, `arr`, and `k`.

