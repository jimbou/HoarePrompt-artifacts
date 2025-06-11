#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end.
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
                #This is printed: a value greater than or equal to 1, 1
            else :
                print('NO')
                #This is printed: NO
            #State: *`n` and `k` are positive integers, stdin contains multiple test cases - 1, `n` is larger than or equal to `k`, and `n` is not equal to `k`. If `k - 1` is less than `n - k + 1`, 'YES' is printed, the number 2 is printed, and the difference between `n` and `k` plus 1 is printed. Otherwise, 'NO' is printed.
        #State: *`n` and `k` are positive integers, stdin contains multiple test cases - 1, `n` is larger than or equal to `k`. If `n` is equal to `k`, 'YES' is printed, and 1 is printed twice. If `n` is not equal to `k`, and `k - 1` is less than `n - k + 1`, 'YES' is printed, the number 2 is printed, and the difference between `n` and `k` plus 1 is printed. Otherwise, 'NO' is printed.
    #State: *`n` and `k` are positive integers, stdin contains multiple test cases - 1. If `n` is less than `k`, 'NO' is printed. If `n` is equal to `k`, 'YES' is printed, and 1 is printed twice. If `n` is larger than `k`, and `k - 1` is less than `n - k + 1`, 'YES' is printed, the number 2 is printed, and the difference between `n` and `k` plus 1 is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:Determines if Alice can buy a certain number of jewels with her coins and prints the result along with the number of purchases and the amount spent on each purchase, if possible.

