#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 3 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n) that form a beautiful array.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        aa = set(a)
        
        if len(aa) == 1:
            print(-1)
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        print(ans)
        
    #State: `t` is an integer between 1 and 10^4 (inclusive) and equals 0, `_` is `t`, stdin contains 0 test cases, `n` is an integer between 1 and 3 * 10^5 (inclusive), `a` is a list of `n` integers, `tmp` is an integer which is the first element of `a`, `aa` is a set of unique integers from `a`, `i` is `n`, `ans` is the minimum of the original `ans` and `cnt`, `cnt` is 0, and the minimum of the original `ans` and `cnt` which is 0 is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of integers. It then analyzes each list to find the minimum length of a subsequence that contains the same number repeatedly. If all numbers in the list are the same, it outputs -1. Otherwise, it outputs the minimum length of the subsequence. The function processes all test cases and prints the results for each case.

