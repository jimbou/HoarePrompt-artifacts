#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains two space-separated integers: the number of cows (n) and the index of the cow of interest (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows.
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
        
    #State: The output state will contain the maximum number of cows that can be defeated by the cow of interest in each test case, considering the two possible scenarios: when the cow of interest is at the beginning of the list and when it is at its original position. The output will be a list of integers, each representing the maximum number of cows that can be defeated in each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines of input. The first line contains two integers: the number of cows and the index of the cow of interest. The second line contains the Cowdeforces ratings of the cows. The function then calculates the maximum number of cows that can be defeated by the cow of interest in two scenarios: when the cow of interest is at the beginning of the list and when it is at its original position. It prints the maximum number of cows that can be defeated in each test case, considering both scenarios.

