#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (2 <= n <= 10^5, 1 <= k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
        p = j
        
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
        
    #State: The loop executes until there are no more test cases in stdin. The values of `n`, `k`, `s`, `ans`, `h`, `j`, `i`, `p`, `ans1`, and `z` are updated according to the loop body. The maximum value between `ans` and `ans1` is printed for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains n integers. For each test case, the function swaps the first and k-th elements of the array, then calculates the maximum number of elements that are less than or equal to the new first element. It also calculates the maximum number of elements that are less than or equal to the k-th element when it is moved to the position of the first element that is greater than it. The function then prints the maximum of these two values for each test case.

