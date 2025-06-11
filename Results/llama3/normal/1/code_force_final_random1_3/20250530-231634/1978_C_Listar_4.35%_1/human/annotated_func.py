#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer.
    k = k // 2
    l = list(range(1, n + 1))
    for i in range(n - 1, -1, -1):
        if k == 0:
            return l
        
        if 1 + i > k:
            x = l[-1]
            l.pop(-1)
            l.insert(-k, x)
            return l
        
        k = k - i + 1
        
        x = l[-1]
        
        l.pop(-1)
        
        l.insert(0, x)
        
    #State: The list `l` contains all integers from 1 to `n` in ascending order, and `k` is 0.

#Overall this is what the function does:Rearranges the elements of a list of integers from 1 to n in ascending order, based on the value of a non-negative integer k, and returns the rearranged list. If k is 0, the original list is returned. Otherwise, the function performs a series of rotations on the list, moving the last element to a position determined by k, until k becomes 0. The final state of the program is a list containing all integers from 1 to n in ascending order, with k being 0.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2*10^5 and 0 <= k <= 10^12.
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two values: the first value is 0, which is an integer, and the second value is also 0, which is an integer.
    #State: *`n` is an integer such that 1 <= n <= 2*10^5 and `k` is an integer such that 0 <= k <= 10^12, stdin contains a space-separated list of two integers. k is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` is an integer such that 1 <= n <= 2*10^5, `k` is an even integer such that 0 <= k <= 10^12, stdin contains a space-separated list of two integers. If `n` is odd, `max_k` is an integer equal to (n^2 - 1) // 2. If `n` is even, `max_k` is an integer equal to 1/2 * n^2.
    if (max_k < k) :
        return 0, 0
        #The program returns two values: 0 and 0. Both values are integers and are equal to zero.
    #State: *`n` is an integer such that 1 <= n <= 2*10^5, `k` is an even integer such that 0 <= k <= 10^12, stdin contains a space-separated list of two integers. If `n` is odd, `max_k` is an integer equal to (n^2 - 1) // 2. If `n` is even, `max_k` is an integer equal to 1/2 * n^2. `max_k` is larger than or equal to `k`
    return n, k
    #The program returns a tuple containing two values: `n` and `k`. `n` is an integer between 1 and 2*10^5 (inclusive), and `k` is an even integer between 0 and 10^12 (inclusive). Additionally, if `n` is odd, `k` is less than or equal to `(n^2 - 1) // 2`, and if `n` is even, `k` is less than or equal to `1/2 * n^2`.

#Overall this is what the function does:This function takes two integers, `n` and `k`, as input from the user, where `n` is between 1 and 2*10^5 (inclusive) and `k` is between 0 and 10^12 (inclusive). If `k` is odd, the function immediately returns two zeros. If `k` is even, it calculates the maximum possible value of `k` based on `n` and checks if the input `k` is within this limit. If `k` exceeds this limit, the function returns two zeros. Otherwise, it returns the original `n` and `k` values.

#State of the program right berfore the function call: l is a list of integers, containing n distinct integers from 1 to n in arbitrary order, where n is the length of the permutation.
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: l is a list of integers that must have n integers, i is the nth integer in the list, 'YES' is being printed, and the nth integer in the list which is i is being printed.
    print()
    #This is printed: YES, i (where i is the nth integer in the list)
    return
    #The program returns nothing

#Overall this is what the function does:Prints 'YES' followed by the elements of the input list, one integer per line, and returns no value.

#State of the program right berfore the function call: n is a non-negative integer and k is a non-negative integer
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, as the return statement is empty. The current value of `n` remains 0, and 'NO' is still being printed. The values of `n` and `k` previously returned by `func_2()` are not affected.
    #State: *`n` and `k` are returned by `func_2()`, and `n` is not equal to 0
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns the value returned by func_1(n, k), where n is not equal to 0 and n and k are returned by func_2().

#Overall this is what the function does:This function determines whether to print 'NO' or return a value based on the value of `n` returned by `func_2()`. If `n` is 0, it prints 'NO' and returns nothing. If `n` is not 0, it calls `func_1(n, k)` and `func_3(l)`, and returns the value returned by `func_1(n, k)`.

