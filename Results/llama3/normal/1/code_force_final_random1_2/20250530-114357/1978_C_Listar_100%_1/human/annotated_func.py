#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer
    k = k // 2
    l = list(range(1, n + 1))
    c = 0
    for i in range(n, -1, -2):
        c += 1
        
        if k == 0:
            return l
        
        if k < i - 1:
            return func_2(c, k, l)
        
        k = k - i + 1
        
        l = func_3(c, l)
        
    #State: The program returns a list of integers from 1 to n, where n is a positive integer, and c is equal to the number of iterations of the loop.

#Overall this is what the function does:This function takes a positive integer `n` and a non-negative integer `k` as input, and returns a list of integers from 1 to `n`. The function iterates over the list, potentially modifying it by calling `func_3`, and keeps track of the number of iterations `c`. If `k` becomes 0 or less than the current iteration index, the function returns the list. Otherwise, it continues iterating and modifying the list until the loop completes, at which point it returns the final list.

#State of the program right berfore the function call: c and k are non-negative integers, l is a list of distinct integers from 1 to n in arbitrary order, and c + k < len(l).
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns a list of distinct integers from 1 to n in arbitrary order, where the elements at indices -c and -c - k are swapped, c is a non-negative integer, k is a non-negative integer, and c + k < len(l).

#Overall this is what the function does:Swaps the elements at the specified indices in the input list and returns the modified list. The function takes a list of distinct integers and two non-negative integers c and k as input, where c + k is less than the length of the list. It swaps the elements at indices -c and -c - k in the list and returns the resulting list, preserving the original order of the other elements.

#State of the program right berfore the function call: c is a positive integer, l is a list of integers, and c <= len(l).
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns list 'l' where the cth element from the start and the cth element from the end have been swapped, and c is a positive integer less than or equal to the length of list 'l'.

#Overall this is what the function does:Swaps the cth element from the start and the cth element from the end of a given list 'l', where 'c' is a positive integer less than or equal to the length of 'l', and returns the modified list.

#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer.
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two values: 0 and 0. The first 0 is an integer and the second 0 is also an integer.
    #State: *`n` is a positive integer, `k` is a non-negative integer, stdin contains a space-separated list of two integers, and `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` is a positive integer, `k` is a non-negative integer, stdin contains a space-separated list of two integers, and `k` is even. If `n` is odd, `max_k` is a positive integer equal to `(n + k) / 2`. If `n` is even, `max_k` is `n` squared divided by 2.
    if (max_k < k) :
        return 0, 0
        #The program returns two values: 0 and 0. Both values are integers and are equal to zero. No variables or values from the initial state are returned.
    #State: *`n` is a positive integer, `k` is a non-negative integer, stdin contains a space-separated list of two integers, and `k` is even. If `n` is odd, `max_k` is a positive integer equal to `(n + k) / 2`. If `n` is even, `max_k` is `n` squared divided by 2. `max_k` is larger than or equal to `k`
    return n, k
    #The program returns two values: a positive integer `n` and a non-negative integer `k` that is even.

#Overall this is what the function does:This function takes two integers, n and k, as input from the user, where n is a positive integer and k is a non-negative integer. It checks if k is even and if n is odd or even. If k is odd, the function returns two zeros. If k is even, it calculates a maximum value max_k based on whether n is odd or even. If max_k is less than k, the function returns two zeros. Otherwise, it returns the original values of n and k. The function effectively filters the input values based on the parity of k and the relationship between max_k and k, returning either the original values or zeros.

#State of the program right berfore the function call: l is a list of integers
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: l is an empty list, 'YES' is being printed, and all the integers in the list are being printed.
    print()
    #This is printed: YES, an empty list
    return
    #The program returns nothing.

#Overall this is what the function does:The function prints 'YES' followed by all integers in the input list, and then returns without any output, leaving the input list empty.

#State of the program right berfore the function call: n and k are integers such that n is non-negative and k is non-negative and the result of func_4() is a tuple of two integers (n, k).
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, and the current value of 'n' is 0, and 'NO' is being printed
    #State: `n` and `k` are integers such that `n` is non-negative and `k` is non-negative, and the values of `n` and `k` are returned by the function `func_4()`, and `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns the return value of func_1(n, k), where n is a non-negative integer not equal to 0, and k is a non-negative integer.

#Overall this is what the function does:This function determines whether to print 'NO' or return a value based on the input values 'n' and 'k'. If 'n' is 0, it prints 'NO' and returns nothing. Otherwise, it calls another function 'func_1' with 'n' and 'k' as arguments, passes the result to 'func_5', and returns the result of 'func_1'.

