#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (-n <= a_i <= n).
    n = int(input())
    arr = list(map(int, input().split()))
    mex = []
    minn = 0
    used = {}
    for i in range(n):
        if arr[i] > 0:
            mex.append(minn)
            used[minn] = True
            while minn in used:
                minn += 1
        else:
            mex.append(abs(arr[i] - minn))
            used[abs(arr[i] - minn)] = True
        
    #State: Output State: The loop iterates over the array 'arr' of length 'n'. For each positive element in 'arr', it appends the current value of 'minn' to the list 'mex', marks 'minn' as used, and increments 'minn' until it finds an unused value. For each non-positive element in 'arr', it appends the absolute difference between the element and 'minn' to 'mex' and marks this difference as used. After the loop, 'mex' contains the minimum excluded values for each element in 'arr', 'used' contains all the values that have been used, and 'minn' is the smallest unused value.
    for itm in mex:
        print(itm, end=' ')
        
    #State: Output State: The loop prints all the elements in 'mex' separated by a space, and 'mex', 'used', and 'minn' remain unchanged.
    print()
    #This is printed: all the elements in 'mex' separated by a space

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases, and then for each test case, it reads an integer n followed by n integers. It calculates the minimum excluded values for each element in the array and prints these values separated by a space. The function does not return any value but prints the results directly to the console.

