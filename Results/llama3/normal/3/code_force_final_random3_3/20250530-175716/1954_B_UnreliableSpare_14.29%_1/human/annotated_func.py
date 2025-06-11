#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t, then t blocks of input. Each block contains an integer n followed by n integers.
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: stdin contains t-1 blocks of input, each block containing an integer n followed by n integers, n is an integer that must be greater than or equal to 1, arr is a list of n integers, if all elements in arr are equal, then flag is True, otherwise flag is False, and i is n.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: ans is either 0, 1, 2, ..., or n-1, val is the first element of arr, cnt is either 0, 1, 2, ..., or n, stdin contains t-1 blocks of input, each block containing an integer n followed by n integers, n is an integer that must be greater than or equal to 1, arr is a list of n integers, if all elements in arr are equal, then flag is True, otherwise flag is False, and i is n.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: an integer value between 0 and min(n-1, cnt) (inclusive)
    #State: *`ans` is either 0, 1, 2, ..., or min(n-1, cnt), `val` is the first element of `arr`, `cnt` is either 0, 1, 2, ..., or n, stdin contains t-1 blocks of input, each block containing an integer n followed by n integers, n is an integer that must be greater than or equal to 1, arr is a list of n integers, and i is n. If all elements in arr are equal, then -1 is printed. Otherwise, ans (where ans is either 0, 1, 2, ..., or min(n-1, cnt)) is printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints a value. It expects the input to contain multiple blocks, each starting with an integer n followed by n integers. The function checks if all elements in each block are equal. If they are, it prints -1. If they are not, it finds the minimum count of consecutive equal elements in the block and prints this value. The function continues this process until all blocks in the input have been processed.

