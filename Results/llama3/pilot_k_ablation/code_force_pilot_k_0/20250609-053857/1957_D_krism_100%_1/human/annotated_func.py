#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The integer is a positive integer and represents the length of the list. The list contains positive integers.
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: Output State: prefix is a list of integers where each element is the XOR of the corresponding element in arr and the previous element in prefix, n remains unchanged, arr remains unchanged, stdin remains unchanged.
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: Output State: prefix remains unchanged, n remains unchanged, arr remains unchanged, stdin remains unchanged, pre is a list of 32 lists where each sublist contains two elements, the first element of each sublist is 1 and the second element is 0, suf is a list of 32 lists where each sublist contains two elements initialized to 0.
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: Output State: The output state after the loop executes all the iterations is: prefix remains unchanged, n remains unchanged, arr remains unchanged, stdin remains unchanged, pre is a list of 32 lists where each sublist contains two elements, the first element of each sublist is 1 and the second element is 0, suf is a list of 32 lists where each sublist contains two elements, the first element of each sublist is the number of times the corresponding bit is set in the prefix array from index n to 1, and the second element is the number of times the corresponding bit is not set in the prefix array from index n to 1.
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
        
    #State: Output State: `ans` is the total number of pairs of elements in the prefix array from index 1 to n that have the same bit set or not set at the same position, prefix remains unchanged, n remains unchanged, arr remains unchanged, stdin remains unchanged, pre is a list of 32 lists where each sublist contains two elements, the first element of each sublist is the number of times the corresponding bit is set in the prefix array from index 1 to n, and the second element is the number of times the corresponding bit is not set in the prefix array from index 1 to n, suf is a list of 32 lists where each sublist contains two elements, the first element of each sublist is 0, and the second element is the number of times the corresponding bit is not set in the prefix array from index 1 to n.
    print(ans)
    #This is printed: The total number of pairs of elements in the prefix array from index 1 to n that have the same bit set or not set at the same position

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a list of n positive integers. It calculates the total number of pairs of elements in the prefix XOR array that have the same bit set or not set at the same position, and prints this count for each test case. The function does not modify the input values or standard input.

