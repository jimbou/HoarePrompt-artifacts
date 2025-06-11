#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains one input: a positive integer n. The second line contains n inputs: a sequence of positive integers.
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: n is a positive integer, i is n - 1, arr is a list of n positive integers, flag is True if all elements in arr are equal, False otherwise, stdin contains multiple test cases - 2.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `n` is a positive integer, `i` is `n - 1`, `arr` is a list of `n` positive integers, `flag` is True if all elements in `arr` are equal, False otherwise, `stdin` contains multiple test cases - 2, `ans` is either 0, 1, or the length of the longest contiguous subarray of `arr` with all elements equal to `val`, `val` is the first element of `arr`, and `cnt` is either 0 or the length of the longest contiguous subarray of `arr` with all elements equal to `val` ending at index `n - 1`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: the minimum length of the longest contiguous subarray of `arr` with all elements equal to `val` ending at index `n - 1`, or 0 if no such subarray exists
    #State: *`n` is a positive integer, `i` is `n - 1`, `arr` is a list of `n` positive integers, `stdin` contains multiple test cases - 2, `val` is the first element of `arr`, `cnt` is either 0 or the length of the longest contiguous subarray of `arr` with all elements equal to `val` ending at index `n - 1`, and `ans` is the minimum of its previous value and `cnt`. If all elements in `arr` are equal, -1 is printed. Otherwise, the minimum of the previous value of `ans` and `cnt` is being printed.

#Overall this is what the function does:This function reads a positive integer n and a sequence of n positive integers from standard input, and prints the minimum length of the longest contiguous subarray with all elements equal to the first element of the sequence. If all elements in the sequence are equal, it prints -1.

