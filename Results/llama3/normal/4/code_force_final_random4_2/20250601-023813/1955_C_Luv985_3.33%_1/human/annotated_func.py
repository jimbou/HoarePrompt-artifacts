#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 1 <= k <= 10^15). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
                if mi - t - k // 2 == 0:
                    ans += 1
                break
        
        if l == r:
            ans += k >= a[l]
        
        print(ans)
        
    #State: T is 0, n is an integer greater than 1 and less than or equal to 2 * 10^5 (inclusive), k is an integer greater than or equal to 0, l is less than or equal to r, mi is the minimum value between a[l] and a[r], and the values of a[l], a[r], t are unchanged. If l is equal to r, then if mi * 2 is less than or equal to k, ans is incremented by 1 and r is decremented by 1 if a[r] is equal to 0. If mi * 2 is greater than k, ans is incremented by 1 if mi - t - k // 2 equals 0, otherwise ans remains unchanged and we break out of the most internal loop or if statement. Additionally, ans is incremented by 1 if k is greater than or equal to a[l]. If l is not equal to r, the values of ans, l, and r remain unchanged. The value of ans is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k, followed by n integers a_1 to a_n. It then calculates the maximum number of pairs of integers from the list a_1 to a_n that can be reduced to zero by subtracting the minimum of the pair from both elements, given the constraint that the total subtraction does not exceed k. The function prints the calculated maximum number of pairs for each test case.

