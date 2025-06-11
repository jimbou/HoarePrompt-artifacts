#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (1 <= n <= 2 * 10^5) and then n integers a_1, a_2, ..., a_n (-n <= a_i <= n).
    n = int(input())
    arr = list(map(int, input().split()))
    mex = []
    minn = 0
    maxx = 0
    for i in range(n):
        if arr[i] > 0:
            mex.append(minn)
            minn += 1
            if minn == maxx:
                minn = maxx + 1
        else:
            mex.append(abs(arr[i] - minn))
            if abs(arr[i] - minn) > maxx:
                maxx = abs(arr[i] - minn)
        
    #State: `n` is an integer greater than or equal to 0, `arr` is a list of `n` integers `a_1`, `a_2`, ..., `a_n` (-`n` <= `a_i` <= `n`), `mex` is a list containing either the value 0 or the absolute difference between the absolute value of `arr[i]` and `minn` which is either 0, 1, or `maxx + 2`, `minn` is either 0, 1, or `maxx + 1`, `maxx` is either 0 or the absolute difference between `arr[i]` and `minn` if the absolute difference between `arr[i]` and `minn` is greater than `maxx`, otherwise `maxx` remains 0, `i` is `n`, and the current value of `arr[i]` is either greater than 0 or less than or equal to 0. If `minn` is equal to `maxx`, then `minn` is updated to `maxx + 1. If `arr[i]` is greater than 0, `mex` is updated with either the value 0 or the absolute difference between the absolute value of `arr[i]` and `minn` which is either 1 or `maxx + 2`, and `minn` is updated to either 1 or `maxx + 1`. If `arr[i]` is less than or equal to 0, `mex` is updated with the absolute difference between `arr[i]` and `minn`, and `minn` is updated to either 0 or `maxx + 1` if `minn` is equal to `maxx`. If the absolute difference between `arr[i]` and `minn` is greater than `maxx`, then `maxx` is updated to the absolute difference between `arr[i]` and `minn`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: mex is a list that must have at least n elements, itm is the nth element in the list, and the first element of the list mex which is itm is printed followed by a space.
    print()
    #This is printed: the first element of the list mex which is itm followed by a space

#Overall this is what the function does:This function takes an integer n and a list of n integers as input, processes the list based on the values of the integers, and prints a new list of integers. The function generates a new list, mex, where each element is either the minimum non-negative integer not present in the input list or the absolute difference between the absolute value of an input integer and the minimum non-negative integer not present in the input list. The function then prints the elements of the mex list, separated by spaces.

