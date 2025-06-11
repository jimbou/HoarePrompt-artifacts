#State of the program right berfore the function call: n is a positive integer, k is a non-negative integer
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
        
    #State: Output State: k is 0, l is a list of integers from 1 to n, c is n/2 + 1, n is a positive integer.

#Overall this is what the function does:This function takes a positive integer n and a non-negative integer k as input, and returns a list of integers from 1 to n. It modifies the list by removing elements based on the value of k, and returns the modified list when k becomes 0. The function also counts the number of iterations and uses this count to modify the list further. The final state of the program is a list of integers from 1 to n, with some elements possibly removed, and a count of iterations equal to n/2 + 1.

#State of the program right berfore the function call: c and k are non-negative integers, l is a list of distinct integers from 1 to n in arbitrary order, and c+k < len(l).
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns a list of distinct integers from 1 to n in arbitrary order, where the elements at indices -c and -c - k have been swapped, and c+k < len(l).

#Overall this is what the function does:This function swaps the elements at indices -c and -c - k in a list of distinct integers from 1 to n, where c and k are non-negative integers and c+k is less than the length of the list, and returns the modified list.

#State of the program right berfore the function call: c is a positive integer, l is a list of distinct integers from 1 to len(l) in arbitrary order, and 1 <= c <= len(l) // 2.
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns list l which contains distinct integers from 1 to len(l) in arbitrary order, where the elements at indices c - 1 and -c are swapped, and 1 <= c <= len(l) // 2

#Overall this is what the function does:This function swaps the elements at indices c-1 and -c in the input list l, where c is a positive integer between 1 and half the length of the list, and returns the modified list.

#State of the program right berfore the function call: n and k are non-negative integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two values: the first value is 0, and the second value is also 0. The value of `n` is still a non-negative integer between 1 and 2 * 10^5, and the value of `k` is still an odd non-negative integer between 0 and 10^12.
    #State: *`n` is a non-negative integer such that 1 <= n <= 2 * 10^5, `k` is a non-negative integer such that 0 <= k <= 10^12, stdin contains a space-separated list of two integers, and `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` is a non-negative integer such that 1 <= n <= 2 * 10^5, `k` is a non-negative integer such that 0 <= k <= 10^12, stdin contains a space-separated list of two integers, and `k` is even. If `n` is odd, `max_k` is an integer equal to (n^2 - 1) // 2. If `n` is even, `max_k` is an integer such that 0.5 * n^2 <= max_k <= 10^10.
    if (max_k < k) :
        return 0, 0
        #The program returns two values: the first value is 0, and the second value is also 0.
    #State: *`n` is a non-negative integer such that 1 <= n <= 2 * 10^5, `k` is a non-negative integer such that 0 <= k <= 10^12, stdin contains a space-separated list of two integers, and `k` is even. If `n` is odd, `max_k` is an integer equal to (n^2 - 1) // 2. If `n` is even, `max_k` is an integer such that 0.5 * n^2 <= max_k <= 10^10. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns a tuple containing two values: `n` and `k`. `n` is a non-negative integer between 1 and 2 * 10^5 (inclusive), and `k` is a non-negative integer between 0 and 10^12 (inclusive). Additionally, `k` is even.

#Overall this is what the function does:This function takes two non-negative integers, n and k, as input and returns either a tuple containing the original values of n and k if k is even and within a certain range determined by n, or a tuple containing two zeros if k is odd or exceeds the maximum allowed value for the given n.

#State of the program right berfore the function call: l is a list of distinct integers from 1 to n in arbitrary order, where n is the length of the list.
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: Output State: The list l remains unchanged, and 'YES' is still being printed, but the numbers from 1 to n are printed in the order they appear in the list, separated by spaces.
    print()
    #This is printed: YES (indicating that the list l remains unchanged), followed by the numbers from 1 to n in the order they appear in the list, separated by spaces
    return
    #The program returns nothing, as there is no explicit return statement. The list l remains unchanged, and 'YES' is still being printed, but the numbers from 1 to n are printed in the order they appear in the list, separated by spaces.

#Overall this is what the function does:The function takes a list of distinct integers from 1 to n as input, prints 'YES', and then prints the numbers from 1 to n in the order they appear in the list, separated by spaces. The function does not modify the input list and does not return any value.

#State of the program right berfore the function call: n and k are integers such that n > 0 and k >= 0.
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, 'n' is 0, 'k' is returned by func_4(), and 'NO' is printed
    #State: `n` and `k` are returned by `func_4()`, and `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns the return value of func_1(n, k), where n is not equal to 0 and n and k are returned by func_4().

#Overall this is what the function does:This function determines whether to print 'NO' and return nothing, or return the result of another function (`func_1`) based on the values of `n` and `k` obtained from `func_4`. If `n` is 0, it prints 'NO' and returns without a value. If `n` is not 0, it calls `func_5` with the result of `func_1(n, k)` and then returns the result of `func_1(n, k)`.

