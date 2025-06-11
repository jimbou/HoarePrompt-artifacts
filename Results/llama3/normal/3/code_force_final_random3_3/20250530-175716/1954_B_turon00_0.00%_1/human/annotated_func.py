#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t, then for each test case, first an integer n and then a list of n integers.
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
        
    #State: `t` is an integer greater than or equal to 0, `_` is `t`, `n` is an integer, `a` is a list of integers, `tmp` is an integer equal to the first element of `a`, `aa` is a set of unique integers from `a`, `i` is `n-1`, `cnt` is the number of consecutive occurrences of `tmp` at the end of `a`, and `ans` is the minimum between the previous minimum number of consecutive occurrences of `tmp` in `a` and the number of consecutive occurrences of `tmp` at the end of `a`, and the minimum between the previous minimum number of consecutive occurrences of `tmp` in `a` and the number of consecutive occurrences of `tmp` at the end of `a` which is `ans` is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then finds the minimum number of consecutive occurrences of the first integer in the list and prints this value. If all integers in the list are the same, it prints -1. The function processes all test cases and prints the result for each case.

