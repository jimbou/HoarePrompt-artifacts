#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n < m:
            print('NO')
        elif n & 1 and m & 1 or n % 2 == 0 and m % 2 == 0:
            print('YES')
        
    #State: `n` and `m` are integers between 1 and 100, stdin is empty. If `n` is less than `m`, 'NO' is printed. Otherwise, if both `n` and `m` are odd or both are even, 'YES' is printed.

#Overall this is what the function does:Determines whether two integers are both odd or both even, and prints 'YES' if they are, 'NO' if the first integer is less than the second, and handles multiple test cases from standard input.

