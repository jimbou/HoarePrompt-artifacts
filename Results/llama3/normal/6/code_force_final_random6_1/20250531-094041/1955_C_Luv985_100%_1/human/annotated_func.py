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
                if a[l] - t - k // 2 == 0:
                    ans += 1
                break
        
        if l == r:
            ans += k >= a[l]
        
        print(ans)
        
    #State: T is 0, stdin is empty, n is an integer, k is an integer, a is a list of n integers, l is an integer between 0 and n-1 (inclusive), r is an integer between 0 and n-1 (inclusive), ans is an integer between 0 and n (inclusive), mi is the minimum of a[l] and a[r], and the value of ans which is the number of times k is greater than or equal to the minimum of a[l] and a[r] when l is equal to r is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers (n and k) and a list of n integers (a_1 to a_n). It then calculates the number of times k is greater than or equal to the minimum of a[l] and a[r] when l is equal to r, and prints this value for each test case. The function continues to read and process test cases until the input is exhausted.

