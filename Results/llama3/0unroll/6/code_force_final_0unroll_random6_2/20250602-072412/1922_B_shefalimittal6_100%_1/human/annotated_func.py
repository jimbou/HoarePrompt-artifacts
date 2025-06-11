#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines: the first line contains one integer n (1 <= n <= 3 * 10^5), and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= n). The sum of n over all test cases does not exceed 3 * 10^5.
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        v = [0] * (n + 1)
        
        for _ in range(n):
            x = int(data[idx])
            idx += 1
            v[x] += 1
        
        cnt = 0
        
        ans = 0
        
        for i in range(n + 1):
            if v[i] >= 2:
                ans += cnt * v[i] * (v[i] - 1) // 2
            if v[i] >= 3:
                ans += v[i] * (v[i] - 1) * (v[i] - 2) // 6
            cnt += v[i]
        
        results.append(str(ans))
        
    #State: Output State: idx is t times the number of integers in a test case plus 1, results is a list of strings representing the number of ways to choose three integers from the input data for each test case.
    print('\n'.join(results))
    #This is printed: the number of ways to choose three integers from the input data for each test case (where the number of ways is represented as a string in the results list)

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It calculates the number of ways to choose three integers from each test case and returns the results as a list of strings, one for each test case. The function does not modify the input data and only uses it to compute the desired output.

