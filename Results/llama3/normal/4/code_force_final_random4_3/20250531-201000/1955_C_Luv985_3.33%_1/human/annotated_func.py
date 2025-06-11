#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines. The first line contains two integers n and k, where n is the number of ships and k is the number of times the Kraken will attack the ships. The second line contains n integers a_1, a_2, ..., a_n, where a_i is the durability of the i-th ship.
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
        
    #State: T is 0, n is a positive integer, k is 0, a is a list of n integers, l is a non-negative integer less than n, r is a non-negative integer less than n, ans is a non-negative integer less than n. If the current values of l and r are equal, then ans is equal to its original value plus 0, and ans is printed.

#Overall this is what the function does:This function simulates a scenario where a Kraken attacks a fleet of ships. It takes as input the number of test cases, and for each test case, it reads the number of ships and the number of Kraken attacks. It then reads the durability of each ship. The function simulates the Kraken's attacks, starting from both ends of the fleet, and keeps track of the number of ships sunk. If a ship's durability is reduced to zero, it is considered sunk. The function continues the simulation until the Kraken's attacks are exhausted or all ships are sunk. Finally, it prints the total number of ships sunk.

