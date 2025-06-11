#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, m, and k (1 <= k <= m <= n <= 2 * 10^5), followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6), and a list of m integers b_1, b_2, ..., b_m (1 <= b_i <= 10^6). The sum of n over all test cases does not exceed 2 * 10^5, and the sum of m over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop will output the number of subarrays of length m that contain at least k elements from the list b, for each test case. The output state will be a list of integers, where each integer represents the number of such subarrays for a particular test case. The state of the other variables, such as cnt_b, will be reset to their initial values after each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers (n, m, k) and two lists of integers (a and b). It then calculates and prints the number of subarrays of length m in list a that contain at least k elements from list b. The function processes each test case independently, resetting its internal state after each case, and outputs the result for each test case as an integer.

