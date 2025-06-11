#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (2 <= n <= 10^5). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases is between 1 and 500.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        if n == 2:
            print(min(a))
            continue
        
        max = 0
        
        for i in range(n - 2):
            temp = a[i:i + 3]
            temp.sort()
            if temp[1] > max:
                max = temp[1]
        
        print(max)
        
    #State: The output state will contain the maximum possible second maximum number for each test case. The value of `t` will be 0, and the stdin will be empty. The value of `n` and `a` will be the last test case values. The `max` variable will hold the maximum possible second maximum number for the last test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n followed by n space-separated integers. For each test case, it finds the maximum possible second maximum number that can be obtained by considering all possible subarrays of size 3. If a test case has only two integers, it simply prints the smaller of the two. The function prints the result for each test case and leaves the input stream empty after processing all test cases.

