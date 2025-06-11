#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a list of n integers.
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
        
    #State: `t` is an integer greater than or equal to 0, `n` is an integer greater than or equal to 0, `a` is a list of integers, `tmp` is the first element of `a`, `i` is `n`, `cnt` is either 0 or the number of consecutive occurrences of `tmp` in `a` starting from the last element of `a`, and `ans` is the minimum of `cnt` and `n`. If `n` is 1 or `ans` is equal to `n`, then -1 is printed. Otherwise, the value of `ans`, which is the minimum of `cnt` and `n`, is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the minimum number of consecutive occurrences of the first element in a list of integers. If the list contains only one element or the minimum number of consecutive occurrences is equal to the list length, it prints -1. Otherwise, it prints the minimum number of consecutive occurrences.

