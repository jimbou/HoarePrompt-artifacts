#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two space-separated integers: the number of cows (n) and the index of the cow of interest (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows. n is an integer such that 2 <= n <= 10^5, k is an integer such that 1 <= k <= n, and the Cowdeforces ratings are integers such that 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: All variables in the loop head and body have reached their final values after the loop has finished executing.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers: the number of cows (n) and the index of the cow of interest (k). The second line contains n integers representing the Cowdeforces ratings of the cows. For each test case, the function swaps the Cowdeforces rating of the cow of interest with the first cow, then calculates the number of cows that have a lower or equal rating than the cow of interest. It then swaps the Cowdeforces rating of the cow of interest with the cow at the position where the previous swap was made, and calculates the number of cows that have a lower or equal rating than the cow of interest again. Finally, the function prints the maximum of these two calculations. The function repeats this process for all test cases.

