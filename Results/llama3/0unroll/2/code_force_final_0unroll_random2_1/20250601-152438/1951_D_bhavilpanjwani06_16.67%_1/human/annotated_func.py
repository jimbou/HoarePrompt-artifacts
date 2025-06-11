#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000) — the number of test cases. Each of the following lines contains two positive integers n and k (1 <= n, k <= 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end.
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
            #This is printed: the current value of n (which is equal to the current value of k)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: (n - k + 1) (where n is the number of coins Alice has and k is the number of jewels Bob wants Alice to have bought), 1
            else :
                print('NO')
                #This is printed: NO
            #State: *`n` and `k` are positive integers, stdin contains multiple lines of input. The first line contains an integer t (0 <= t <= 1000) — the number of test cases. Each of the following lines contains two positive integers n and k (1 <= n, k <= 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. n is larger than or equal to k. n is not equal to k. If k - 1 < n - k + 1, then 'YES' is printed, 2 is printed, and the difference between n and k plus 1 is printed which is n - k + 1, and 1 is printed. If k - 1 is larger than or equal to n - k + 1, then 'NO' is printed.
        #State: *`n` and `k` are positive integers, stdin contains multiple lines of input. The first line contains an integer t (0 <= t <= 1000) — the number of test cases. Each of the following lines contains two positive integers n and k (1 <= n, k <= 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. n is larger than or equal to k. If n is equal to k, then 'YES' is printed, 1 is printed, and the value of `n` which is equal to `k` is printed. If n is not equal to k, then if k - 1 < n - k + 1, 'YES' is printed, 2 is printed, and the difference between n and k plus 1 is printed which is n - k + 1, and 1 is printed. If k - 1 is larger than or equal to n - k + 1, then 'NO' is printed.
    #State: *`n` and `k` are positive integers, stdin contains multiple lines of input. The first line contains an integer t (0 <= t <= 1000) — the number of test cases. Each of the following lines contains two positive integers n and k (1 <= n, k <= 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. If `n` is less than `k`, 'NO' is printed. If `n` is larger than or equal to `k`, then if `n` is equal to `k`, 'YES' is printed, 1 is printed, and the value of `n` which is equal to `k` is printed. If `n` is not equal to `k`, then if `k - 1` is less than `n - k + 1`, 'YES' is printed, 2 is printed, and the difference between `n` and `k` plus 1 is printed which is `n - k + 1`, and 1 is printed. If `k - 1` is larger than or equal to `n - k + 1`, then 'NO' is printed.

#Overall this is what the function does:Determines if Alice can buy a certain number of jewels with her coins and prints the result along with the number of jewels she can buy and the remaining coins.

