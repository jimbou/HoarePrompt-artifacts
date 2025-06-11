#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: t is 0, n is an integer, a is a list of integers, tmp is an integer, stdin is empty, i is n, cnt is 0, ans is the minimum of its original value and the number of consecutive occurrences of tmp in a, and ans has been updated to be the minimum of its original value and cnt which is 0. If n is 1 or n is equal to ans, -1 is printed. Otherwise, ans is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then finds the minimum number of consecutive occurrences of the first integer in the list. If the list contains only one element or the minimum number of consecutive occurrences is equal to the length of the list, it prints -1. Otherwise, it prints the minimum number of consecutive occurrences.

