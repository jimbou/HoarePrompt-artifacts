#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines. The first line contains two integers n and k, where n is a positive integer and k is a non-negative integer. The second line contains n positive integers.
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
        
    #State: T is 0, stdin contains 0 test cases, n is at least 2, k is 0, l is at least 0 and less than or equal to r, r is at least 1, a is a list of n non-negative integers, ans is at least 0 and at most n, mi is the minimum of a[l] and a[r], and t is equal to k % 2. If l is equal to r, ans is increased by 1 if k is greater than or equal to a[l], which is equivalent to a[r] since l is equal to r, and the value of ans is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines. The first line contains two integers, n and k, where n is a positive integer and k is a non-negative integer. The second line contains n positive integers. The function then processes each test case by iteratively reducing the values of the integers from both ends of the list, subtracting the minimum of the two end values from both ends and decrementing k by twice the minimum value, until k becomes 0 or the list is fully processed. The function counts the number of integers that can be fully reduced to 0 and prints this count for each test case.

