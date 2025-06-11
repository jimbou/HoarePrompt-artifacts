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
        
    #State: `n` is a positive integer, `k` is 0, `l` is a list of integers from 1 to `n` in reverse order, `i` is -1.

#Overall this is what the function does:Reorders a list of integers from 1 to n in a specific way based on the input k, resulting in a list where the last element is moved to a position determined by k, and the remaining elements are in reverse order.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two values: the first value is 0, and the second value is also 0.
    #State: *`n` is an integer such that 1 <= n <= 2 * 10^5 and `k` is an integer such that 0 <= k <= 10^12, stdin contains a space-separated list of integers, and k is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` is an integer such that 1 <= n <= 2 * 10^5 and `k` is an even integer such that 0 <= k <= 10^12, stdin contains a space-separated list of integers. If `n` is odd, `max_k` is an integer such that (n^2 - 1) // 2. If `n` is even, `max_k` is an integer such that 1/2 * n^2 <= max_k <= 1/2 * (2 * 10^5)^2.
    if (max_k < k) :
        return 0, 0
        #The program returns two values: 0 and 0. Both values are integers and are returned simultaneously.
    #State: *`n` is an integer such that 1 <= n <= 2 * 10^5, `k` is an even integer such that 0 <= k <= 10^12, stdin contains a space-separated list of integers. If `n` is odd, `max_k` is an integer such that (n^2 - 1) // 2. If `n` is even, `max_k` is an integer such that 1/2 * n^2 <= max_k <= 1/2 * (2 * 10^5)^2. `max_k` is larger than or equal to `k`
    return n, k
    #The program returns two values: `n`, which is an integer between 1 and 2 * 10^5 (inclusive), and `k`, which is an even integer between 0 and 10^12 (inclusive). Additionally, if `n` is odd, `k` is less than or equal to (n^2 - 1) // 2, and if `n` is even, `k` is less than or equal to 1/2 * n^2.

#Overall this is what the function does:This function takes two integers, `n` and `k`, as input, where `n` is between 1 and 2 * 10^5 (inclusive) and `k` is between 0 and 10^12 (inclusive). It checks if `k` is even and if `k` is within a certain range based on `n`. If `k` is odd or exceeds the maximum allowed value based on `n`, the function returns two zeros. Otherwise, it returns the original `n` and `k` values. The function effectively filters or validates the input values based on these conditions.

#State of the program right berfore the function call: l is a list of integers
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: 'YES' is being printed, and l is a list of integers that has been exhausted, and i is the last integer in the list.
    print()
    #This is printed: YES
    return
    #The program returns nothing, 'YES' has been printed, and list 'l' is exhausted, and 'i' is the last integer in the list.

#Overall this is what the function does:Prints 'YES' followed by the elements of the input list 'l', exhausting the list, and returns nothing.

#State of the program right berfore the function call: n and k are integers such that n is non-negative and k is non-negative, and they are the result of a function func_2() that presumably reads input from somewhere.
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, as the return statement is empty. The current state of the program remains unchanged, with 'n' still being 0 and 'NO' still being printed. The values of 'n' and 'k' remain as non-negative integers, but their specific values are not affected by the empty return statement.
    #State: *`n` and `k` are non-negative integers, and they are the result of a function `func_2()` that presumably reads input from somewhere. `n` is larger than 0
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns nothing, as there is no value or variable specified in the return statement. The values of n, k, and l remain unchanged, with n being a non-negative integer greater than 0, k being a non-negative integer, and l being the result of the function func_1(n, k).

#Overall this is what the function does:This function takes two non-negative integers `n` and `k` as input, which are presumably obtained from a function `func_2()`. If `n` is 0, it prints 'NO' and returns without modifying the input values. If `n` is greater than 0, it calls another function `func_1(n, k)` to obtain a value `l`, and then calls a third function `func_3(l)` without returning any value. In both cases, the input values `n` and `k` remain unchanged.

