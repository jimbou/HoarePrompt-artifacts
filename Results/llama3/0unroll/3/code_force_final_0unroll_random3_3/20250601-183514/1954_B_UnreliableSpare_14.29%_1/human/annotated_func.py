#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n) that form a beautiful array.
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: stdin contains t-1 test cases, n is an integer between 1 and 3 * 10^5 inclusive, arr is a list of n integers between 1 and n inclusive, flag is False
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: Output State: The value of cnt is the number of occurrences of the first element of arr in arr, and the value of ans is the minimum number of occurrences of any element in arr that is equal to the first element of arr. The values of t, n, flag, and val remain unchanged.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: the minimum value between the previous value of ans and the count of the first element of arr in arr
    #State: *The value of `ans` is the minimum of its previous value and the number of occurrences of the first element of `arr` in `arr`, and the values of `t`, `n`, `val` remain unchanged. If `flag` is True, -1 is printed. If `flag` is False, the value of `ans` is printed.

#Overall this is what the function does:This function reads an integer n and a list of n integers from standard input, checks if all elements in the list are the same, and prints the minimum count of any element in the list if they are not all the same, otherwise prints -1.

