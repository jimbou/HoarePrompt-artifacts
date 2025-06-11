#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[(j + 1) for j in range(n)])
        
    #State: The output state will contain t lines, each containing a sequence of integers. If k is 1, the sequence will be a list of consecutive integers from 1 to n. If k is greater than 1, the sequence will either be a list of k repeated k times (if n equals k), or the string '-1' (if n is greater than k).

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers, n and k. For each test case, if k is 1, it prints a sequence of consecutive integers from 1 to n. If k is greater than 1, it either prints a sequence of k repeated k times (if n equals k) or prints '-1' (if n is greater than k). The function outputs the results for all test cases, with each result on a separate line.

