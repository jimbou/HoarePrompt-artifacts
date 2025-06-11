#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer represents the minimum length of a subarray that contains all elements of the input array. If the input array contains only one element or if all elements are the same, the output is -1. Otherwise, the output is the minimum length of a subarray that contains all elements. The output is printed for each test case.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts a series of test cases, each containing an integer n followed by n integers. The function calculates the minimum length of a subarray that contains all elements of the input array. If the input array contains only one element or if all elements are the same, the function prints -1. Otherwise, it prints the minimum length of a subarray that contains all elements. The function processes multiple test cases and prints the result for each case.

