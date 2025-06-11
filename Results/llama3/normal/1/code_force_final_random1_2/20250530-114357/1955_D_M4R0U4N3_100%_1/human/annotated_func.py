#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains three integers n, m, and k (1 <= k <= m <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6). The third line contains m integers b_1, b_2, ..., b_m (1 <= b_i <= 10^6).
    max_val = 1000000
    cnt_b = [0] * (max_val + 1)
    for _ in range(int(input())):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        for i in range(m):
            cnt_b[b[i]] += 1
        
        b_values = set(b)
        
        ans = 0
        
        curr = 0
        
        for i in range(m):
            if a[i] in b_values:
                cnt_b[a[i]] -= 1
                if cnt_b[a[i]] >= 0:
                    curr += 1
        
        if curr >= k:
            ans += 1
        
        for i in range(n - m):
            if a[i] in b_values:
                cnt_b[a[i]] += 1
                if cnt_b[a[i]] > 0:
                    curr -= 1
            if a[i + m] in b_values:
                cnt_b[a[i + m]] -= 1
                if cnt_b[a[i + m]] >= 0:
                    curr += 1
            if curr >= k:
                ans += 1
        
        print(ans)
        
        for i in b_values:
            cnt_b[i] = 0
        
    #State: `max_val` is 1000000, `cnt_b` is a list of 1000001 zeros, `n`, `m`, `k`, `a`, `b`, `_`, `i`, `b_values`, `curr`, `ans` are undefined, stdin is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, each consisting of three lines. It calculates the number of subarrays of a given size that contain at least a specified number of elements from a second array, and prints this count for each test case. The function then resets its internal state, leaving the input stream empty and all variables undefined except for a list `cnt_b` which is reset to zeros.

