#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (-n <= a_i <= n).
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
        
    #State: mex contains the absolute values of the differences between each element of arr and minn, minn is updated to maxx + 1 if minn equals maxx, and maxx is updated to the maximum absolute value of the differences between each element of arr and minn.
    for itm in mex:
        print(itm, end=' ')
        
    #State: `mex` is an empty list, `itm` is not defined, `minn` is updated to `maxx + 1` if `minn` equals `maxx`, and `maxx` is updated to the maximum absolute value of the differences between each element of `arr` and `minn`, and no elements are being printed.
    print()
    #This is printed: Nothing

#Overall this is what the function does:This function reads an integer n and a list of n integers from standard input, calculates the absolute differences between each element and a minimum value, updates the minimum value if necessary, and prints the calculated differences.

