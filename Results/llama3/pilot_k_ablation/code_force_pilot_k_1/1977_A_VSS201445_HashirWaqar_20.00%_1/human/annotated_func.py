#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n < m:
            print('NO')
        elif n & 1 and m & 1 or n % 2 == 0 and m % 2 == 0:
            print('YES')
        
    #State: `_` is equal to the number of test cases t, stdin is empty, for each test case, if `n` is less than `m`, 'NO' is printed, otherwise, if `n` and `m` are both odd or both even, 'YES' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers n and m. It then checks each case and prints 'YES' if n and m are both odd or both even, and 'NO' if n is less than m. The function processes all test cases and empties the standard input.

