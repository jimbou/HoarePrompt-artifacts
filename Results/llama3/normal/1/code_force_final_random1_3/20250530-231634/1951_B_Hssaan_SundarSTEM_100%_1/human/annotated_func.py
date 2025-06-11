#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two space-separated integers: n and k, where n is the number of cows (2 <= n <= 10^5) and k is the index of the cow (1 <= k <= n). The second line contains n space-separated integers: the Cowdeforces ratings of the cows (1 <= a_i <= 10^9), which are all distinct.
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
        
    #State: The loop has finished executing, and the maximum value between `ans` and `ans1` has been printed for each test case. The values of `n`, `k`, `s`, `h`, `j`, `p`, `ans`, `ans1`, `z`, and `i` have been reset for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers (n and k) and the second line contains n distinct integers representing cow strengths. For each test case, it swaps the first and k-th cow strengths, then calculates the maximum number of cows that can be defeated by the k-th cow when placed at the beginning and when placed at a position that maximizes the number of cows it can defeat. It prints the maximum of these two values for each test case.

