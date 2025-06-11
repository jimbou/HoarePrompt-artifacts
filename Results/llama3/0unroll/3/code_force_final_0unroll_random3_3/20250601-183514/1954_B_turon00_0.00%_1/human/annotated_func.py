#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4) representing the number of test cases. Each test case consists of two lines. The first line of each test case contains an integer n (1 <= n <= 3 * 10^5). The second line of each test case contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n) representing a beautiful array. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: Output State: The output state after the loop executes all the iterations is that the variable `t` remains unchanged, still being an integer between 1 and 10^4. The variable `n` has been updated to the last value read from the input, which is an integer between 1 and 3 * 10^5. The variable `a` has been updated to the last list of integers read from the input, where each integer is between 1 and `n`. The variable `tmp` has been updated to the first element of the last list `a`. The variable `aa` has been updated to a set containing all unique elements from the last list `a`. The variable `cnt` has been updated to the count of consecutive occurrences of the first element `tmp` in the last list `a`. The variable `ans` has been updated to the minimum count of consecutive occurrences of any element in the last list `a`. The output of the loop is the minimum count of consecutive occurrences of any element in each list `a` for all iterations.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It calculates and prints the minimum count of consecutive occurrences of any element in each list. If all elements in the list are the same, it prints -1. The function processes all test cases and outputs the minimum count for each case.

