#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer.
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
        
    #State: Output State: n is a positive integer, k is a non-negative integer equal to its original value divided by 2, l is a list of integers from 1 to n, c is 0

#Overall this is what the function does:This function takes a positive integer n and a non-negative integer k as input, modifies k by dividing it by 2, and generates a list of integers from 1 to n. It then iterates through the list in reverse order, incrementing a counter c and potentially modifying the list and k based on certain conditions. The function may return the list at various points during the iteration, either directly or by calling other functions (func_2 and func_3), and ultimately returns the modified list. The function's purpose is to transform the input list and integers based on the given conditions and return the resulting list.

#State of the program right berfore the function call: c and k are non-negative integers, l is a list of distinct integers from 1 to n in arbitrary order, and c+k < len(l).
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns a list of distinct integers from 1 to n in arbitrary order, where the values at indices -c and -c-k have been swapped, and c+k < len(l).

#Overall this is what the function does:Swaps the values at the last c and last c+k indices of a list of distinct integers from 1 to n, returning the modified list.

#State of the program right berfore the function call: c is a positive integer and l is a list of integers such that c <= len(l) and the elements of l are distinct integers from 1 to len(l) in arbitrary order.
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns list 'l' of integers with distinct integers from 1 to len(l) in arbitrary order, but the values at indices c-1 and -c have been swapped, where c is a positive integer and c <= len(l).

#Overall this is what the function does:Swaps the elements at indices c-1 and -c in a list of distinct integers, returning the modified list.

#State of the program right berfore the function call: n and k are non-negative integers, n is the length of a permutation and k is the required Manhattan value.
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two values: the first value is 0, which is an integer, and the second value is also 0, which is an integer.
    #State: `n` and `k` are non-negative integers, `n` is assigned the first integer from the input and `k` is assigned the second integer from the input, stdin contains no input, and `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` and `k` are non-negative integers, stdin contains no input, and `k` is even. If `n` is odd, `max_k` is an integer equal to `(n + k) / 2`. If `n` is even, `max_k` is equal to `n` squared divided by 2.
    if (max_k < k) :
        return 0, 0
        #The program returns two values: 0 and 0. Both values are integers and are equal to zero. No variables are returned, only literal values. The values of `n`, `k`, and `max_k` are not affected by the return statement and remain unchanged.
    #State: *`n` and `k` are non-negative integers, stdin contains no input, and `k` is even. If `n` is odd, `max_k` is an integer equal to `(n + k) / 2`. If `n` is even, `max_k` is equal to `n` squared divided by 2. `max_k` is larger than or equal to `k`
    return n, k
    #The program returns two non-negative integers, `n` and `k`, where `k` is even, and `n` can be either odd or even. If `n` is odd, `max_k` is an integer equal to `(n + k) / 2`, otherwise, `max_k` is equal to `n` squared divided by 2, and `max_k` is larger than or equal to `k`.

#Overall this is what the function does:This function determines whether a given Manhattan value (k) is achievable for a permutation of a given length (n). It takes two non-negative integers, n and k, as input and returns two values. If k is odd or exceeds the maximum possible Manhattan value for the given n, the function returns (0, 0). Otherwise, it returns the original input values (n, k).

#State of the program right berfore the function call: l is a list of distinct integers from 1 to n in arbitrary order, where n is the length of the list.
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: Output State: The list l remains unchanged, still containing distinct integers from 1 to n in arbitrary order, where n is the length of the list, and the numbers from 1 to n have been printed in arbitrary order, separated by spaces, followed by 'YES'.
    print()
    #This is printed: a sequence of numbers from 1 to n, in arbitrary order, separated by spaces, followed by 'YES' (where n is the length of the list l)
    return
    #The program returns nothing, as there is no explicit return statement, and the list l remains unchanged, still containing distinct integers from 1 to n in arbitrary order, where n is the length of the list, and the numbers from 1 to n have been printed in arbitrary order, separated by spaces, followed by 'YES'.

#Overall this is what the function does:Prints the input list of distinct integers from 1 to n in arbitrary order, separated by spaces, followed by 'YES', without modifying the original list.

#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer.
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing because there is no value or variable specified in the return statement. The current state of the program remains unchanged, with 'n' being 0 and 'NO' being printed. The values of 'n' and 'k' returned by the function 'func_4()' are not affected by this empty return statement.
    #State: *`n` and `k` are returned by the function `func_4()`, and `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns the return value of func_1(n, k), where n is not equal to 0 and n and k are returned by the function func_4().

#Overall this is what the function does:This function determines whether a certain condition is met based on the values of `n` and `k` returned by `func_4()`. If `n` is 0, it prints 'NO' and returns without modifying the state of the program. If `n` is not 0, it calls `func_1(n, k)` and `func_5(l)`, and returns the value returned by `func_1(n, k)`.

