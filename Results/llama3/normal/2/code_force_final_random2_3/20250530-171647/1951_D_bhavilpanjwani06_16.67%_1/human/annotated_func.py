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
            print(n)
            #This is printed: 1
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: n - k + 1 (where n - k + 1 is the difference between n and k plus 1), 1
            else :
                print('NO')
                #This is printed: NO
            #State: *`n` and `k` are positive integers between 1 and 10^18, `n` is not less than `k` and `n` is not equal to `k`. If `k-1` is less than `n-k+1`, 'YES' is printed, 2 is printed, and `n-k+1` is printed. If `k-1` is not less than `n-k+1`, 'NO' is printed.
        #State: *`n` and `k` are positive integers between 1 and 10^18, `n` is not less than `k`. If `n` is equal to `k`, 'YES' is printed, 1 is printed, and the value of `n` which is equal to `k` is printed. If `n` is not equal to `k`, then if `k-1` is less than `n-k+1`, 'YES' is printed, 2 is printed, and `n-k+1` is printed. Otherwise, 'NO' is printed.
    #State: *`n` and `k` are positive integers between 1 and 10^18. If `n` is less than `k`, 'NO' is printed. If `n` is not less than `k`, then if `n` is equal to `k`, 'YES' is printed, 1 is printed, and the value of `n` which is equal to `k` is printed. If `n` is not equal to `k`, then if `k-1` is less than `n-k+1`, 'YES' is printed, 2 is printed, and `n-k+1` is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function determines whether it is possible to partition a set of `n` elements into `k` non-empty subsets, where `n` and `k` are positive integers between 1 and 10^18. It prints 'YES' if possible, along with the number of subsets and their sizes, and 'NO' otherwise. The function takes no arguments and reads input from stdin, where each line contains two positive integers `n` and `k`. The function handles three cases: (1) `n` is less than `k`, in which case it prints 'NO'; (2) `n` is equal to `k`, in which case it prints 'YES', 1, and `n`; and (3) `n` is greater than `k`, in which case it checks if `k-1` is less than `n-k+1`, printing 'YES', 2, and `n-k+1` if true, and 'NO' otherwise.

