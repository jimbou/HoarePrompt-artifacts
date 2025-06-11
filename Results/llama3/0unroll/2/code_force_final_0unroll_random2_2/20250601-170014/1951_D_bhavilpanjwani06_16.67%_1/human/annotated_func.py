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
            print(n)
            #This is printed: k (where k is the value of k)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: a positive integer greater than 1, 1
            else :
                print('NO')
                #This is printed: NO
            #State: *A `ValueError` is raised because the second part of the input line cannot be converted to an integer. The stdin still contains multiple lines of input, but the first line has been read. `n` is not less than `k` and `n` is not equal to `k`. If `k - 1` is less than `n - k + 1`, 'YES' is printed, the number 2 is printed, and the value of `n - k + 1` which is greater than 1 is printed, followed by the number 1. If `k - 1` is not less than `n - k + 1`, 'NO' is printed.
        #State: *A `ValueError` is raised because the second part of the input line cannot be converted to an integer. The stdin still contains multiple lines of input, but the first line has been read. `n` is not less than `k`. If `n` equals `k`, 'YES' is printed, followed by the number 1, and the value of `n` which is equal to `k` is printed. If `n` does not equal `k`, then if `k - 1` is less than `n - k + 1`, 'YES' is printed, the number 2 is printed, and the value of `n - k + 1` which is greater than 1 is printed, followed by the number 1. If `k - 1` is not less than `n - k + 1`, 'NO' is printed.
    #State: *A `ValueError` is raised because the second part of the input line cannot be converted to an integer. The stdin still contains multiple lines of input, but the first line has been read. If `n` is less than `k`, 'NO' is printed. If `n` is not less than `k`, then if `n` equals `k`, 'YES' is printed, followed by the number 1, and the value of `n` which is equal to `k` is printed. If `n` does not equal `k`, then if `k - 1` is less than `n - k + 1`, 'YES' is printed, the number 2 is printed, and the value of `n - k + 1` which is greater than 1 is printed, followed by the number 1. If `k - 1` is not less than `n - k + 1`, 'NO' is printed.

#Overall this is what the function does:Determines whether Alice can buy a certain number of jewels with her coins and prints the result along with the number of jewels and the number of coins used.

