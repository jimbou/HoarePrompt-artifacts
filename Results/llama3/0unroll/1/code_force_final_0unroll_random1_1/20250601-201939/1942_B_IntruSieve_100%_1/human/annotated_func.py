#State of the program right berfore the function call: stdin contains multiple inputs: first an integer (number of test cases), then for each test case, first an integer (length of the array), then a list of integers (the array). The length of the array is a positive integer and the integers in the array are between -n and n (inclusive).
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
        
    #State: The output state is a list of integers representing the minimum excluded value (mex) for each iteration of the loop, and a dictionary (used) that keeps track of the used values. The variable minn is updated to the next available minimum excluded value after each iteration.
    for itm in mex:
        print(itm, end=' ')
        
    #State: The list of integers representing the minimum excluded value (mex) for each iteration of the loop remains unchanged, and the dictionary (used) that keeps track of the used values remains unchanged. The variable minn remains unchanged as well.
    print()
    #This is printed: None

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the minimum excluded value (mex) for each iteration of the loop. It takes no arguments and returns None. The function's purpose is to calculate and display the mex values based on the input array. The final state of the program is that the mex values are printed to the console, and the input variables (n, arr, mex, minn, and used) remain unchanged after the function concludes.

