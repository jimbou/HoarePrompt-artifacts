#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then t blocks of two lines each. Each block contains first an integer n (1 <= n <= 10^5), then n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: stdin contains t-1 blocks of two lines each, n is an integer, arr is a list of n integers, prefix is a list containing n+1 elements: 0 and the XOR of all elements in arr.
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: n is an integer, arr is a list of n integers, prefix is a list containing n+1 elements: 0 and the XOR of all elements in arr, pre is a 2D list containing 32 sublists, each containing [32, 0], suf is a 2D list containing 32 sublists, each containing [0, 0], stdin contains t-1 blocks of two lines each, i is equal to 32
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: Output State: `n` is an integer greater than 0, `arr` is a list of `n` integers, `prefix` is a list containing `n+1` elements: 0 and the XOR of all elements in `arr`, `pre` is a 2D list containing 32 sublists, each containing [32, 0], `suf` is a 2D list containing 32 sublists, where the jth sublist is [1, 0] if the jth bit of `cur` is 0, otherwise it is [0, 1], except for `suf[j]` which is [0, n-1] if the jth bit of `cur` is 1, otherwise it is [n, 0], `cur` is the XOR of all elements in `arr`, `i` is 0, stdin contains `t-1` blocks of two lines each, and `j` is 32.
    #
    #In natural language, the output state after the loop executes all iterations is that the loop has iterated over all elements in the `arr` list, updating the `suf` list accordingly. The `i` variable has reached its minimum value of 0, indicating that the loop has completed all iterations. The state of the other variables remains unchanged.
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
        
    #State: n is at least 1, arr is a list of n integers, prefix is a list containing n+1 elements: 0 and the XOR of all elements in arr, pre is a 2D list containing 32 sublists, where the jth sublist is [32, n] if the jth bit of cur is 1, otherwise it is [n, 0], suf is a 2D list containing 32 sublists, where the jth sublist is [1, 0] if the jth bit of cur is 1, otherwise it is [0, n], cur is the XOR of all elements in arr, i is n, j is 32, ans is the sum of pre[k][0] * suf[k][0] + pre[k][1] * suf[k][1] for k from 0 to 31, y is the ith element of arr, k is the bit length of y minus 1, c is the ith element of prefix.
    print(ans)
    #This is printed: The sum of pre[k][0] * suf[k][0] + pre[k][1] * suf[k][1] for k from 0 to 31 (where pre[k][0] is 32 if the kth bit of cur is 1, otherwise it is n, pre[k][1] is n if the kth bit of cur is 1, otherwise it is 0, suf[k][0] is 1 if the kth bit of cur is 1, otherwise it is 0, suf[k][1] is 0 if the kth bit of cur is 1, otherwise it is n, and cur is the XOR of all elements in arr)

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the sum of products of certain bit counts. It takes no arguments and returns no value. The input is expected to contain multiple blocks of two lines each, where the first line contains an integer n, and the second line contains n integers. The function calculates the XOR of all elements in each block, then updates two 2D lists (pre and suf) based on the bits of the XOR value. Finally, it calculates and prints the sum of products of certain bit counts from the pre and suf lists.

