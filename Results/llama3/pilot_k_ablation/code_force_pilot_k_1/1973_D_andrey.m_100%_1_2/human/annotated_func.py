#State of the program right berfore the function call: l is a positive integer and x is a positive integer such that 1 <= l <= n and 1 <= x <= 10^9, where n is the length of the hidden array.
    print(f'? {l} {x}')
    #This is printed: ? [l] [x] (where l is a positive integer between 1 and n, and x is a positive integer between 1 and 10^9)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns the value of the variable 'ret', which is an integer.

#Overall this is what the function does:The function takes two positive integers, l and x, as input, where l is between 1 and n (the length of a hidden array) and x is between 1 and 10^9. It prints a query in the format '? l x' and waits for an integer response, which it then returns as the output.

#State of the program right berfore the function call: m is a positive integer
    print(f'! {m}')
    #This is printed: ! m (where m is a positive integer)
    sys.stdout.flush()
    ret = int(input())

#Overall this is what the function does:The function takes a positive integer `m` as input, prints an exclamation mark followed by the value of `m`, waits for user input, and returns the user's input as an integer.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `max_val` is the maximum value of `i` for which `func_1(1, i * n)` returns a value less than or equal to `n`, or 0 if no such `i` exists, `i` is 1, `r` is the return value of `func_1(1, 1 * n)`.
    for i in range(n // k, 0, -1):
        m = i * max_val
        
        p = 0
        
        for j in range(1, k + 1):
            if p >= n:
                p = 0
                break
            p = func_1(p + 1, m)
        
        if p == n:
            func_2(m)
            return
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `max_val` is the maximum value of `i` for which `func_1(1, i * n)` returns a value less than or equal to `n`, or 0 if no such `i` exists, `i` is 0, `r` is the return value of `func_1(1, 1 * n)`, `m` is 0, `j` is 1, and `p` is not equal to `n` and is the return value of `func_1(p + 1, m)` after `k` iterations. If `func_2(m)` was called, then `p` equals `n` and `m` equals `i * max_val` for some `i` in the range `[n // k, 0]`
    func_2(-1)

#Overall this is what the function does:This function takes two positive integers `n` and `k` as input, where `1 <= k <= n <= 10^4`, and performs the following actions:

#State of the program right berfore the function call: stdin contains one input: a positive integer t (1 <= t <= 10^3) representing the number of test cases.
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `_` is `t-1`, `t` is a positive integer between 1 and 10^3, and the function `func_3()` has been executed `t` times.

#Overall this is what the function does:Reads a positive integer t from standard input, representing the number of test cases, and executes the function func_3() t times.

