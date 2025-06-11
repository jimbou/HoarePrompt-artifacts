#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains three integers n, m, and k (1 <= k <= m <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6). The third line contains m integers b_1, b_2, ..., b_m (1 <= b_i <= 10^6).
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
        
    #State: Output State: `max_val` is 1000000, `cnt_b` is a list of 1000001 zeros, `n` is a positive integer, `m` is a positive integer, `k` is a positive integer, `a` is a list of positive integers, `b` is a list of positive integers, stdin contains no input, `i` is the last value in `b_values`, `b_values` is an empty set, `curr` is the number of times `a[i]` is in `b_values` minus `n-m-1` if `cnt_b[a[i]]` is greater than `n-m-1` and `a[i]` is not in `b_values`, otherwise `curr` is the number of times `a[i]` is in `b_values` minus `n-m`. If `curr` is greater than or equal to `k`, then `ans` is `n-m+1`. Otherwise, `ans` is `n-m`. If `a[i + m]` is in `b_values`, then the value at index `a[i + m]` in `cnt_b` is one less than its previous value. If `cnt_b[a[i + m]]` is greater than or equal to 0, `curr` is incremented by 1. If `a[i]` is not in `b_values`, then `cnt_b` remains unchanged. If `a[i + m]` is in `b_values`, the value at index `a[i + m]` in `cnt_b` is one less than its previous value. If `cnt_b[a[i + m]]` is less than 0, then `cnt_b` remains unchanged, and ans is printed, where ans is either `n-m+1` if `curr` is greater than or equal to `k`, otherwise `ans` is `n-m`.
    #
    #In natural language, the output state after the loop executes all the iterations is that the set `b_values` is empty, indicating that the loop has iterated over all elements in the set. The variable `i` is the last element in the set `b_values`. The counts of elements in `cnt_b` are updated according to the loop body, and the total number of times `curr` is greater than or equal to `k` during the loop execution is stored in `ans`. The other variables remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines. The first line contains three integers n, m, and k. The second line contains n integers, and the third line contains m integers. The function then calculates the number of times a subarray of length m in the first array contains at least k elements from the second array. The function prints the result for each test case.

