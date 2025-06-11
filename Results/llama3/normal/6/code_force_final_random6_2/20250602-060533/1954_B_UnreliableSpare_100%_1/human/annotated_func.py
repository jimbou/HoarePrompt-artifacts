#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n) that form a beautiful array.
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: n is an integer between 1 and 3 * 10^5 inclusive, arr is a list of n integers between 1 and n inclusive, stdin is empty, i is n, flag is False if there exists at least one pair of adjacent elements in arr that are not equal, otherwise flag is True.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `n` is an integer between 1 and 3 * 10^5 inclusive, `arr` is a list of `n` integers between 1 and `n` inclusive, `stdin` is empty, `i` is `n`, `flag` is False if there exists at least one pair of adjacent elements in `arr` that are not equal, otherwise `flag` is True, `ans` is the minimum value between the original value of `ans` and the maximum number of consecutive occurrences of `val` in `arr`, `cnt` is 0, and `val` is the first element of `arr`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: 0 or a negative integer (the minimum value between the original value of ans and 0)
    #State: *`n` is an integer between 1 and 3 * 10^5 inclusive, `arr` is a list of `n` integers between 1 and `n` inclusive, `stdin` is empty, `i` is `n`, `ans` is the minimum value between the original value of `ans` and 0, `cnt` is 0, and `val` is the first element of `arr`. If there are no pairs of adjacent elements in `arr` that are not equal, meaning all adjacent elements in `arr` are equal, then -1 is printed. Otherwise, there exists at least one pair of adjacent elements in `arr` that are not equal, and the minimum value between the original value of `ans` and 0 is printed.

#Overall this is what the function does:This function determines the minimum number of consecutive occurrences of an element in a beautiful array. It reads an integer n and a list of n integers from standard input, then checks if all adjacent elements in the list are equal. If they are, it prints -1. Otherwise, it finds the minimum number of consecutive occurrences of any element in the list and prints this value.

