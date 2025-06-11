#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two positive integers n and k (1 <= n, k <= 10^18).
    n, k = map(int, input().split())
    if (n < k) :
        print('NO')
        #This is printed: NO
    else :
        if (n == k) :
            print('YES')
            #This is printed: YES
            print(1)
            #This is printed: 1
            print(1)
            #This is printed: 1
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: n - k + 1 (where n - k + 1 is a positive integer), 1
            else :
                print('NO')
                #This is printed: NO
            #State: *`n` and `k` are positive integers, `n` is larger than or equal to `k`, and `n` is not equal to `k`. stdin contains t-1 lines, each containing two positive integers n and k (1 <= n, k <= 10^18), where t is a positive integer (1 <= t <= 1000). If `k-1` is less than `n-k+1`, 'YES' is printed, followed by the number 2, the value of `n-k+1`, and the number 1. Otherwise, 'NO' is printed.
        #State: *`n` and `k` are positive integers, `n` is larger than or equal to `k`, and stdin contains t-1 lines, each containing two positive integers n and k (1 <= n, k <= 10^18), where t is a positive integer (1 <= t <= 1000). If `n` is equal to `k`, 'YES' is printed, followed by the number 1. If `n` is not equal to `k`, 'YES' is printed, followed by the number 2, the value of `n-k+1`, and the number 1, if `k-1` is less than `n-k+1`. Otherwise, 'NO' is printed.
    #State: *`n` and `k` are positive integers, stdin contains t-1 lines, each containing two positive integers n and k (1 <= n, k <= 10^18), where t is a positive integer (1 <= t <= 1000). If `n` is less than `k`, 'NO' is printed. If `n` is equal to `k`, 'YES' is printed, followed by the number 1. If `n` is larger than `k`, 'YES' is printed, followed by the number 2, the value of `n-k+1`, and the number 1, if `k-1` is less than `n-k+1`. Otherwise, 'NO' is printed.

#Overall this is what the function does:Determines if a given pair of positive integers `n` and `k` can be combined in a specific way and prints the result. If `n` is less than `k`, it prints 'NO'. If `n` is equal to `k`, it prints 'YES' followed by the number 1. If `n` is larger than `k`, it checks if `k-1` is less than `n-k+1` and prints 'YES' followed by the number 2, the value of `n-k+1`, and the number 1 if true, otherwise it prints 'NO'.

