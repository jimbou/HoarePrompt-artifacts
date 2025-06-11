#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
    input = sys.stdin.read
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []
    for _ in range(T):
        n = int(data[index])
        
        index += 1
        
        a = list(map(int, data[index:index + n]))
        
        index += n
        
        last_year = a[0]
        
        for i in range(1, n):
            next_year = (last_year + 1 + a[i] - 1) // a[i] * a[i]
            last_year = next_year
        
        results.append(str(last_year))
        
    #State: Output State: T is an integer between 1 and 1000, index is T + 1 + sum(n_i) where n_i is the number of integers in the i-th test case, results is a list of T strings where each string represents the last year of the i-th test case, data contains t test cases, each test case consists of an integer n followed by n integers a_1, a_2, ..., a_n, stdin is empty.
    sys.stdout.write('\n'.join(results) + '\n')

#Overall this is what the function does:This function reads input from standard input, processes it, and writes the results to standard output. It expects the input to contain an integer T (1 <= T <= 1000) followed by T test cases. Each test case consists of an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6). The function processes each test case, calculates the last year of the test case, and stores the results in a list. Finally, it writes the results to standard output, one result per line, followed by a newline character. The function does not return any value.

