#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The integer is a positive integer and represents the length of the list. The list contains positive integers. The sum of the lengths of all lists over all test cases does not exceed 3 * 10^5.
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
        
    #State: `t` is 0, `_` is `t`, `n` is a positive integer, `a` is a list of positive integers, `tmp` is a positive integer, `aa` is a set of positive integers, `cnt` is either 0 or a positive integer, `ans` is the minimum of the original value of `ans` and `cnt`, `i` is -1, and stdin contains no test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n followed by a list of n positive integers. It then finds the minimum length of a subsequence of consecutive equal elements in the list. If all elements in the list are equal, it prints -1. Otherwise, it prints the minimum length of the subsequence. The function processes all test cases and prints the results for each case.

