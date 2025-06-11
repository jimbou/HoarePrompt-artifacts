#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        else:
            print(-1)
        
    #State: _ is t-1, stdin is empty, and for each iteration, if n equals k, a string of '1 ' repeated n times (excluding the last space) is printed, otherwise -1 is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of two integers n and k. For each case, if n equals k, it prints a string of '1 ' repeated n times (excluding the last space); otherwise, it prints -1. The function continues this process until all test cases have been read from standard input, leaving the input stream empty.

