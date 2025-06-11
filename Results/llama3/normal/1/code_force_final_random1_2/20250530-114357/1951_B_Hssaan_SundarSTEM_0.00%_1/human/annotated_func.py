#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (2 <= n <= 10^5, 1 <= k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). It is guaranteed that a_i 's are pairwise different.
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
        
    #State: `n`, `k`, `s`, `h`, `ans`, `j`, `_`, `i`, `p`, `ans1`, `z`, and `stdin` are integers or lists of integers. `s` has at least `k` elements and the first and (`k-1`)th elements swapped a number of times equal to the number of test cases in `stdin`. `ans` is the number of elements in `s[1:]` that are less than or equal to the `k`th element of the original list `s`. `h` is the `k`th element of the original list `s`. `j` is `k` minus the number of test cases in `stdin` minus 1. `_` is the number of test cases in `stdin` minus 1. `i` is the last element of `s`. `p` is `k` minus the number of test cases in `stdin` minus 1. `ans1` is the number of elements in `s[1:]` that are equal to `h` and appear after the first occurrence of `h` in `s`. `z` is 1. `stdin` contains 0 inputs. The maximum value between `ans` and `ans1` is being printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains n distinct integers. For each test case, it swaps the first and kth elements of the list, then calculates the number of elements in the list (excluding the first element) that are less than or equal to the kth element. It also calculates the number of elements in the list (excluding the first element) that are equal to the kth element and appear after the first occurrence of the kth element. The function then prints the maximum of these two counts for each test case.

