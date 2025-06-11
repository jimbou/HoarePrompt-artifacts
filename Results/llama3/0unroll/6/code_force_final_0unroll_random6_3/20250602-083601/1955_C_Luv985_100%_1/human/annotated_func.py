#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first two integers n and k, and then a list of n integers. n and k are positive integers, k is less than or equal to 10^15, n is less than or equal to 2 * 10^5, and the sum of n for all test cases does not exceed 2 * 10^5. The integers in the list are positive and less than or equal to 10^9.
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
        
    #State: The final output state is the total number of integers that can be completely removed from the list by subtracting the minimum of the first and last elements from both ends, considering the constraint of k.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers (n and k) and a list of n integers. It then calculates the maximum number of integers that can be completely removed from the list by iteratively subtracting the minimum of the first and last elements from both ends, considering the constraint of k. The function prints the total number of removable integers for each test case.

