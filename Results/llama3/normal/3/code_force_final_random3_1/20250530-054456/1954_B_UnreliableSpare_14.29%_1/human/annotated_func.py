#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 3 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: n is an integer between 1 and 3 * 10^5, i is n, arr is a list of n integers between 1 and n, stdin contains multiple test cases minus 1, flag is False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: `n` is an integer between 1 and 3 * 10^5, `i` is `n`, `n` must be greater than or equal to 0, arr is a list of `n` integers between 1 and `n`, stdin contains multiple test cases minus 1, flag is False, ans is the minimum of Infinity and cnt, val is the first integer in arr, and cnt is either the number of times `val` appears in arr if `arr[i]` is equal to `val`, or the number of times `val` appears in arr minus 1 if the last element of arr is not equal to val.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: the minimum of the minimum of Infinity and cnt, and the number of times val appears in arr if arr[i] is equal to val, or the minimum of the minimum of Infinity and cnt, and the number of times val appears in arr minus 1 if the last element of arr is not equal to val (where cnt is the number of times val appears in arr if arr[i] is equal to val, or the number of times val appears in arr minus 1 if the last element of arr is not equal to val, and val is the first integer in arr)
    #State: `n` is an integer between 1 and 3 * 10^5, `i` is `n`, `n` must be greater than or equal to 0, arr is a list of `n` integers between 1 and `n`, stdin contains multiple test cases minus 1, val is the first integer in arr, and cnt is either the number of times `val` appears in arr if `arr[i]` is equal to `val`, or the number of times `val` appears in arr minus 1 if the last element of arr is not equal to val. If flag is True, -1 is printed. Otherwise, ans is the minimum of the minimum of Infinity and cnt, and the number of times `val` appears in arr if `arr[i]` is equal to `val`, or the minimum of the minimum of Infinity and cnt, and the number of times `val` appears in arr minus 1 if the last element of arr is not equal to val, and ans is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the minimum count of consecutive occurrences of the first integer in each test case. If all integers in a test case are the same, it prints -1.

