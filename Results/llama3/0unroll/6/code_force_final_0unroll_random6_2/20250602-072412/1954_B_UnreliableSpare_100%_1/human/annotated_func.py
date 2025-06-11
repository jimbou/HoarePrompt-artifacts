#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: n is an integer between 1 and 3 * 10^5, arr is a list of n integers between 1 and n, flag is False if there exists at least one pair of adjacent elements in arr that are not equal, otherwise flag is True, stdin contains t - 1 test cases.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: Output State: The value of ans is the minimum length of a subarray in arr with all elements equal to val, and the value of cnt is the length of the last subarray in arr with all elements equal to val.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: minimum length of a subarray in `arr` with all elements equal to `val`
    #State: The value of `ans` is the minimum length of a subarray in `arr` with all elements equal to `val`, which is the minimum of its previous value and `cnt`, and the value of `cnt` is the length of the last subarray in `arr` with all elements equal to `val`. If `flag` is True, -1 is printed. Otherwise, the minimum length of a subarray in `arr` with all elements equal to `val`, which is `ans`, is printed.

#Overall this is what the function does:This function reads an integer n and a list of n integers from standard input, checks if all elements in the list are equal, and if not, finds the minimum length of a subarray with all elements equal. If all elements are equal, it prints -1; otherwise, it prints the minimum length of a subarray with all elements equal.

