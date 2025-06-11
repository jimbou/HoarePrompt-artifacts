#State of the program right berfore the function call: n and k are positive integers such that 1 <= n, k <= 10^18.
    if (n == k) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(1)
        #This is printed: 1
        return
        #The program returns nothing, 'YES' is printed, and the number 1 is printed twice. The values of n and k remain unchanged as positive integers such that 1 <= n, k <= 10^18, and n is still equal to k.
    #State: *n and k are positive integers such that 1 <= n, k <= 10^18, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: *n and k are positive integers such that 1 <= n, k <= 10^18, n is not equal to k, and n is greater than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: n is 0, k is a positive integer less than n, h is the sum of n // (n - k + 1) + n // 1 + n // 1 + ... + n // 1 (k - 1 times), costs is a list containing two elements: n - k + 1 and 1, i is 1, curr is 0, n is 0
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: 2 1
    #State: *n is 0, k is a positive integer less than n, h is the sum of n // (n - k + 1) + n // 1 + n // 1 + ... + n // 1 (k - 1 times), costs is a list containing two elements: n - k + 1 and 1, i is 1, curr is 0. If h is less than k, 'NO' is printed. If h is larger than or equal to k, 'YES' is printed, the number 2 is printed, and the elements of the list costs which are n - k + 1 and 1 are printed.

#Overall this is what the function does:This function determines whether it is possible to divide a given positive integer `n` into `k` parts such that the sum of the parts is greater than or equal to `k`. It takes two positive integers `n` and `k` as input and prints 'YES' or 'NO' accordingly. If 'YES' is printed, it also prints the number of parts and the sizes of the parts. If `n` is equal to `k`, it prints 'YES' and the number 1 twice. If `n` is less than `k`, it prints 'NO'. Otherwise, it calculates the sum of the parts by dividing `n` into two parts: `n - k + 1` and `1`, and checks if the sum is greater than or equal to `k`. If the sum is less than `k`, it prints 'NO'. If the sum is greater than or equal to `k`, it prints 'YES', the number 2, and the sizes of the two parts.

