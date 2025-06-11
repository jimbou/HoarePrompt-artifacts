#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains two space-separated integers: the number of cows (n) and the index of the cow (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows. n is an integer such that 2 <= n <= 10^5, k is an integer such that 1 <= k <= n, and the Cowdeforces ratings are integers such that 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: `n`, `k` are integers, `s` is a list of integers that is not empty with the first element and the kth element swapped back to their original positions, `ans` is the number of elements in `s` that are less than or equal to `h` (excluding the first element), `h` is the new first element of `s`, `j` is the index of the last element in `s` that is less than or equal to `h`, `stdin` contains no test cases, `i` is the last element in `s` that is less than or equal to `h`, `p` is `j` + 1, `ans1` is the number of elements in `s` that are equal to `h` (excluding the first element), `z` is 1, and the maximum value between the number of elements in `s` that are less than or equal to `h` (excluding the first element) and the number of elements in `s` that are equal to `h` (excluding the first element) is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers representing the number of cows and the index of a specific cow, and the second line contains a list of integers representing the Cowdeforces ratings of the cows. The function then swaps the first cow with the cow at the specified index, finds the number of cows with ratings less than or equal to the new first cow's rating, and finds the number of cows with ratings equal to the new first cow's rating. Finally, it prints the maximum of these two counts for each test case.

