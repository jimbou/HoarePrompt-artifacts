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
                #This is printed: [n - k + 1], 1 (where n - k + 1 is a positive integer value)
            else :
                print('NO')
                #This is printed: NO
            #State: *`n` and `k` are positive integers, stdin contains multiple lines of input. The first line contains an integer t-1 (0 ≤ t-1 ≤ 999) — the number of test cases. Each of the following t-1 lines contains two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. n is larger than or equal to k and n is not equal to k. If k - 1 is less than n - k + 1, 'YES' is printed, and the number 2 is printed, and this is printed: n - k + 1 and 1. Otherwise, 'NO' is printed.
        #State: *`n` and `k` are positive integers, stdin contains multiple lines of input. The first line contains an integer t-1 (0 ≤ t-1 ≤ 999) — the number of test cases. Each of the following t-1 lines contains two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. n is larger than or equal to k. If n is equal to k, 'YES' is printed, and the number 1 is printed. If n is not equal to k, and k - 1 is less than n - k + 1, 'YES' is printed, and the number 2 is printed, and this is printed: n - k + 1 and 1. Otherwise, 'NO' is printed.
    #State: `n` and `k` are positive integers, stdin contains multiple lines of input. The first line contains an integer t-1 (0 ≤ t-1 ≤ 999) — the number of test cases. Each of the following t-1 lines contains two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. If `n` is less than `k`, 'NO' is printed. If `n` is equal to `k`, 'YES' is printed, and the number 1 is printed. If `n` is not equal to `k`, and `k - 1` is less than `n - k + 1`, 'YES' is printed, and the number 2 is printed, and this is printed: `n - k + 1` and 1. Otherwise, 'NO' is printed.

#Overall this is what the function does:Determines whether Alice can buy the desired number of jewels with her coins and prints the result along with the number of ways to do so if possible.

