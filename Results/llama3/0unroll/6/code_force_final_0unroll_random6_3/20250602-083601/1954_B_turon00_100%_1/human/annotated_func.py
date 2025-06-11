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
        
    #State: The output state is a list of integers, where each integer represents the minimum number of consecutive occurrences of the first element in the corresponding test case. If the first element occurs only once or if all elements in the test case are the same, the output is -1. The list has a length of `t`, where `t` is the number of test cases.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints output to standard output. It accepts no parameters and returns no value. The function reads an integer t, representing the number of test cases, followed by t test cases. Each test case consists of an integer n, representing the number of elements, followed by n integers. The function processes each test case, finding the minimum number of consecutive occurrences of the first element. If the first element occurs only once or if all elements are the same, the function prints -1. Otherwise, it prints the minimum number of consecutive occurrences. The function repeats this process for all test cases, printing the result for each case.

