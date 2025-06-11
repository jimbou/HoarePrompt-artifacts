#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a result of converting a space-separated string from the input line to an integer.

#Overall this is what the function does:The function reads a line of space-separated integers from standard input, converts each integer string to an integer, and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: func_1 is a function that returns an iterator of values
    return list(func_1())
    #The program returns a list of values returned by the iterator func_1

#Overall this is what the function does:The function accepts an iterator func_1 as input and returns a list of values produced by the iterator. The function does not modify the input iterator and only consumes its values to create the output list. The final state of the program is that the input iterator is exhausted, and the output list contains all the values produced by the iterator.

#State of the program right berfore the function call: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of distinct integers from 1 to n in arbitrary order, and pos is the index of k in arr.
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is a positive integer, `k` is a positive integer such that 1 <= k <= n, `arr` is a list of distinct integers from 1 to n in arbitrary order, `i` is `n-1`. If the current value of `arr[i]` is equal to `k`, then `pos` is `n-1`. Otherwise, `pos` remains -1.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: low is equal to high - 1, st is a set containing all integers from 0 to n-1.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: high (which is low + 1), pos + 1 (where pos is an index or position within the set st or the array arr)
    #State: *low is equal to high - 1, st is a set containing all integers from 0 to n-1. If the current value of arr[low] is equal to k, then 0 is printed. Otherwise, 1 is printed, and the values of low and pos are incremented by 1.

#Overall this is what the function does:Searches for a target value `k` in a list of distinct integers `arr` and prints the result of the search. If `k` is found at the predicted position `pos`, prints 0. Otherwise, prints 1 followed by the actual position of `k` in the list and the predicted position `pos` incremented by 1.

