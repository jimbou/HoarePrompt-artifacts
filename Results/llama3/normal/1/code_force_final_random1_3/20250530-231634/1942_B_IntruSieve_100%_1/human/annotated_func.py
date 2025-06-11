#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The integer is a positive integer and represents the length of the list. The list contains integers in the range -n to n, where n is the length of the list.
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
        
    #State: n is greater than or equal to 0, i is n, arr is a list of integers in the range -n to n, mex contains the absolute differences between the elements of arr and minn if the elements are not greater than 0, used contains the absolute differences between the elements of arr and minn as keys with value True, and minn is the smallest non-negative integer that is not in used if any element of arr is greater than 0, otherwise minn is 0.
    for itm in mex:
        print(itm, end=' ')
        
    #State: `n` is greater than or equal to 0, `i` is `n`, `arr` is a list of integers in the range -n to n, `mex` is an empty list, `used` contains the absolute differences between the elements of `arr` and `minn` as keys with value True, `minn` is the smallest non-negative integer that is not in `used` if any element of `arr` is greater than 0, otherwise `minn` is 0, and all elements in `mex` have been printed.
    print()
    #This is printed: Nothing

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts no parameters and returns no value. The function reads a positive integer n and a list of integers of length n from stdin, where the integers are in the range -n to n. It then calculates the absolute differences between the elements of the list and a minimum value minn, and prints these differences. The function also keeps track of the used values in a dictionary. After processing the input, the function prints the calculated differences and an empty line. The final state of the program is that all input has been processed and the output has been printed.

