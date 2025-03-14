#State of the program right berfore the function call: No variables are present in the function signature. This function is expected to read input from the standard input and return a map object containing integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object containing integers that are parsed from the input string, where the input string is split by whitespace.
#Overall this is what the function does:The function `func_1` reads a line of input from the standard input, splits it into substrings separated by whitespace, converts each substring into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: The function `func_2` does not take any parameters and returns a list generated by the function `func_1`.
def func_2():
    return list(func_1())
    #The program returns a list generated by the function `func_1`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list generated by the function `func_1`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is a positive integer representing the number to be found such that 1 <= k <= n. arr is a list of integers representing the permutation of length n, where each integer from 1 to n appears exactly once.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` and `k` are the values returned by `func_1()`, `arr` is the value returned by `func_2()`, `pos` is the index of the first occurrence of `k` in `arr` or `-1` if `k` is not found in `arr`.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `low` and `high` are consecutive, `st` contains all the midpoints used in the binary search, `pos` and `arr` are unchanged, `n` and `k` are unchanged.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: high, pos + 1 (where high is the integer consecutive to low and pos is the position indicator in the binary search)
    #State: `low` and `high` are consecutive, `st` contains all the midpoints used in the binary search, `pos` and `arr` are unchanged, `n` and `k` are unchanged. If `arr[low]` equals `k`, then `arr[low]` equals `k`. Otherwise, `arr[low]` is not equal to `k`.
#Overall this is what the function does:The function finds the position of a given integer `k` in a permutation `arr` of length `n`. It then performs a binary search to determine a specific condition related to `k` in the permutation. If `k` is found at the position indicated by the binary search (`low`), it prints `0`. Otherwise, it prints `1` followed by `low + 1` and the position of `k` in the permutation (`pos + 1`).

