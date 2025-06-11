#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three integers n, m and k (1 <= m, k <= n <= 50).
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) <= k:
            print('NO')
        else:
            print('Yes')
        
    #State: The output state will contain 't' number of lines, each containing either 'NO' or 'YES'. The value of 't' remains unchanged, stdin will be empty as all lines have been read, and the values of 'n', 'm', and 'k' will be the values from the last line of stdin.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers n, m, and k. It then determines whether a certain condition is met (n > k and n - math.ceil(n / m) > k) and prints 'YES' if the condition is true, and 'NO' otherwise. The function processes all test cases and prints the corresponding results, one per line, until all input has been read.

