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
        
    #State: The loop terminates when `i` is -1, at which point `k` is 0 and the list `l` is a rotated version of the original list, with the last `n - k` elements moved to the beginning of the list.

#Overall this is what the function does:Rotates a list of integers from 1 to n by moving the last k elements to the beginning of the list, where n is a positive integer and k is a non-negative integer. The function returns the rotated list. If k is 0, the original list is returned.

#State of the program right berfore the function call: n and k are non-negative integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12.
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two values: the first value is 0, and the second value is also 0. Both values are integers.
    #State: *`n` is a non-negative integer such that 1 <= n <= 2 * 10^5, `k` is a non-negative integer such that 0 <= k <= 10^12, stdin contains no input. k is an even number
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *`n` is a non-negative integer such that 1 <= n <= 2 * 10^5, `k` is a non-negative integer such that 0 <= k <= 10^12, stdin contains no input. If `n` is odd, `max_k` is a non-negative integer such that 0 <= max_k <= 2 * 10^10. If `n` is even, `max_k` is an integer such that 0.5 * n^2 <= max_k <= 2 * 10^10.
    if (max_k < k) :
        return 0, 0
        #The program returns two values: the first value is 0, which is an integer, and the second value is also 0, which is an integer.
    #State: *`n` is a non-negative integer such that 1 <= n <= 2 * 10^5, `k` is a non-negative integer such that 0 <= k <= 10^12, stdin contains no input. If `n` is odd, `max_k` is a non-negative integer such that 0 <= max_k <= 2 * 10^10. If `n` is even, `max_k` is an integer such that 0.5 * n^2 <= max_k <= 2 * 10^10. Additionally, `max_k` is greater than or equal to `k`.
    return n, k
    #The program returns a tuple containing two values: `n` and `k`. `n` is a non-negative integer between 1 and 2 * 10^5 (inclusive), and `k` is a non-negative integer between 0 and 10^12 (inclusive). Additionally, if `n` is odd, `k` is less than or equal to `max_k`, which is a non-negative integer between 0 and 2 * 10^10 (inclusive). If `n` is even, `k` is less than or equal to `max_k`, which is an integer between 0.5 * n^2 and 2 * 10^10 (inclusive).

#Overall this is what the function does:This function takes two non-negative integers `n` and `k` as input, where `1 <= n <= 2 * 10^5` and `0 <= k <= 10^12`. It checks if `k` is even, and if so, it calculates a maximum value `max_k` based on `n`. If `k` is greater than `max_k`, the function returns `(0, 0)`. Otherwise, it returns the original values of `n` and `k`. If `k` is odd, the function immediately returns `(0, 0)`. The function effectively filters out cases where `k` is odd or exceeds the calculated `max_k` for a given `n`, and returns the original values only when `k` is even and within the valid range.

#State of the program right berfore the function call: l is a list of distinct integers from 1 to n in arbitrary order, where n is the length of the list.
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: l is a list of distinct integers from 1 to n in arbitrary order, where n is the length of the list, 'YES' is being printed, i is the last integer in the list, and the last integer in the list which is [i] is being printed, and all integers in the list have been printed
    print()
    #This is printed: Nothing
    return
    #The program returns nothing because the return statement is empty. The list 'l' remains unchanged, containing distinct integers from 1 to n in arbitrary order, where n is the length of the list. The string 'YES' has been printed, the last integer in the list 'i' has been printed, and all integers in the list have been printed, followed by a new line.

#Overall this is what the function does:Prints 'YES' followed by the elements of the input list 'l' in their original order, separated by spaces, and then a new line, without modifying the list.

#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer.
    n, k = func_2()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing because there is no return value specified in the return statement. The current state of the program remains unchanged, with 'n' being 0 and 'NO' being printed. The values of 'n' and 'k' returned by func_2() are not utilized in this code snippet.
    #State: *`n` and `k` are returned by `func_2()`, `n` is a positive integer and not equal to 0, `k` is a non-negative integer
    l = func_1(n, k)
    func_3(l)
    return
    #The program returns the value of l, which is the value returned by func_1(n, k), where n is a positive integer and not equal to 0, and k is a non-negative integer.

#Overall this is what the function does:This function takes no parameters and returns either nothing or a value. If the positive integer 'n' returned by func_2() is 0, it prints 'NO' and returns nothing. Otherwise, it calls func_1() with 'n' and non-negative integer 'k' as arguments, passes the result to func_3(), and returns the value returned by func_1().

