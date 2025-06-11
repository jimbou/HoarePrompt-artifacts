#State of the program right berfore the function call: l is a positive integer, x is a positive integer such that 1 <= l <= n and 1 <= x <= 10^9.
    print(f'? {l} {x}')
    #This is printed: ? [l] [x] (where l is a positive integer and x is a positive integer)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns an integer 'ret'.

#Overall this is what the function does:The function takes two positive integers, l and x, as input, prints a query in the format '? l x', waits for user input, and returns the user's response as an integer.

#State of the program right berfore the function call: m is a positive integer
    print(f'! {m}')
    #This is printed: ! [m] (where m is a positive integer)
    sys.stdout.flush()
    ret = int(input())

#Overall this is what the function does:Prints a message to the console indicating the start of a factorial calculation for a given positive integer m, waits for user input, and returns the user's input as an integer.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `max_val` is the maximum value of `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`, or 0 if no such `i` exists.
    for i in range(n // k, 0, -1):
        m = i * max_val
        
        p = 0
        
        for j in range(1, k + 1):
            p = func_1(p + 1, m)
            if p >= n:
                break
        
        if p == n:
            func_2(m)
            return
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `max_val` is the maximum value of `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`, or 0 if no such `i` exists, `i` is 0, `m` is 0, `p` is either `n` or 0, `j` is 1. If `p` is `n`, `func_2(m)` has been called with `m` as an argument. If `n` is less than `k`, the loop does not execute and `p` is 0.
    func_2(-1)

#Overall this is what the function does:This function determines the maximum value of `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`, and then uses this value to find a suitable `m` that satisfies a certain condition involving `func_1` and `n`. If such an `m` is found, it calls `func_2(m)`. If no such `m` is found, it calls `func_2(-1)`. The function takes two positive integers `n` and `k` as input, where `1 <= k <= n <= 10^4`, and does not return any value.

#State of the program right berfore the function call: stdin contains one input: a positive integer t (1 <= t <= 10^3)
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `t` is 0, stdin is empty, and the function `func_3()` has been called `t` times.

#Overall this is what the function does:Reads a positive integer from standard input, then calls the function `func_3()` that many times, leaving the input stream empty.

