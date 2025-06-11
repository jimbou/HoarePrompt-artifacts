#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains a single integer n (1 <= n <= 10^5). Each of the following t lines contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: The prefix list now contains n+1 elements, where each element is the XOR of the corresponding element in the arr list and the previous element in the prefix list. The value of n and the contents of stdin remain unchanged.
    print(arr, prefix)
    #This is printed: [arr list], [prefix list where each element is the XOR of the corresponding element in arr and the previous element in prefix]
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: Output State: The prefix list still contains n+1 elements, where each element is the XOR of the corresponding element in the arr list and the previous element in the prefix list. The value of n and the contents of stdin remain unchanged. The contents of the arr list and the prefix list are still being printed. The two new lists, pre and suf, each contain 32 sublists, but now each sublist in pre has been updated to [1, 0], while the sublists in suf remain unchanged at [0, 0].
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: Output State: The prefix list still contains n+1 elements, where each element is the XOR of the corresponding element in the arr list and the previous element in the prefix list. The value of n remains unchanged. The contents of the arr list and the prefix list are still being printed. The two new lists, pre and suf, each contain 32 sublists. Each sublist in pre still contains [1, 0], while each sublist in suf now contains the correct count of 1s and 0s for each bit position in the prefix list.
    print(pre)
    #This is printed: [[1, 0], [1, 0], [1, 0], ..., [1, 0]] (32 sublists, each containing [1, 0])
    print(suf)
    #This is printed: A list of 32 sublists, where each sublist contains the count of 1s and 0s for each bit position in the prefix list
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
        
    #State: Output State: The prefix list still contains n+1 elements, where each element is the XOR of the corresponding element in the arr list and the previous element in the prefix list. The value of n remains unchanged. The contents of the arr list and the prefix list are still being printed. The two new lists, pre and suf, each contain 32 sublists. Each sublist in pre contains the correct count of 1s and 0s for each bit position in the prefix list, and the contents of the pre list are printed. Each sublist in suf contains [0, 0], and the contents of the suf list are printed. The variable ans is assigned the value equal to the sum of the products of the counts of 1s and 0s for each bit position in the prefix list.
    print(ans)
    #This is printed: The sum of the products of the counts of 1s and 0s for each bit position in the prefix list

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the results. It first reads an integer n, then a list of n integers, and calculates the prefix XOR of the list. It then initializes two lists, pre and suf, to keep track of the count of 1s and 0s for each bit position in the prefix list. The function then iterates over the prefix list from right to left, updating the suf list with the correct counts. After that, it iterates over the prefix list from left to right, updating the pre list and calculating the sum of the products of the counts of 1s and 0s for each bit position. Finally, it prints the sum. The function does not return any value, and its purpose is to process and print the results of the input data.

