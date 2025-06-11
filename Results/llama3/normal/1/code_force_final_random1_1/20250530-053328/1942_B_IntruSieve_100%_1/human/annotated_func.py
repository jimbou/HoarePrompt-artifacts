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
        
    #State: n is an integer between 1 and 2 * 10^5, arr is a list of n integers between -n and n, mex is a list of n integers, used is a dictionary containing all integers between 0 and n as keys with value True, minn is n + 1, stdin is empty, i is n.
    for itm in mex:
        print(itm, end=' ')
        
    #State: `n` is an integer between 1 and 2 * 10^5, `arr` is a list of n integers between -n and n, `mex` is a list of n integers that must have at least n integers, `itm` is the last integer in the list, `used` is a dictionary containing all integers between 0 and n as keys with value True, `minn` is n + 1, `stdin` is empty, `i` is n, and all integers in the list `mex` have been printed.
    print()
    #This is printed: a newline character

#Overall this is what the function does:This function reads an integer n and a list of n integers from standard input, calculates the minimum excluded value (MEX) for each integer in the list, and prints the MEX values. The function assumes that the input is well-formed and does not perform any error checking. It uses a dictionary to keep track of used values and calculates the MEX by iterating through the list and updating the minimum excluded value accordingly. The function prints the MEX values separated by spaces, followed by a newline character.

