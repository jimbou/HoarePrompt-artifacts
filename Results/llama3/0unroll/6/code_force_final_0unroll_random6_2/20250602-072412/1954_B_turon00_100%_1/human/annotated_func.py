#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (1 <= n <= 3 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer represents the minimum count of consecutive occurrences of the first element in the corresponding test case. If the first element occurs only once or is the only element in the test case, the output is -1. The output list has the same number of elements as the number of test cases in the input.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It then calculates the minimum count of consecutive occurrences of the first element in each test case. If the first element occurs only once or is the only element in the test case, it outputs -1. Otherwise, it outputs the minimum count. The function processes all test cases and prints the results in the same order as the input.

