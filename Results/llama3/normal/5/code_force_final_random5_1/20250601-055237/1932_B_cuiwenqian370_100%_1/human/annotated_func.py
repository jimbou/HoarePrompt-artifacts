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
        
    #State: T is 0, index is T + n + 1, results is a list containing T strings which are the values of last_year, stdin contains 0 test cases, _ is T-1, n is an integer, a is a list of n integers, last_year is ((last_year + 1 + a[n-1] - 1) // a[n-1] * a[n-1]), i is n-1
    sys.stdout.write('\n'.join(results) + '\n')

#Overall this is what the function does:Reads input from standard input, processes multiple test cases, and outputs the results. For each test case, it calculates the final value of 'last_year' by iteratively updating it based on the given integers, and appends this value as a string to the 'results' list. Finally, it writes all the results to standard output, separated by newline characters.

