#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers, which are the result of converting each string in the input list into an integer. The input list is a space-separated list of integers from stdin.

#Overall this is what the function does:The function reads a space-separated list of integers from standard input, converts each integer string into an integer, and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: func_1 is a generator that yields values
    return list(func_1())
    #The program returns a list of values yielded by the generator func_1.

#Overall this is what the function does:This function takes a generator as input, consumes all its yielded values, and returns them as a list. The generator is exhausted after the function call, and the returned list contains all the values yielded by the generator.

#State of the program right berfore the function call: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of n distinct integers from 1 to n in arbitrary order, and pos is the index of k in arr.
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is greater than or equal to 0, `i` is `n-1`, `k` is a reassigned value returned by `func_1()`, `arr` is a reassigned value returned by `func_2()`. If the current value of `arr` at index `i` is equal to the current value of `k`, then `pos` is `i`. Otherwise, `pos` remains -1.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: low is equal to high, st is a set containing all the mid values calculated during the loop execution, n is greater than or equal to 0, i is n-1, k is a reassigned value returned by func_1(), arr is a reassigned value returned by func_2(), pos is either i or -1 depending on whether arr[i] equals k.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: (the next index after low, either n or 0)
    #State: *low is equal to high, st is a set containing all the mid values calculated during the loop execution, n is greater than or equal to 0, i is n-1, k is a reassigned value returned by func_1(), arr is a reassigned value returned by func_2(), pos is either i or -1 depending on whether arr[i] equals k. If the current value of arr[low] is equal to k, then the value 0 is printed. Otherwise, the value 1 is printed, and the value of low + 1 and pos + 1 is printed, where low + 1 is equal to high + 1 and pos + 1 is either i + 1 or 0 depending on whether arr[i] equals k.

#Overall this is what the function does:This function searches for a target value `k` in a list of distinct integers `arr` and determines its presence and position. It first finds the index `pos` of `k` in `arr` if it exists. Then, it performs a binary search to find the position of `k` in `arr`. If `k` is found at the final search position `low`, it prints 0. If `k` is not found, it prints 1 and the next index after `low` (which is `high + 1`) and the position of `k` in `arr` (either `i + 1` or 0). The function does not modify the input list `arr` or the target value `k`.

