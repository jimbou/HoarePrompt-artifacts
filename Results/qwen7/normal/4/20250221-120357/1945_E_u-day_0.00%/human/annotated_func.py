#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4, n is an integer such that 1 ≤ n ≤ 2⋅10^5, x is an integer such that 1 ≤ x ≤ n, and p is a list of n integers representing a permutation where 1 ≤ p_i ≤ n for all i.
def func_1():
    return map(int, input().split())
    #The program returns a map object containing integers split from user input.
#Overall this is what the function does:The function reads a line of space-separated integers from the user input, converts each integer to a string, and returns a map object containing these integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of n and x where 1 ≤ x ≤ n ≤ 2⋅10^5, and p is a list of integers representing a permutation of size n.
def func_2():
    return list(func_1())
    #The program returns a list generated by func_1(), which is not defined in the given information.
#Overall this is what the function does:The function does not accept any parameters and returns a list generated by `func_1()`. The nature of the actions performed by `func_1()` are not specified in the given information.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, k is an integer such that 1 ≤ k ≤ n, and arr is a list of n distinct integers from 1 to n representing the permutation.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: Output State: After the loop executes all the iterations, the postcondition is that `n` must be greater than or equal to the final value of `i`, which is `n-1` (since `i` starts from 0 and increments by 1 in each iteration up to `n-1`). The variable `i` will be equal to `n-1`. The variable `pos` will be set to the index of the first occurrence of `k` in `arr` if `k` exists in `arr`, otherwise it will remain `-1`.
    #
    #In simpler terms, `n` will be at least as large as the last index checked by the loop, `i` will be the last index checked (`n-1`), and `pos` will either be the index where `k` was found in `arr` or will still be `-1` if `k` was not found.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: The final state of the loop will have `low` equal to `high` or `low + 1` equal to `high`, indicating the search range has been narrowed down as much as possible. The set `st` will contain all the midpoints calculated during the iterations of the loop.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: low + 1, low + 1
    #State: The final state of the loop will have `low` equal to `high` or `low + 1` equal to `high`, indicating the search range has been narrowed down as much as possible. The set `st` will contain all the midpoints calculated during the iterations of the loop. Additionally, `arr[low]` will be equal to `k` if the condition `arr[low] == k` is met in the if part, and not equal to `k` if the else part is executed.
#Overall this is what the function does:The function accepts a positive integer `n` representing the length of a permutation, an integer `k` such that \(1 \leq k \leq n\), and a list `arr` of `n` distinct integers from 1 to n representing the permutation. It performs a binary search to find the position of `k` in `arr`. If `k` is found, it prints 0. If `k` is not found, it prints 1 followed by the index where `k` would be inserted to maintain the sorted order and the index of the first occurrence of `k` in `arr` (or -1 if not found). The function returns nothing.

