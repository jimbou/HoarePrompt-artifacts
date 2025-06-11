#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 1000) followed by t lines, each containing two positive integers n and k (1 ≤ n, k ≤ 10^18).
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
                #This is printed: (n - k + 1) (where n - k + 1 is a positive integer greater than 1), 1
            else :
                print('NO')
                #This is printed: NO
            #State: *`n` and `k` are positive integers (1 ≤ n, k ≤ 10^18), stdin contains an integer t-1 (0 ≤ t-1 ≤ 999) followed by t-1 lines, each containing two positive integers n and k (1 ≤ n, k ≤ 10^18). `n` is not less than `k` and `n` is not equal to `k`. If `k-1` is less than `n-k+1`, 'YES' is printed, the number 2 is printed, and the value of `n - k + 1` and the number 1 are printed. Otherwise, 'NO' is printed.
        #State: *`n` and `k` are positive integers (1 ≤ n, k ≤ 10^18), `n` is not less than `k`. If `n` equals `k`, 'YES' is printed, and 1 is printed twice. If `n` is not equal to `k`, 'YES' is printed, the number 2 is printed, and the value of `n - k + 1` and the number 1 are printed if `k-1` is less than `n-k+1`. Otherwise, 'NO' is printed.
    #State: *`n` and `k` are positive integers (1 ≤ n, k ≤ 10^18), stdin contains an integer t-1 (0 ≤ t-1 ≤ 999) followed by t-1 lines, each containing two positive integers n and k (1 ≤ n, k ≤ 10^18). If `n` is less than `k`, 'NO' is printed. If `n` equals `k`, 'YES' is printed, and 1 is printed twice. If `n` is greater than `k`, 'YES' is printed, the number 2 is printed, and the value of `n - k + 1` and the number 1 are printed if `k-1` is less than `n-k+1`. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function determines whether it is possible to partition a set of `n` elements into `k` non-empty subsets, where `n` and `k` are positive integers. It reads input from stdin, where each line contains two positive integers `n` and `k`. The function prints 'YES' if partitioning is possible and 'NO' otherwise. If partitioning is possible, it also prints the number of subsets and the size of each subset. The function handles three cases: (1) `n` is less than `k`, in which case it prints 'NO'; (2) `n` is equal to `k`, in which case it prints 'YES' and the size of each subset (1); and (3) `n` is greater than `k`, in which case it prints 'YES' and the size of each subset if `k-1` is less than `n-k+1`, otherwise it prints 'NO'.

