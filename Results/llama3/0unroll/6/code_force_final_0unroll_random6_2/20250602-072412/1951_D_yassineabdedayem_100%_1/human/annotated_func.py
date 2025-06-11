#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two positive integers n and k (1 <= n, k <= 10^18).
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        if n == k:
            print('YES')
            print(1)
            print(1)
        elif n + 2 > k * 2:
            print('YES')
            print(2)
            print(n - k + 1, end=' ')
            print(1)
        else:
            print('NO')
        
    #State: The output state will contain t lines, each containing either 'YES' or 'NO'. If 'YES', it will be followed by two more lines: the first line will contain either 1 or 2, and the second line will contain either a single number (1) or two numbers (n - k + 1 and 1). The value of t and the values of n and k in each line of stdin will be unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two positive integers n and k. It then determines whether it's possible to satisfy a certain condition based on the values of n and k. If the condition is satisfied, it prints 'YES' followed by a specific output format indicating the solution; otherwise, it prints 'NO'. The function processes all test cases and produces the corresponding output for each case, leaving the input values unchanged.

