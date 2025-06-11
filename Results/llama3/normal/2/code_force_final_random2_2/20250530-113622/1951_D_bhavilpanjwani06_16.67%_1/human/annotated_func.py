#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
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
            #This is printed: k (where k is the value of k which is equal to n)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: n - k + 1 (where n is an integer greater than 0 and k is an integer such that n is greater than or equal to k and n is not equal to k), 1
            else :
                print('NO')
                #This is printed: NO
            #State: *`n` is an integer greater than 0, `k` is an integer, stdin is empty, `n` is greater than or equal to `k`, and `n` is not equal to `k`. If `k - 1` is less than `n - k + 1`, 'YES' is printed, the number 2 is printed, and the values `n - k + 1` and 1 are printed. Otherwise, 'NO' is printed.
        #State: *`n` is an integer greater than 0, `k` is an integer, stdin is empty, and `n` is greater than or equal to `k`. If `n` is equal to `k`, 'YES' is printed, 1 is printed, and the value of `n` which is equal to `k` is printed. If `n` is not equal to `k`, and `k - 1` is less than `n - k + 1`, 'YES' is printed, the number 2 is printed, and the values `n - k + 1` and 1 are printed. Otherwise, 'NO' is printed.
    #State: *`n` is an integer greater than 0, `k` is an integer, stdin is empty. If `n` is less than `k`, 'NO' is printed. If `n` is greater than or equal to `k`, then if `n` is equal to `k`, 'YES', 1, and `n` are printed. If `n` is not equal to `k` and `k - 1` is less than `n - k + 1`, 'YES', 2, `n - k + 1`, and 1 are printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:Determines if a given integer `n` is greater than or equal to another integer `k`, and if so, prints 'YES' along with specific values based on the relationship between `n` and `k`. If `n` is less than `k`, prints 'NO'. If `n` equals `k`, prints 'YES', 1, and the value of `n` (which is equal to `k`). If `n` is greater than `k` and `k - 1` is less than `n - k + 1`, prints 'YES', 2, `n - k + 1`, and 1. Otherwise, prints 'NO'.

