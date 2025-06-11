#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        else:
            print(-1)
        
    #State: No output is printed, and stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. If n equals k, it prints a string of n ones separated by spaces; otherwise, it prints -1. The function processes all test cases and leaves the standard input empty.

