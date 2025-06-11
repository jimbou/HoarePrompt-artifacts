#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two space-separated integers: the number of cows (n) and the index of the cow (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows. n is an integer between 2 and 10^5 (inclusive), k is an integer between 1 and n (inclusive), and the Cowdeforces ratings are distinct integers between 1 and 10^9 (inclusive).
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
        
    #State: The output state contains multiple test cases. Each test case contains a single integer representing the maximum number of cows that can be defeated by the cow at index k, considering the two possible scenarios where the cow at index k is either at the beginning or at its original position.

#Overall this is what the function does:This function determines the maximum number of cows that can be defeated by the cow at a given index k, considering two scenarios: when the cow at index k is at the beginning and when it is at its original position. It takes multiple test cases as input, where each test case consists of the number of cows, the index of the cow, and the Cowdeforces ratings of the cows. The function returns the maximum number of cows that can be defeated in each test case.

