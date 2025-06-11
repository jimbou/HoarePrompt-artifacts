#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
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
        
    #State: Output State: T is an integer between 1 and 1000, index is T + 1, results is a list of T strings, each string representing the last year of a test case, data contains T test cases, each test case contains an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6), stdin is empty.
    sys.stdout.write('\n'.join(results) + '\n')

#Overall this is what the function does:This function reads input from standard input, processes it, and writes the results to standard output. It accepts no parameters and returns no value. The input is expected to contain an integer T (1 <= T <= 1000) followed by T test cases. Each test case contains an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6). The function processes each test case, calculates the last year of a sequence based on the given integers, and stores the results in a list. Finally, it writes the results to standard output, one result per line, followed by a newline character. The function modifies the state of the standard input and output streams, but does not modify any external state or variables.

