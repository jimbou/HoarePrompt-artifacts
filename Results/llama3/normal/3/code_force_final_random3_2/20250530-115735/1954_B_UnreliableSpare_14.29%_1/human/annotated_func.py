#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: n is an integer between 1 and 3 * 10^5, arr is a list of n integers between 1 and n, stdin contains t - 1 test cases, i is n, flag is True if all elements in arr are equal, False otherwise.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: n is an integer between 1 and 3 * 10^5, arr is a list of n integers between 1 and n, stdin contains t - 1 test cases, i is n, flag is True if all elements in arr are equal, False otherwise, ans is the minimum of Infinity and cnt which is ans is 0 or 1 or 2 or 3 or ... or n, and cnt is 0.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: 0
    #State: *`n` is an integer between 1 and 3 * 10^5, `arr` is a list of `n` integers between 1 and `n`, `i` is `n`, `ans` is the minimum of `ans` and `cnt` which is 0, and `cnt` is 0, stdin contains `t - 1` test cases. If all elements in `arr` are equal, -1 is printed. Otherwise, the minimum of `ans` and `cnt` which is 0 is printed.

#Overall this is what the function does:This function reads an integer n and a list of n integers from standard input, checks if all elements in the list are equal, and prints -1 if they are equal or the minimum count of consecutive equal elements if they are not equal.

