#State of the program right berfore the function call: stdin contains three inputs: first two integers n and k separated by a space, then a list of n integers separated by a space, and finally n integers separated by a space. n and k are positive integers, and the list of n integers are non-negative integers.
    try:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = [0] * (n + 1)
        for i in range(n):
            x = int(input())
            
            b[abs(x)] += a[i]
            
        #State: n and k are positive integers, a is a list of n non-negative integers, b is a list of n+1 integers where the value at each index i is the sum of the absolute values of the input integers that correspond to the non-negative integers in a at index i, stdin is empty.
        r = 0
        for i in range(1, n + 1):
            r += k
            
            if r < b[i]:
                print('NO')
                return
            
            r -= b[i]
            
        #State: `n` is a positive integer, `k` is a positive integer, `a` is a list of `n` non-negative integers, `b` is a list of `n+1` integers where the value at each index `i` is the sum of the absolute values of the input integers that correspond to the non-negative integers in `a` at index `i`, `r` is `k` if `n` is 0, otherwise `r` is `k` minus the sum of the absolute values of the input integers that correspond to the non-negative integers in `a` at index `n`, `i` is `n+1`, stdin is empty, and either the program has printed 'NO' and terminated or `r` is greater than or equal to `b[i]` for all `i` from 1 to `n`.
    except (ValueError):
        print('Invalid input format')
        #This is printed: Invalid input format
    #State: `n` and `k` are positive integers, `a` is a list of `n` non-negative integers, `b` is a list of `n+1` integers where the value at each index `i` is the sum of the absolute values of the input integers that correspond to the non-negative integers in `a` at index `i`, `r` is `k` if `n` is 0, otherwise `r` is `k` minus the sum of the absolute values of the input integers that correspond to the non-negative integers in `a` at index `n`, `i` is `n+1`, stdin is empty, and either the program has printed 'NO' and terminated or `r` is greater than or equal to `b[i]` for all `i` from 1 to `n`. If a `ValueError` occurs, the program prints 'Invalid input format'.

#Overall this is what the function does:This function reads input from stdin, expecting three inputs: two positive integers n and k, a list of n non-negative integers, and n integers. It then calculates the sum of the absolute values of the input integers corresponding to each non-negative integer in the list. If the sum of these absolute values exceeds k at any point, it prints 'NO' and terminates. If all sums are less than or equal to k, it continues to the end. If the input format is invalid, it prints 'Invalid input format'. The function does not return any value, but its execution results in either printing 'NO' or 'Invalid input format', or silently terminating if all conditions are met.

#State of the program right berfore the function call: stdin contains one input: an integer (t) representing the number of test cases.
    try:
        t = int(input())
        for _ in range(t):
            func_1()
            
        #State: `t` is an integer representing the number of test cases, and the function `func_1()` has been executed `t` times.
    except (ValueError):
        print('Invalid input format')
        #This is printed: Invalid input format
    #State: `t` is an integer representing the number of test cases. If the input is not an integer, the program prints 'Invalid input format', otherwise, the function `func_1()` has been executed `t` times.

#Overall this is what the function does:This function reads an integer from standard input, representing the number of test cases, and attempts to execute another function (`func_1`) that many times. If the input is not a valid integer, it prints an error message ('Invalid input format').

