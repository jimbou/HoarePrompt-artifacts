#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n) such that the list is beautiful.
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: n is an integer between 1 and 3 * 10^5 inclusive, arr is a list of n integers between 1 and n inclusive, stdin contains t - 1 test cases, i is n, flag is False if there exists at least one pair of adjacent elements in arr that are not equal, otherwise flag is True.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: n is an integer between 1 and 3 * 10^5 inclusive, arr is a list of n integers between 1 and n inclusive, stdin contains t - 1 test cases, i is n, flag is False if there exists at least one pair of adjacent elements in arr that are not equal, otherwise flag is True, ans is the minimum of its original value and the number of consecutive elements in arr that are equal to the first element of arr, val is the first element of arr, cnt is the number of consecutive elements in arr that are equal to the first element of arr.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: the minimum number of consecutive elements in `arr` that are equal to the first element of `arr`
    #State: *`n` is an integer between 1 and 3 * 10^5 inclusive, `arr` is a list of `n` integers between 1 and `n` inclusive, stdin contains `t - 1` test cases, `i` is `n`, `val` is the first element of `arr`, `cnt` is the number of consecutive elements in `arr` that are equal to the first element of `arr`. If all adjacent elements in `arr` are equal, then `flag` is `True`, `ans` is the minimum of its original value and `n`, and -1 is printed. Otherwise, `flag` is `False`, `ans` is the minimum of its original value and the number of consecutive elements in `arr` that are equal to the first element of `arr`, and this minimum value is printed.

#Overall this is what the function does:This function reads an integer `n` and a list of `n` integers from standard input, then determines the minimum number of consecutive elements in the list that are equal to the first element. If all adjacent elements in the list are equal, it prints -1; otherwise, it prints the minimum number of consecutive elements equal to the first element.

