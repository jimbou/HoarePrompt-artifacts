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
        
    #State: `t` is greater than or equal to 0, `i` is equal to `t`, `n` and `m` are integers between 1 and 100, stdin is empty. If `n` equals `m`, 'Yes' is printed. If `m` is greater than `n`, 'No' is printed. If `m` equals `n-1`, 'Yes' is printed. Otherwise, if both `m` and `n` are even integers or both are odd integers, 'Yes' is printed. Otherwise, 'No' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, n and m. It then determines whether the numbers satisfy certain conditions and prints 'Yes' or 'No' accordingly. The conditions are: if n equals m, if m is one less than n, or if both n and m are either even or odd integers. If none of these conditions are met, it prints 'No'. The function processes all test cases and prints the corresponding results.

