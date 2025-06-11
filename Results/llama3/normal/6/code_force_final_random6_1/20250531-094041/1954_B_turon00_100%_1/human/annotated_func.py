#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n) such that the list is beautiful.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        if n == 1 or ans == n:
            print(-1)
        else:
            print(ans)
        
    #State: `t` is an integer between 1 and 10^4 (inclusive), `_` is equal to `t`, `n` is an integer and `n` is greater than or equal to 0, `a` is a list of integers, `tmp` is an integer equal to the first element of `a`, `i` is equal to `n`, `cnt` is either 0 or greater than 0, `ans` is the minimum of its previous value and `cnt`. If `n` is 1 or `ans` is equal to `n`, then -1 is printed. Otherwise, `ans` is printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n) such that the list is beautiful. The function then finds the minimum length of a subsequence that contains all elements of the list and prints it. If the list contains only one element or the minimum length is equal to the length of the list, it prints -1.

