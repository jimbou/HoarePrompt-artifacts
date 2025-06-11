#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The integer is a positive integer and represents the length of the list. The list contains integers between -n and n, where n is the length of the list.
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
        
    #State: Output State: The list mex contains the minimum excluded value for each positive integer in the input list arr, and the dictionary used keeps track of the used values. The variable minn is updated to the next available minimum excluded value after each iteration. The other variables n and arr remain unchanged.
    for itm in mex:
        print(itm, end=' ')
        
    #State: Output State: The list mex contains the minimum excluded value for each positive integer in the input list arr, and the dictionary used keeps track of the used values. The variable minn is updated to the next available minimum excluded value after each iteration. The other variables n and arr remain unchanged.
    print()
    #This is printed: The minimum excluded value for each positive integer in the input list arr, which is the value of mex, and the used values, which is the value of used

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the minimum excluded value for each positive integer in the input list. It takes no parameters and returns no value. The function reads two inputs from stdin: an integer representing the length of a list, and a list of integers. It then calculates the minimum excluded value for each positive integer in the list and prints these values. The function also keeps track of used values in a dictionary, but this is not output. The function does not modify the input list or its length.

