#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: stdin contains t-1 test cases, n is an integer between 1 and 10^5, arr is a list of n integers between 1 and 10^9, prefix is a list of n+1 integers where each element is the XOR of the corresponding element in arr and the previous element in prefix.
    print(arr, prefix)
    #This is printed: [list of n integers between 1 and 10^9], [list of n+1 integers where each element is the XOR of the corresponding element in arr and the previous element in prefix]
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: Output State: The value of pre[i][0] is incremented by 1 for each iteration of the loop, resulting in pre[i][0] being equal to 33 after the loop finishes executing. The values of the other variables remain unchanged.
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: Output State: The value of suf[j][0] is incremented by 1 for each iteration of the loop where cur >> j & 1 is False, and the value of suf[j][1] is incremented by 1 for each iteration of the loop where cur >> j & 1 is True.
    print(pre)
    #This is printed: the prefix sums of the binary representation of the numbers from 0 to n, where n is the length of the input array
    print(suf)
    #This is printed: A list of lists, where each inner list contains two elements, the first element is the count of iterations where cur >> j & 1 is False, and the second element is the count of iterations where cur >> j & 1 is True.
    ans = 0
    for i in range(1, n + 1):
        y = arr[i - 1]
        
        k = y.bit_length() - 1
        
        ans += pre[k][0] * suf[k][0] + pre[k][1] * suf[k][1]
        
        c = prefix[i]
        
        for j in range(32):
            if c >> j & 1:
                pre[j][1] += 1
                suf[j][1] -= 1
            else:
                pre[j][0] += 1
                suf[j][0] -= 1
        
    #State: Output State: The value of suf[j][0] is incremented by 1 for each iteration of the loop where cur >> j & 1 is False, and the value of suf[j][1] is incremented by 1 for each iteration of the loop where cur >> j & 1 is True, and the value of pre is printed, and suf is printed, and ans is the sum of the products of the corresponding elements of pre and suf for each iteration of the loop.
    print(ans)
    #This is printed: sum of products of corresponding elements of pre and suf after loop iterations

#Overall this is what the function does:This function reads an integer t from standard input, followed by t test cases. Each test case consists of an integer n and a list of n integers. The function calculates the XOR prefix sum of the list and then iterates over the list to calculate the sum of products of corresponding elements of two lists, pre and suf, which are initialized with zeros. The function prints the sum of these products for each test case.

