#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
        
    #State: stdin contains t-1 test cases, arr is a list of n integers, prefix is a list of n+1 integers where the i-th element (1 <= i <= n) is the XOR of all integers from 1 to i in arr.
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
        
    #State: stdin contains t-1 test cases, arr is a list of n integers, prefix is a list of n+1 integers where the i-th element (1 <= i <= n) is the XOR of all integers from 1 to i in arr, pre is a list of 32 lists where each list contains [1,0], suf is a list of 32 lists each containing two zeros.
    for i in range(n, 0, -1):
        cur = prefix[i]
        
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
        
    #State: stdin contains t-1 test cases, arr is a list of n integers, prefix is a list of n+1 integers where the i-th element (1 <= i <= n) is the XOR of all integers from 1 to i in arr, pre is a list of 32 lists where each list contains [1,0], suf is a list of 32 lists where the j-th list contains [number of zeros in the j-th bit of all integers from n to 1 in arr, number of ones in the j-th bit of all integers from n to 1 in arr].
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
        
    #State: `ans` is the sum of the products of the number of zeros and ones in the k-th bit of all integers from 1 to i-1 in `arr` and the number of zeros and ones in the k-th bit of all integers from i to n in `arr`, where k is the bit length of the i-th integer in `arr` minus 1, `pre` is a list of 32 lists where the j-th list contains [number of zeros in the j-th bit of all integers from 1 to n in `arr`, number of ones in the j-th bit of all integers from 1 to n in `arr`], `suf` is a list of 32 lists where the j-th list contains [0, number of ones in the j-th bit of all integers from 1 to n in `arr`], `prefix` is a list of n+1 integers where the i-th element (1 <= i <= n) is the XOR of all integers from 1 to i in `arr`, `arr` is a list of n integers, `n` is a non-negative integer. If `n` is 0, `ans` is 0, `pre` is a list of 32 lists where each list contains [1,0], `suf` is a list of 32 lists where each list contains [1,0], `prefix` is a list of n+1 integers where the first element is 0 and the rest are the XOR of all integers from 1 to i in `arr`.
    print(ans)
    #This is printed: ans (where ans is the sum of the products of the number of zeros and ones in the k-th bit of all integers from 1 to i-1 in `arr` and the number of zeros and ones in the k-th bit of all integers from i to n in `arr`, where k is the bit length of the i-th integer in `arr` minus 1)

#Overall this is what the function does:This function reads an integer n from standard input, followed by n integers, and calculates the sum of the products of the number of zeros and ones in the k-th bit of all integers from 1 to i-1 and the number of zeros and ones in the k-th bit of all integers from i to n, where k is the bit length of the i-th integer minus 1. It then prints this sum to standard output. The function performs this calculation for each test case, where the number of test cases is specified by an integer t read from standard input before the first test case.

