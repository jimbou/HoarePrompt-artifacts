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
        
    #State: The loop has finished executing, and the file object `open(0)` is exhausted. The values of `n` and `k` are no longer accessible. The output is a series of lines, each containing either a list of integers or -1, as determined by the conditions in the loop body.

#Overall this is what the function does:This function reads input from standard input, where the first line contains an integer t, representing the number of test cases, followed by t lines, each containing two integers n and k. For each test case, if k is greater than or equal to 2, it prints a list of k integers if n equals k, otherwise it prints -1. If k is less than 2, it prints a list of integers from 1 to n. The function continues this process until all test cases have been processed, exhausting the input file object.

