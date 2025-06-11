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
        
    #State: T is 0, index is T * (n + 1), results is a list containing the string representation of last_year T times, _ is T-1, n is an integer greater than or equal to 1, a is a list of n integers, last_year is ((a[0] + 1 + a[n-1] - 1) // a[n-1] * a[n-1]), i is n-1
    sys.stdout.write('\n'.join(results) + '\n')

#Overall this is what the function does:This function reads input from standard input, processes it, and writes the results to standard output. It expects the input to contain an integer T (1 <= T <= 1000) followed by T test cases. Each test case consists of an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6). The function calculates the last year for each test case by iteratively rounding up the previous year to the nearest multiple of the current year's value, and appends the result as a string to a list. Finally, it writes the list of results to standard output, one result per line, followed by a newline character.

