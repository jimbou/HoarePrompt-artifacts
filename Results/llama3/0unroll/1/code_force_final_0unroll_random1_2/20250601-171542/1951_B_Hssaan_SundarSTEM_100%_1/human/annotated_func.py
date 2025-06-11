#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains two integers n and k (2 <= n <= 10^5, 1 <= k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). It is guaranteed that a_i 's are pairwise different.
    for _ in range(int(input())):
        n, k = list(map(int, input().split()))
        
        s = list(map(int, input().split()))
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans = 0
        
        h = s[0]
        
        j = -1
        
        for i in s[1:]:
            j += 1
            if h < i:
                break
            else:
                ans += 1
        
        p = j + 1
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans1 = 0
        
        s[p], s[k - 1] = s[k - 1], s[p]
        
        z = 0
        
        for i in s:
            if i == h:
                if s[0] != h:
                    ans1 += 1
                z = 1
            elif i > h:
                break
            elif z == 1:
                ans1 += 1
        
        print(max(ans, ans1))
        
    #State: The output state will be the maximum number of elements that can be removed from the list `s` such that the remaining elements are in non-decreasing order, for each test case. The output will be a list of integers, where each integer represents the maximum number of elements that can be removed for the corresponding test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines of input. The first line contains two integers n and k, and the second line contains n distinct integers. The function swaps the first and k-th elements, then calculates the maximum number of elements that can be removed to make the remaining elements non-decreasing. It also considers an alternative scenario where the k-th element is moved to a different position. The function prints the maximum number of removable elements for each test case.

