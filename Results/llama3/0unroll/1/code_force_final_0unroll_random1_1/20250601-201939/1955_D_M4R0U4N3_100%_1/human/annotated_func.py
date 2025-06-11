#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, m, and k, followed by a list of n integers and a list of m integers. n, m, and k are non-negative integers such that 1 <= k <= m <= n <= 2 * 10^5. The sum of n over all test cases does not exceed 2 * 10^5. Similarly, the sum of m over all test cases does not exceed 2 * 10^5. The integers in the lists are between 1 and 10^6 (inclusive).
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
        
    #State: stdin is empty, and cnt_b is a list of 1000001 zeros.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers (n, m, k) followed by two lists of integers (a and b). It then calculates the number of sublists of length m in list a that contain at least k elements from list b. The function prints the result for each test case and resets the input state to empty.

