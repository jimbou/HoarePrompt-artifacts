#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: stdin contains t-1 test cases, n is an integer between 1 and 3 * 10^5, arr is a list of n integers between 1 and n, flag is False if there exists at least one pair of adjacent elements in arr that are not equal, otherwise flag is True.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: Output State: The value of ans is the minimum number of consecutive occurrences of the first element in arr, cnt is the total number of occurrences of the first element in arr, and the values of the other variables remain unchanged.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: the minimum between the previous minimum number of consecutive occurrences of the first element in arr and the total number of occurrences of the first element in arr
    #State: *The value of ans is the minimum between the previous minimum number of consecutive occurrences of the first element in arr and the total number of occurrences of the first element in arr, cnt is the total number of occurrences of the first element in arr, and the values of the other variables remain unchanged. If flag is True, -1 is printed. Otherwise, the value of ans is printed.

#Overall this is what the function does:This function reads an integer n and a list of n integers from standard input, checks if all elements in the list are equal, and if not, finds the minimum number of consecutive occurrences of the first element in the list. If all elements are equal, it prints -1; otherwise, it prints the minimum number of consecutive occurrences.

