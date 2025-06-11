#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 50) and then t integers (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            print('YES')
            pattern = []
            for i in range(n // 2):
                pattern.append('AB'[i % 2])
                pattern.append('AB'[i % 2 ^ 1])
            print(''.join(pattern))
        
    #State: `t` is an integer greater than or equal to 0, `_` is `t`, `n` is an integer between 1 and 50 inclusive, stdin contains 0 integers (1 <= n <= 50). If `n` is odd, 'NO' is printed. If `n` is even, 'YES' is printed, and a string of 'A's and 'B's of length `n` is printed.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer represents the number of test cases (t) and each subsequent integer represents the size of a pattern (n). For each pattern size, if the size is odd, the function prints 'NO'. If the size is even, the function prints 'YES' followed by a string of alternating 'A's and 'B's of the specified length. The function processes all test cases and then terminates, leaving the standard input empty.

