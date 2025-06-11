#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains three space-separated integers: n, m, and k (1 <= k <= m <= n <= 2 * 10^5). The second line contains n space-separated integers (1 <= a_i <= 10^6). The third line contains m space-separated integers (1 <= b_i <= 10^6).
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
        
    #State: `n` is an integer, `m` is an integer greater than or equal to 0, `k` is an integer, `a` is a list of integers, `b` is a list of integers, `max_val` is 1000000, `cnt_b` is a list of 1000001 integers where all elements are 0, `stdin` is empty, `i` is the last element in `b_values`, `b_values` is an empty set, and `ans` is the total number of times the number of elements in `a` that are in `b_values` and have a count greater than or equal to 0 in `cnt_b` is greater than or equal to `k` for all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: the first line contains three integers n, m, and k, and the second and third lines contain n and m space-separated integers, respectively. The function then calculates the total number of times the number of elements in the second line that are in the third line and have a count greater than or equal to 0 is greater than or equal to k, for all test cases. The function prints the total count for each test case and empties the standard input after processing all test cases.

