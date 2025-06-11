#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two space-separated integers: the number of cows (n) and the index of the cow (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows. The number of cows (n) is between 2 and 10^5 (inclusive), the index of the cow (k) is between 1 and n (inclusive), and the Cowdeforces ratings are between 1 and 10^9 (inclusive).
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
        
    #State: The output state contains the maximum number of cows that can be defeated by the cow at index k, for each test case. The number of cows that can be defeated is determined by swapping the cow at index k with the first cow and then with the cow at the position where the first cow's rating is exceeded, and taking the maximum of these two values. The output is in the same order as the input test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains the number of cows and the index of a specific cow, and the second line contains the Cowdeforces ratings of the cows. For each test case, it determines the maximum number of cows that can be defeated by the cow at the specified index by swapping it with the first cow and then with the cow at the position where the first cow's rating is exceeded, and prints this maximum value. The function processes all test cases and outputs the results in the same order as the input.

