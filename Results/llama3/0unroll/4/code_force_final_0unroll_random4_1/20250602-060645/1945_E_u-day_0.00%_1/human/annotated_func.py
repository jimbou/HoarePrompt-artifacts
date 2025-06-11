#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a list of integers, where each integer is a value from the space-separated list of integers provided as input through stdin.

#Overall this is what the function does:The function reads a space-separated list of integers from standard input, converts each integer to an integer type, and returns a map object containing the list of integers.

#State of the program right berfore the function call: func_1 is a function that returns an iterator
    return list(func_1())
    #The program returns a list that contains all the values produced by the iterator returned by the function func_1.

#Overall this is what the function does:The function takes no parameters and returns a list containing all values produced by the iterator returned by the function func_1.

#State of the program right berfore the function call: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of distinct integers from 1 to n in arbitrary order, and the function func_1() returns a tuple of two integers (n, k) and the function func_2() returns a list of integers arr.
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: Output State: The value of pos is the index of the first occurrence of k in arr, and the values of n, k, and arr remain unchanged.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: low is the index of the first occurrence of k in arr, high is the index of the first occurrence of k in arr, st is a set of indices of elements in arr that are greater than k, pos is unchanged, n is unchanged, k is unchanged, arr is unchanged.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: 1, 1
    #State: low and high are the indices of the first occurrence of k in arr, st is a set of indices of elements in arr that are greater than k, pos, n, k, and arr remain unchanged. If the current value of arr at index low is equal to k, then 0 is printed. Otherwise, the value of low + 1, which is equal to 2, and pos + 1, which is also equal to 2, are printed.

#Overall this is what the function does:This function determines the position of a target value k in a list of distinct integers arr. It first finds the index of k in arr and then uses a binary search approach to find the first occurrence of k. If k is found at the predicted position, it prints 0. Otherwise, it prints the actual position of k and the predicted position. The function does not modify the input list arr or the values of n and k.

