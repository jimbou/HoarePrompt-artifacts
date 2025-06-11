#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a list of integers, where each integer is a value from the input provided in stdin, split by spaces.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns a map object containing the list of integers.

#State of the program right berfore the function call: func_1 is a generator that yields values of any type and value
    return list(func_1())
    #The program returns a list containing all the values yielded by the generator func_1, where each value can be of any type and value.

#Overall this is what the function does:The function accepts a generator as input and returns a list containing all the values yielded by the generator, regardless of their type or value.

#State of the program right berfore the function call: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of distinct integers from 1 to n in arbitrary order, and the function func_1() returns a tuple of two integers (n, k), and the function func_2() returns a list of integers.
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: Output State: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of integers, pos is the index of the first occurrence of k in arr if k exists in arr, otherwise pos is -1.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: low is the index of the first occurrence of k in arr if k exists in arr, otherwise low is the index of the first element in arr that is greater than k, high is low + 1, st is a set of indices of elements in arr that were used to find the first occurrence of k or the first element greater than k.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: the index of the second element in arr that is greater than k, or the index of the first element in arr that is greater than or equal to k, 1
    #State: *low is the index of the first occurrence of k in arr if k exists in arr, otherwise low is the index of the first element in arr that is greater than k, high is low + 1, st is a set of indices of elements in arr that were used to find the first occurrence of k or the first element greater than k. If the element at index low in arr is equal to k, 0 is printed. Otherwise, arr[low] is not equal to k, 1 is printed, and the values of low + 1 and pos + 1 are printed.

#Overall this is what the function does:This function determines the position of a target element k in a list arr of distinct integers from 1 to n. It first finds the index of the first occurrence of k in arr, if it exists. If k is found, the function prints 0. If k is not found, the function prints 1, followed by the index of the first element in arr that is greater than k and the index of the first occurrence of k in arr (or -1 if k is not present). The function uses a binary search approach to find the position of k or the first element greater than k in arr.

