#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        else:
            print(-1)
        
    #State: The output state is a series of lines, each containing either a sequence of '1's separated by spaces or '-1'. The number of lines is equal to the value of t in the initial state. If n equals k in a line, the output is a sequence of '1's repeated n times. Otherwise, the output is '-1'.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, if n equals k, it prints a sequence of '1's repeated n times, separated by spaces. Otherwise, it prints '-1'. The function processes all test cases and outputs the results accordingly.

