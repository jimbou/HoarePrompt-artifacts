#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 1 <= k <= 10^15). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    """
        @Time : 2024/8/26 17:59
        @Author : Zhiliang.L
        @Email : 2410103062@mails.edu.cn
        @File : 1955-C.py
    """
    T = int(input())
    while T:
        T -= 1
        
        n, k = input().split()
        
        n = int(n)
        
        k = int(k)
        
        a = input().split()
        
        a = list(map(lambda x: int(x), a))
        
        l = 0
        
        r = n - 1
        
        ans = 0
        
        while l < r and k > 0:
            mi = min(a[l], a[r])
            if mi * 2 <= k:
                a[l] -= mi
                a[r] -= mi
                k -= mi * 2
                if a[l] == 0:
                    ans += 1
                    l += 1
                if a[r] == 0:
                    ans += 1
                    r -= 1
            else:
                t = k % 2
                if a[l] - t - k // 2 == 0:
                    ans += 1
                break
        
        if l == r:
            ans += k >= a[l]
        
        print(ans)
        
    #State: T = 0, n = 0, k = 0, a = [], l = 0, r = -1, ans = 0

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. The function then processes each test case by iterating through the integers from both ends, subtracting the minimum of the two end values from both and updating the count of processed integers (ans) until either the two ends meet or k becomes 0. If the two ends meet, it checks if the remaining value is less than or equal to k and updates the count accordingly. Finally, it prints the total count of processed integers for each test case.

