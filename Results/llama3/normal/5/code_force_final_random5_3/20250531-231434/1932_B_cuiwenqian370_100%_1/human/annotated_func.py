#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 1000), then for each test case, first an integer n (1 <= n <= 100), then n integers a_1, a_2, a_3, ..., a_n (1 <= a_i <= 10^6).
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
        
    #State: T is an integer between 1 and 1000, index is 1 + n + 1 + n + ... + n (n times), results is a list containing the string representation of last_year, last_year is an integer between 1 and 10^6 and is equal to ((last_year + 1 + a[i] - 1) // a[i] * a[i]), i is n-1, next_year is an integer between 1 and 10^6 and is equal to ((last_year + 1 + a[i] - 1) // a[i] * a[i]), stdin contains multiple inputs: for each test case, first an integer n (1 <= n <= 100), then n integers a_1, a_2, a_3, ..., a_n (1 <= a_i <= 10^6).
    sys.stdout.write('\n'.join(results) + '\n')

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates the last year after a series of increments, where each increment is the smallest multiple of the current year's increment that is greater than or equal to the previous year's last year plus one. The function returns a list of the last years for each test case, with each result as a string, and writes the results to standard output, one per line.

