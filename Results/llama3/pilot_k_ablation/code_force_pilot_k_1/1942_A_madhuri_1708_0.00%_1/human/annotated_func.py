#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[j for j in range(n)])
        
    #State: stdin is empty, n and k are the last integers in the input (if it is not empty), for each line in the input, if k is greater than or equal to 2, then if n is equal to k, k repeated k times is printed, otherwise -1 is printed. If k is less than 2, a list of integers from 0 to n-1 is printed.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t (1 <= t <= 10^3) representing the number of test cases, followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3). For each test case, if k is greater than or equal to 2, it checks if n is equal to k. If true, it prints k repeated k times. If false, it prints -1. If k is less than 2, it prints a list of integers from 0 to n-1. After processing all test cases, stdin is left empty.

