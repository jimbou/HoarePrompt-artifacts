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
        
    #State: n is an integer between 1 and 2 * 10^5 and greater than or equal to i, arr is a list of n integers between -n and n, mex is a list containing either 0 or the absolute difference between the absolute value of the current element of arr at index i and minn, minn is either 0, 1, 2, 3, or 4, or the absolute difference between the absolute value of the current element of arr at index i and minn plus 1, maxx is either 0, 1, or the absolute difference between the absolute value of the current element of arr at index i and minn, i is equal to n, stdin contains t-n test cases. If arr[i] > 0, then the last element of mex is equal to the previous value of minn, and minn is one more than its previous value. If minn is equal to maxx, then minn is one more than maxx. If arr[i] <= 0, then if the absolute difference between the absolute value of the current element of arr at index i and minn is greater than maxx, then maxx is updated to the absolute difference between the absolute value of the current element of arr at index i and minn.
    for itm in mex:
        print(itm, end=' ')
        
    #State: The loop has executed for all elements in the mex list, printing each element in the list. The loop has finished executing, and the program has terminated.
    print()
    #This is printed: a blank line

#Overall this is what the function does:This function reads an integer n and a list of n integers from standard input, then prints a list of integers to standard output. The output list is generated based on the input list, where each element is either the current minimum value (minn) if the corresponding input element is positive, or the absolute difference between the absolute value of the input element and the current minimum value (minn) if the input element is non-positive. The function also updates the minimum value (minn) and maximum value (maxx) based on the input elements. The function prints each element of the output list followed by a space, and finally prints a blank line.

