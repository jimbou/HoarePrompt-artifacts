#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer
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
        
    #State: Output State: The list l has been rotated to the right by k places, where k is the original value of k divided by 2, and the last element of the list has been moved to the front of the list. The value of n remains unchanged.

#Overall this is what the function does:Rotates the input list to the right by half of the input integer k places, moving the last element to the front, and returns the modified list, while keeping the input integer n unchanged.

#State of the program right berfore the function call: n and k are non-negative integers, n is the length of a permutation and k is the required Manhattan value.
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two values: the first value is 0, which is an integer, and the second value is also 0, which is an integer.
    #State: *`n` is a non-negative integer, `k` is a non-negative integer, stdin contains a space-separated list of integers, and `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` and `k` are non-negative integers, stdin contains a space-separated list of integers, and `k` is even. If `n` is odd, `max_k` is equal to `(n+k)/2`. If `n` is even, `max_k` is `n` squared divided by 2.
    if (max_k < k) :
        return 0, 0
        #The program returns two values: the first value is 0 and the second value is also 0.
    #State: *`n` and `k` are non-negative integers, stdin contains a space-separated list of integers, and `k` is even. If `n` is odd, `max_k` is equal to `(n+k)/2`. If `n` is even, `max_k` is `n` squared divided by 2. `max_k` is larger than or equal to `k`
    return n, k
    #The program returns two values: `n` which is a non-negative integer, and `k` which is an even non-negative integer.

#Overall this is what the function does:Determines the validity of a permutation based on its length and required Manhattan value, returning the original values if valid or zeros if invalid.

#State of the program right berfore the function call: l is a list of integers, and it represents a permutation of length n such that its Manhattan value is equal to k.
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: Output State: The list l has been printed to the console, with each integer separated by a space, and 'YES' is still being printed.
    print()
    #This is printed: a newline
    return
    #The program returns None

#Overall this is what the function does:Prints a list of integers to the console, separated by spaces, preceded by 'YES', and followed by a newline, and returns None.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2*10^5 and 0 <= k <= 10^12, and they are the output of function func_2().
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing because the return statement is empty. The value of 'n' remains 0, and 'NO' is still being printed. The values of 'n' and 'k' are still within their defined ranges, but they are not being returned or used in any way.
    #State: *`n` is an integer such that 1 <= n <= 2*10^5, `k` is an integer such that 0 <= k <= 10^12, and they are the output of function func_2(). `n` is not equal to 0
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns nothing

#Overall this is what the function does:This function determines whether a certain condition is met based on the input values 'n' and 'k', which are integers within specific ranges. If 'n' is 0, it prints 'NO' and returns without performing any further actions. If 'n' is not 0, it calls another function 'func_1' with 'n' and 'k' as arguments, assigns the result to 'l', and then calls another function 'func_3' with 'l' as an argument. The function does not return any value in either case.

