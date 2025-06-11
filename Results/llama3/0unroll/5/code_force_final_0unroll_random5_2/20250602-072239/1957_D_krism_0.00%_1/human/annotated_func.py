#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    print('-----------------')
    #This is printed: -----------------
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: stdin contains t-1 test cases, n is an integer between 1 and 10^5, arr is a list of n integers between 1 and 10^9, prefix is a list of n+1 integers where each element is the XOR of all elements in arr up to that index.
    print(arr, prefix)
    #This is printed: [list of n integers between 1 and 10^9], [list of n+1 integers where each element is the XOR of all elements in arr up to that index]
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: Output State: The value of pre[i][0] is incremented by 1 for each i in the range 32.
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: Output State: The value of suf[j][0] is incremented by the number of times the jth bit is 0 in the binary representation of prefix[i] for all i in the range n to 1, and the value of suf[j][1] is incremented by the number of times the jth bit is 1 in the binary representation of prefix[i] for all i in the range n to 1.
    print(pre)
    #This is printed: The prefix array where prefix[i] is the number of 1's in the binary representation of all numbers from 1 to i
    print(suf)
    #This is printed: A 2D array where each sub-array contains the count of 0s and 1s in the binary representation of prefix[i] for all i in the range n to 1
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
        
    #State: Output State: The value of suf[j][0] is incremented by the number of times the jth bit is 0 in the binary representation of prefix[i] for all i in the range 1 to n, and the value of suf[j][1] is incremented by the number of times the jth bit is 1 in the binary representation of prefix[i] for all i in the range 1 to n, and the value of pre is printed, and suf is printed, and ans is the sum of the products of the number of times the jth bit is 0 in the binary representation of prefix[i] and the number of times the jth bit is 0 in the binary representation of prefix[i] for all i in the range 1 to n, and the number of times the jth bit is 1 in the binary representation of prefix[i] and the number of times the jth bit is 1 in the binary representation of prefix[i] for all i in the range 1 to n.
    print(ans)
    #This is printed: The sum of the products of the number of times the jth bit is 0 in the binary representation of prefix[i] and the number of times the jth bit is 0 in the binary representation of prefix[i] for all i in the range 1 to n, and the number of times the jth bit is 1 in the binary representation of prefix[i] and the number of times the jth bit is 1 in the binary representation of prefix[i] for all i in the range 1 to n.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result to stdout. It takes an integer t (1 <= t <= 10^4) followed by t test cases, where each test case contains an integer n (1 <= n <= 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The function calculates the sum of the products of the number of times the jth bit is 0 in the binary representation of prefix[i] and the number of times the jth bit is 0 in the binary representation of prefix[i] for all i in the range 1 to n, and the number of times the jth bit is 1 in the binary representation of prefix[i] and the number of times the jth bit is 1 in the binary representation of prefix[i] for all i in the range 1 to n. The result is printed to stdout.

