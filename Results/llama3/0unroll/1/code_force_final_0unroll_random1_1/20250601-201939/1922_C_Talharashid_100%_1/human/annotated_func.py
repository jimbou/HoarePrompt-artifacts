#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer n (2 <= n <= 10^5), then n space-separated integers a_1, a_2, ..., a_n (0 <= a_1 < a_2 < ... < a_n <= 10^9), then an integer m (1 <= m <= 10^5), and finally m lines each containing two space-separated integers x_i and y_i (1 <= x_i, y_i <= n; x_i != y_i).
    for i in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        d1 = defaultdict(int)
        
        d2 = defaultdict(int)
        
        d1[2] = 1
        
        for i in range(1, n - 1):
            if l[i + 1] - l[i] < l[i] - l[i - 1]:
                d1[i + 2] = 1 + d1[i + 1]
            else:
                d1[i + 2] = l[i + 1] - l[i] + d1[i + 1]
        
        d2[n - 1] = 1
        
        for i in range(n - 2, 0, -1):
            if l[i] - l[i - 1] < l[i + 1] - l[i]:
                d2[i] = 1 + d2[i + 1]
            else:
                d2[i] = l[i] - l[i - 1] + d2[i + 1]
        
        m = int(input())
        
        for j in range(m):
            x, y = map(int, input().split())
            if y > x:
                print(d1[y] - d1[x])
            else:
                print(d2[y] - d2[x])
        
    #State: The output state after the loop executes all the iterations is a series of print statements, each containing the difference in the values of the dictionaries d1 and d2 at the indices y and x, respectively, for each query (x, y). The values of the other variables in the precondition remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n, followed by n space-separated integers, then an integer m, and finally m lines of two space-separated integers. It calculates and prints the differences in values between two dictionaries, d1 and d2, at specific indices for each query (x, y), where x and y are the two integers in each query. The function processes all test cases and queries, printing the results for each query.

