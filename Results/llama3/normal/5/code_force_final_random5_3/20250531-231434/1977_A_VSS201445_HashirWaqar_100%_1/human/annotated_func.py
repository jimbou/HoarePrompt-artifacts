#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: `n` and `m` are integers between 1 and 100 inclusive, stdin is empty, _ is t-1. If `n` is greater than or equal to `m` and the difference between `n` and `m` is even, 'YES' has been printed. Otherwise, 'NO' has been printed.

#Overall this is what the function does:Determines whether the difference between two integers is even and prints 'YES' or 'NO' accordingly, repeating this process for a specified number of test cases.

