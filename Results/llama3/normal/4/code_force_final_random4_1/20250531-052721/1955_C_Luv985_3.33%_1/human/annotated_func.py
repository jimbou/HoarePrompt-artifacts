#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 1 <= k <= 10^15). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: T is 0, n is an integer, k is 0, a is a list of integers, l is n, r is -1, ans is an integer. If l is equal to r, ans is updated to ans + (0 >= a[n]), and the value of ans is being printed

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the number of pairs of integers that can be made equal by subtracting a certain value from both integers in each pair, given a list of integers and a target value. The function iterates through the list, comparing pairs of integers from the start and end of the list, and updates the count of pairs that can be made equal based on the comparison and the remaining target value. If there is only one integer left in the list, the function checks if the target value is greater than or equal to the remaining integer and updates the count accordingly. The function then prints the total count of pairs that can be made equal.

