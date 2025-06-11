#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains three integers n, m, and k. The second line contains n integers a_1, a_2, ..., a_n. The third line contains m integers b_1, b_2, ..., b_m. n, m, and k are non-negative integers such that 1 <= k <= m <= n <= 2 * 10^5. a_i and b_i are non-negative integers such that 1 <= a_i, b_i <= 10^6.
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
        
    #State: stdin is empty, cnt_b is a list of 1000001 zeros, and the console contains the output of the program for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, each containing three lines of integers. It then processes these test cases to find the number of valid subarrays of a certain size that contain at least a specified number of elements from a given set. The function prints the count of such valid subarrays for each test case and resets its internal state after processing each test case.

