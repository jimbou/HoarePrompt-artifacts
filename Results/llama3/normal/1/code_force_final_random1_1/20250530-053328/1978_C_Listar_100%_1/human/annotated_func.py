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
        
    #State: `l` is a list of integers from 1 to `n`, where `n` is a positive integer.

#Overall this is what the function does:This function takes two integers, n and k, as input and returns a list of integers from 1 to n. It modifies the list based on the value of k, potentially removing elements from the list through recursive calls to other functions (func_2 and func_3). The function returns the modified list, which may or may not be the original list of integers from 1 to n, depending on the value of k.

#State of the program right berfore the function call: c and k are non-negative integers, l is a list of integers, c and c+k are valid indices of the list l.
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns list l where the values at indices -c and -c - k have been swapped, c and c+k are valid indices of the list l.

#Overall this is what the function does:This function swaps the values at two specified indices in a given list and returns the modified list. It takes a list of integers and two non-negative integers as input, where the integers represent valid indices from the end of the list. The function exchanges the values at these indices and returns the updated list with the swapped values.

#State of the program right berfore the function call: c is a positive integer, l is a list of distinct integers from 1 to len(l) in arbitrary order, and c <= len(l).
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns a list of distinct integers from 1 to the length of the list, but with the elements at indices -c and c-1 swapped, where c is a positive integer.

#Overall this is what the function does:Swaps the elements at indices -c and c-1 in a list of distinct integers from 1 to the length of the list, where c is a positive integer, and returns the modified list.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, and n and k are the length of the permutation and the required Manhattan value, respectively.
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two values: the first value is 0, which is an integer, and the second value is also 0, which is also an integer.
    #State: *n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, and n and k are the length of the permutation and the required Manhattan value, respectively, and stdin contains a space-separated list of two integers. k is even.
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: *n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, and n and k are the length of the permutation and the required Manhattan value, respectively, and stdin contains a space-separated list of two integers. k is even. If n is odd, max_k is an integer equal to (n^2 - 1) // 2. If n is even, max_k is an integer equal to n^2 / 2.
    if (max_k < k) :
        return 0, 0
        #The program returns two values: 0 and 0. Both values are integers and are returned as a result of the program execution.
    #State: *n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, and n and k are the length of the permutation and the required Manhattan value, respectively, and stdin contains a space-separated list of two integers. k is even. If n is odd, max_k is an integer equal to (n^2 - 1) // 2. If n is even, max_k is an integer equal to n^2 / 2. max_k is larger than or equal to k.
    return n, k
    #The program returns two integers, n and k. n is the length of the permutation and is between 1 and 2 * 10^5 (inclusive), and k is the required Manhattan value and is between 0 and 10^12 (inclusive). Additionally, k is even, and the maximum possible Manhattan value (max_k) is larger than or equal to k. If n is odd, max_k is (n^2 - 1) // 2, and if n is even, max_k is n^2 / 2.

#Overall this is what the function does:This function determines whether a permutation of a given length can achieve a specified Manhattan value. It accepts two parameters, the length of the permutation (n) and the required Manhattan value (k), and returns two values. If k is odd or exceeds the maximum possible Manhattan value for the given n, the function returns 0, 0. Otherwise, it returns the original n and k values, indicating that a permutation of length n can achieve a Manhattan value of k.

#State of the program right berfore the function call: l is a list of integers
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: 'YES' is being printed, and all the integers in the list `l` are being printed.
    print()
    #This is printed: YES, followed by all the integers in the list l
    return
    #The program returns nothing.

#Overall this is what the function does:Prints 'YES' followed by all integers in the input list and returns nothing.

#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, and they are the output of function func_4().
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, as there is no return statement with a value. The current state of the program remains unchanged, with 'n' being 0 and 'NO' being printed. The values of 'n' and 'k' are still within their defined ranges, but they are not being returned or used in any way.
    #State: *`n` is an integer such that 1 <= n <= 2 * 10^5, `k` is an integer such that 0 <= k <= 10^12, and they are the output of function func_4(). Additionally, `n` is not equal to 0.
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns nothing, as there is no return statement with a value. The program simply ends without producing any output.

#Overall this is what the function does:This function takes no arguments and returns no value. It first checks the value of 'n' returned by function func_4(). If 'n' is 0, it prints 'NO' and ends. If 'n' is not 0, it calls function func_1() with 'n' and 'k' as arguments, assigns the result to 'l', and then calls function func_5() with 'l' as an argument, without producing any output.

