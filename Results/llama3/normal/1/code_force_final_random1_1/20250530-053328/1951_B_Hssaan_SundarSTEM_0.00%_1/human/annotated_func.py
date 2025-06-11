#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two space-separated integers: n and k, where n is the number of cows and k is the index of the cow of interest. The second line contains n space-separated integers representing the Cowdeforces ratings of the cows.
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
        
    #State: `n` is an integer, `k` is an integer, `s` is a list of integers that must have at least 2 elements and the first and k-th elements swapped twice, `ans` is the number of elements in `s` that are less than or equal to `h`, `h` is the new first element of the list `s`, `j` is `len(s)-1`, `stdin` contains no test cases, `p` is `j`, `i` is the last element of `s`, `ans1` is the number of elements in `s` that are less than or equal to `h` and are equal to `h` if `s[0]` is not equal to `h`, `z` is 1 if `s[0]` is equal to `h`, otherwise `z` is 0, and the maximum value between `ans` and `ans1` is printed, which is the maximum value between the number of elements in `s` that are less than or equal to `h` and the number of elements in `s` that are less than or equal to `h` and are equal to `h` if `s[0]` is not equal to `h`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers: the number of cows (n) and the index of the cow of interest (k). The second line contains n integers representing the Cowdeforces ratings of the cows. The function then swaps the first and k-th elements of the ratings list, calculates the number of elements less than or equal to the new first element (h), and stores this count in 'ans'. It then swaps the first and k-th elements back, swaps the p-th (where p is the index of the last element less than or equal to h) and k-th elements, and calculates the number of elements less than or equal to h, considering only elements equal to h if the first element is not h. The function stores this count in 'ans1'. Finally, it prints the maximum value between 'ans' and 'ans1', which represents the maximum number of elements less than or equal to h in the two scenarios.

