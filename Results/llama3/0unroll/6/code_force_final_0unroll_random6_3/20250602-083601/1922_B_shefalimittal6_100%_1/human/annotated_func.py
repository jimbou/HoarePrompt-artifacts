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
        
    #State: idx is t * (n + 1) + 1, results is a list of strings representing the results of each test case.
    print('\n'.join(results))
    #This is printed: the results of each test case (where results is the list of strings representing the results of each test case)

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It calculates the number of ways to choose three distinct numbers from the given integers, with the constraint that at least two of the chosen numbers must be equal. The function returns a list of strings, where each string represents the result of each test case. The results are then printed to the console, one result per line.

