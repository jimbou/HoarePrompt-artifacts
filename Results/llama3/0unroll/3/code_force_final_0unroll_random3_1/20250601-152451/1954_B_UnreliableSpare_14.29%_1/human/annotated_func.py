#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n) that form a beautiful array.
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: stdin contains t-1 test cases, n is an integer between 1 and 3 * 10^5, arr is a list of n integers between 1 and n, flag is False if there exists at least one pair of adjacent elements in arr that are not equal, otherwise flag is True.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: ans is the minimum number of consecutive equal elements in arr, val is the last element of arr, cnt is the number of consecutive equal elements ending at the last element of arr, n is an integer between 1 and 3 * 10^5, arr is a list of n integers between 1 and n, flag is False if there exists at least one pair of adjacent elements in arr that are not equal, otherwise flag is True, stdin contains t-1 test cases.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: the minimum number of consecutive equal elements in the list arr
    #State: `ans` is the minimum of the previous minimum number of consecutive equal elements in `arr` and the number of consecutive equal elements ending at the last element of `arr`, `val` is the last element of `arr`, `cnt` is the number of consecutive equal elements ending at the last element of `arr`, `n` is an integer between 1 and 3 * 10^5, `arr` is a list of n integers between 1 and n. If all adjacent elements in `arr` are equal, -1 is printed. Otherwise, there exists at least one pair of adjacent elements in `arr` that are not equal, and the minimum of the previous minimum number of consecutive equal elements in `arr` and the number of consecutive equal elements ending at the last element of `arr` which is `ans` is being printed.

#Overall this is what the function does:This function reads an integer n and a list of n integers from standard input, checks if the list contains at least one pair of adjacent elements that are not equal, and prints the minimum number of consecutive equal elements in the list if such a pair exists, otherwise prints -1.

