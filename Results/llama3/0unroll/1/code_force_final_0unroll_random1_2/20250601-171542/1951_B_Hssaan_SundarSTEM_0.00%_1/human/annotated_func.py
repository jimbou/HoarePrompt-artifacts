#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains two integers: the number of cows (n) and the index of the cow (k). The second line contains n integers representing the Cowdeforces ratings of the cows.
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
        
    #State: The output state will contain the maximum number of cows that can be defeated by the cow at index k, considering the two possible scenarios: swapping the cow at index 0 with the cow at index k, and swapping the cow at index p with the cow at index k. The output will be the maximum of these two scenarios for each test case.

#Overall this is what the function does:This function determines the maximum number of cows that can be defeated by the cow at a given index k in a list of cows with different strength ratings. It considers two scenarios: swapping the strongest cow with the cow at index k, and swapping the cow at a specific position p with the cow at index k. The function then prints the maximum number of cows that can be defeated in each scenario for multiple test cases.

