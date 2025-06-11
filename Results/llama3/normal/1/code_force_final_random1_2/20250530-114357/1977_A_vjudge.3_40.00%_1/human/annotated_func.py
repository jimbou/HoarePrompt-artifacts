#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()]
        
        if n == m:
            print('Yes')
        elif m > n:
            print('No')
        elif m == n - 1:
            print('Yes')
        elif m % 2 == 0 and n % 2 == 0:
            print('Yes')
        elif m % 2 != 0 and n % 2 != 0:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is an integer between 1 and 100 (inclusive), stdin is empty, `i` is `t`, `n` and `m` are the last two integers read from stdin. If `n` equals `m`, 'Yes' is printed. If `n` does not equal `m`, then if `m` > `n`, 'No' is printed. If `m` is one less than `n`, 'Yes' is printed. If `m` and `n` are both even or both odd, 'Yes' is printed. If `m` and `n` have different parity, 'No' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers, and determines whether the second integer is compatible with the first integer based on specific rules. It then prints 'Yes' if the integers are compatible and 'No' otherwise. The function processes all test cases and empties the standard input.

