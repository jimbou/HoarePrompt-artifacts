#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases. Each of the following t lines contains two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end.
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
                #This is printed: x (where x is the value of n - k + 1), 1
            else :
                print('NO')
                #This is printed: NO
            #State: *`n` and `k` are positive integers (1 ≤ n ≤ 10^18, 1 ≤ k ≤ 10^18), stdin contains t-1 lines of input, `n` is not less than `k`, and `n` is not equal to `k`. If `k-1` is less than `n-k+1`, then 'YES' is printed, followed by the number 2, `n-k+1`, and 1. Otherwise, 'NO' is printed.
        #State: *`n` and `k` are positive integers (1 ≤ n ≤ 10^18, 1 ≤ k ≤ 10^18), stdin contains t-1 lines of input, and `n` is not less than `k`. If `n` is equal to `k`, then 'YES' is printed, followed by the number 1, and 1 is printed. If `n` is not equal to `k`, then if `k-1` is less than `n-k+1`, 'YES' is printed, followed by the number 2, `n-k+1`, and 1. Otherwise, 'NO' is printed.
    #State: *`n` and `k` are positive integers (1 ≤ n ≤ 10^18, 1 ≤ k ≤ 10^18), stdin contains t-1 lines of input. If `n` is less than `k`, 'NO' is printed. If `n` is equal to `k`, 'YES' is printed, followed by the number 1, and 1 is printed. If `n` is greater than `k`, then if `k-1` is less than `n-k+1`, 'YES' is printed, followed by the number 2, `n-k+1`, and 1. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function determines whether Alice can buy a certain number of jewels with her available coins. It takes two positive integers `n` (the number of coins Alice has) and `k` (the number of jewels Bob wants Alice to buy) as input. If `n` is less than `k`, it prints 'NO'. If `n` is equal to `k`, it prints 'YES' followed by 1 and 1. If `n` is greater than `k`, it checks if `k-1` is less than `n-k+1`. If true, it prints 'YES' followed by 2, `n-k+1`, and 1. Otherwise, it prints 'NO'. The function processes multiple test cases from standard input, where the first line contains the number of test cases `t`.

