#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000). Each of the following t lines contains two positive integers n and k (1 <= n, k <= 10^18).
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
            #This is printed: k (where k is the current value of k, which is equal to n)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: [n - k + 1] (where n is the current value of n and k is the current value of k), 1
            else :
                print('NO')
                #This is printed: NO
            #State: *`n` and `k` are positive integers, stdin contains multiple lines of input. The first line contains an integer t-1 (0 <= t-1 <= 999). Each of the following t-1 lines contains two positive integers n and k (1 <= n, k <= 10^18). n is larger than or equal to k and n is not equal to k. If k-1 is less than n-k+1, 'YES' is printed, 2 is printed, and the value of n-k+1 and 1 are printed. If k-1 is not less than n-k+1, 'NO' is printed.
        #State: *`n` and `k` are positive integers, stdin contains multiple lines of input. The first line contains an integer t-1 (0 <= t-1 <= 999). Each of the following t-1 lines contains two positive integers n and k (1 <= n, k <= 10^18). n is larger than or equal to k. If `n` is equal to `k`, 'YES' is printed, 1 is printed, and the value of `n` which is equal to `k` is printed. If `n` is not equal to `k`, then if k-1 is less than n-k+1, 'YES' is printed, 2 is printed, and the value of n-k+1 and 1 are printed. If k-1 is not less than n-k+1, 'NO' is printed.
    #State: *`n` and `k` are positive integers, stdin contains multiple lines of input. The first line contains an integer t-1 (0 <= t-1 <= 999). Each of the following t-1 lines contains two positive integers n and k (1 <= n, k <= 10^18). If `n` is less than `k`, 'NO' is printed. If `n` is equal to `k`, 'YES' is printed, 1 is printed, and the value of `n` which is equal to `k` is printed. If `n` is larger than `k`, then if k-1 is less than n-k+1, 'YES' is printed, 2 is printed, and the value of n-k+1 and 1 are printed. If k-1 is not less than n-k+1, 'NO' is printed.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t (1 <= t <= 1000) and each subsequent line contains two positive integers n and k (1 <= n, k <= 10^18). It then checks the relationship between n and k, and based on the comparison, it prints either 'YES' or 'NO' followed by additional information. If n is less than k, it prints 'NO'. If n is equal to k, it prints 'YES', 1, and the value of n (which is equal to k). If n is greater than k, it checks if k-1 is less than n-k+1, and if true, it prints 'YES', 2, and the values of n-k+1 and 1. Otherwise, it prints 'NO'.

