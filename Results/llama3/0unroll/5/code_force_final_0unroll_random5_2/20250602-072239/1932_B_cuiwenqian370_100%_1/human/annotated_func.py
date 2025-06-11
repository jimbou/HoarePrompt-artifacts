#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 1000), then for each test case, first an integer n (1 <= n <= 100) and then n integers a_1, a_2, a_3, ..., a_n (1 <= a_i <= 10^6).
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
        
    #State: Output State: T is an integer between 1 and 1000 inclusive, index is T + 1 + sum of all n values in the test cases, results is a list of T strings, each representing the last year value for the corresponding test case, stdin contains T test cases, each consisting of an integer n (1 <= n <= 100) and n integers a_1, a_2, a_3, ..., a_n (1 <= a_i <= 10^6).
    sys.stdout.write('\n'.join(results) + '\n')

#Overall this is what the function does:This function reads input from standard input, processes multiple test cases, and outputs the results to standard output. It accepts no parameters and returns no value. The function reads an integer T, representing the number of test cases, followed by T test cases. Each test case consists of an integer n and n integers a_1, a_2, ..., a_n. The function calculates the last year value for each test case based on the given integers and appends the result as a string to a list. Finally, it writes the list of results to standard output, one result per line, followed by a newline character.

