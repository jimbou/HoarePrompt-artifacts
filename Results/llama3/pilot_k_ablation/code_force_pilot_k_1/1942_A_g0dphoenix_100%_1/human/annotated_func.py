#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        elif k == 1:
            print(' '.join([str(x + 1) for x in range(n)]))
        else:
            print(-1)
        
    #State: stdin is empty, _ is equal to the initial value of t, n and k are the last values read from stdin (if t is greater than 0) or are undefined (if t is 0).

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it prints a specific sequence of numbers based on the values of n and k. If n equals k, it prints a sequence of 1s repeated n times. If k equals 1, it prints a sequence of numbers from 1 to n. If neither condition is met, it prints -1. The function continues this process until all test cases have been read from standard input, leaving the input stream empty.

