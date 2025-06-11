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
        
    #State: `t` is an integer between 1 and 100, `n` and `m` are integers between 1 and 100 inclusive, `i` is `t-1`, stdin is empty. If `n` equals `m`, 'Yes' is printed. If `m` is greater than `n`, 'No' is printed. If `m` is one less than `n`, 'Yes' is printed. If both `m` and `n` are even or both are odd, 'Yes' is printed. Otherwise, 'No' is printed.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t pairs of integers n and m. It then checks each pair and prints 'Yes' if n equals m, m is one less than n, or both n and m have the same parity (both even or both odd). Otherwise, it prints 'No'. The function processes all t pairs and empties the standard input.

