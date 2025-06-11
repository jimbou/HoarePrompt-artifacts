#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return map(int, input().split())
    #The program returns a map object that contains the integers from the input line, split by spaces.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns a map object containing these integers.

#State of the program right berfore the function call: func_1 is a generator that yields values
    return list(func_1())
    #The program returns a list of values yielded by the generator func_1.

#Overall this is what the function does:The function accepts a generator as input and returns a list of all values yielded by the generator. The function does not modify the input generator or any external state; it solely converts the generator's output into a list. Upon conclusion, the program's state is updated with the returned list, which contains all values produced by the generator.

#State of the program right berfore the function call: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of distinct integers from 1 to n in arbitrary order, and the function func_1() returns a tuple of two integers (n, k), and the function func_2() returns a list of integers arr.
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: n is a positive integer, k is a positive integer such that 1 <= k <= n, arr is a list of distinct integers from 1 to n in arbitrary order, pos is the index of the element k in the list arr if k exists in arr, otherwise pos is -1.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: low = pos, high = pos + 1, st = a set of integers from 0 to n-1 that are greater than pos, pos remains the same, n remains the same, k remains the same, arr remains the same.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: pos + 1, pos + 1 (where pos is the unchanged value of pos)
    #State: low equals pos, high equals pos + 1, st is a set of integers from 0 to n-1 that are greater than pos, pos remains the same, n remains the same, k remains the same, arr remains the same. If the current value of arr at index low is equal to k, then 0 is printed. Otherwise, 1 is printed and (pos + 1, pos + 2) is printed.

#Overall this is what the function does:This function searches for a target integer k in a list of distinct integers arr and prints the result. If k is found at the expected position, it prints 0. If k is not found at the expected position, it prints 1 and the expected position of k. The function does not modify the input list or variables.

