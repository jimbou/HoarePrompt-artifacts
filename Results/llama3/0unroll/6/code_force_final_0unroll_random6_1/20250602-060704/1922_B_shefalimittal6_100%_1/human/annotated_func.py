#State of the program right berfore the function call: stdin contains t+2*t*n integers, where t is a positive integer, n is a positive integer such that 1 <= n <= 3*10^5, and the sum of n over all test cases does not exceed 3*10^5. The first integer is t. Then for each test case, the first integer is n, and the following n integers are a_1, a_2, ..., a_n, where 0 <= a_i <= n.
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
        
    #State: Output State: t is a positive integer, idx is t+1, results is a list of t strings, data contains t+2*t*n-1 integers, stdin is empty
    print('\n'.join(results))
    #This is printed: a string containing all elements of the results list, separated by newline characters

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the results. It expects the input to contain a positive integer t, followed by t test cases. Each test case consists of a positive integer n, followed by n integers between 0 and n. The function calculates the number of pairs and triples of equal integers in each test case and prints the results as a string, with each result separated by a newline character. The function does not modify the input data and does not have any side effects beyond printing the results.

