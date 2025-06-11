#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n) that form a beautiful array.
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: flag is False if there exists at least one pair of adjacent elements in the array that are not equal, otherwise flag remains True. The value of n and the array arr remain unchanged.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: Output State: flag remains True if the array arr contains all equal elements, otherwise flag is False. The value of n and the array arr remain unchanged. ans is the minimum number of consecutive equal elements in the array arr, val is the first element of the array arr, and cnt is the number of consecutive equal elements ending at the last index of the array arr.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: the minimum number of consecutive equal elements in the array arr
    #State: flag remains True if the array arr contains all equal elements, otherwise flag is False. The value of n and the array arr remain unchanged. ans is the minimum number of consecutive equal elements in the array arr, val is the first element of the array arr, and cnt is the number of consecutive equal elements ending at the last index of the array arr. If the array arr contains all equal elements, -1 is printed. Otherwise, the minimum number of consecutive equal elements in the array arr is printed.

#Overall this is what the function does:This function determines the minimum number of consecutive equal elements in an array. It reads an integer n and an array of n integers from standard input, checks if all elements in the array are equal, and prints -1 if they are. Otherwise, it finds the minimum number of consecutive equal elements and prints this value. The function does not modify the input array.

