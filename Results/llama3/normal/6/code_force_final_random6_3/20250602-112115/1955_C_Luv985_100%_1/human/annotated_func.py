#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains two integers n and k. The second line contains n integers a_1, a_2, ..., a_n. t is a positive integer, n is a positive integer less than or equal to 2 * 10^5, k is a positive integer less than or equal to 10^15, and a_i is a positive integer less than or equal to 10^9 for all i.
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
        
    #State: T is 0, n is an integer greater than 1, k is an integer greater than or equal to 0, a is a list of n integers, stdin contains 0 test cases, l is an integer greater than or equal to 0 and less than or equal to n - 1, r is an integer greater than or equal to 0 and less than or equal to n - 1, ans is an integer greater than or equal to 0 and less than or equal to n. If l is equal to r, then ans is equal to the number of elements in a that are less than or equal to k plus the previous value of ans, and the value of ans is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines. The first line contains two integers, n and k, and the second line contains n integers. The function then processes each test case by iterating through the list of integers from both ends, subtracting the minimum of the two current integers from k and removing the integer if it becomes zero. If k becomes zero or the list is fully processed, the function counts the number of remaining integers that are less than or equal to k and prints the total count of removed and counted integers. The function repeats this process for all test cases and finally prints the results.

