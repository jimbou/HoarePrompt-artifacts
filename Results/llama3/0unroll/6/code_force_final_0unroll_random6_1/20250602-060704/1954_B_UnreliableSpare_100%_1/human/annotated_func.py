#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: The value of flag is False if there exists at least one pair of adjacent elements in arr that are not equal, otherwise flag remains True. The value of i is n-1. The values of t, n, and arr remain unchanged.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: Output State: The value of ans is the minimum number of consecutive occurrences of the first element of arr in arr, val is equal to the first element of arr, cnt is 0, and the values of flag, i, t, n, and arr remain unchanged.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: the minimum of the current value of ans and 0
    #State: *The value of `ans` is the minimum of its current value and 0, `val` is equal to the first element of `arr`, `cnt` is 0, and the values of `i`, `t`, `n`, and `arr` remain unchanged. If `flag` is True, -1 is printed. If `flag` is False, the value of `ans` which is the minimum of its current value and 0 is printed.

#Overall this is what the function does:This function reads an integer n and a list of n integers from standard input, checks if all elements in the list are equal, and if not, finds the minimum number of consecutive occurrences of the first element in the list. If all elements are equal, it prints -1; otherwise, it prints the minimum number of consecutive occurrences.

