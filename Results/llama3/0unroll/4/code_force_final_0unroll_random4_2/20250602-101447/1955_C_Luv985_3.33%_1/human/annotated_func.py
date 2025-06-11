#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 2*10^5, 1 <= k <= 10^15). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases is between 1 and 10^4.
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
        
    #State: T = 0, ans = number of pairs of elements in a that can be made equal to zero by subtracting the same number from both elements, without exceeding k.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. It then calculates and prints the maximum number of pairs of elements in the array that can be made equal to zero by subtracting the same number from both elements, without exceeding k. The function processes all test cases and prints the result for each case.

