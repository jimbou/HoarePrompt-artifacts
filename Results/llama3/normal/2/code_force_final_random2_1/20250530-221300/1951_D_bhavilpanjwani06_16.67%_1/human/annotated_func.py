#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases. Each of the following lines contains two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end.
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
            #This is printed: k (where k is the current value of k)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: n - k + 1 (where n - k + 1 is a positive integer greater than or equal to 1), 1
            else :
                print('NO')
                #This is printed: NO
            #State: *`n` and `k` are positive integers (1 ≤ n, k ≤ 10^18), stdin contains multiple lines of input, the first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases minus one, and the rest of the lines contain two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. Additionally, `n` is larger than or equal to `k` and `n` is not equal to `k`. If `k - 1` is less than `n - k + 1`, then the number 2 is printed, and this is printed: `n - k + 1` and 1. Otherwise, 'NO' is printed.
        #State: `n` and `k` are positive integers (1 ≤ n, k ≤ 10^18), stdin contains multiple lines of input, the first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases minus one, and the rest of the lines contain two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. Additionally, `n` is larger than or equal to `k`. If `n` is equal to `k`, 'YES' is printed, and 1 is printed, and the value of `n` which is equal to `k` is being printed. If `n` is not equal to `k`, then if `k - 1` is less than `n - k + 1`, then the number 2 is printed, and this is printed: `n - k + 1` and 1. Otherwise, 'NO' is printed.
    #State: *`n` and `k` are positive integers (1 ≤ n, k ≤ 10^18), stdin contains multiple lines of input, the first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases minus one, and the rest of the lines contain two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. If `n` is less than `k`, 'NO' is printed. If `n` is equal to `k`, 'YES' is printed, and 1 is printed, and the value of `n` which is equal to `k` is being printed. If `n` is larger than `k`, then if `k - 1` is less than `n - k + 1`, then the number 2 is printed, and this is printed: `n - k + 1` and 1. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function determines whether it is possible for Alice to buy a certain number of jewels with her available coins, and if so, prints the minimum number of transactions required to do so. It takes two positive integers as input, `n` and `k`, representing the number of coins Alice has and the number of jewels Bob wants her to buy, respectively. If `n` is less than `k`, it prints 'NO'. If `n` is equal to `k`, it prints 'YES', '1', and the value of `n`. If `n` is greater than `k`, it checks if `k - 1` is less than `n - k + 1`, and if so, prints 'YES', '2', and the values `n - k + 1` and '1'. Otherwise, it prints 'NO'.

