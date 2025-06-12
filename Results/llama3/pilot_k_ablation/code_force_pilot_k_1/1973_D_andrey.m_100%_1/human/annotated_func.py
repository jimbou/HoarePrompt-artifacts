#State of the program right berfore the function call: l is a positive integer, x is a positive integer such that 1 <= l <= n and 1 <= x <= 10^9, where n is the length of the hidden array.
    print(f'? {l} {x}')
    #This is printed: ? [l] [x] (where l is a positive integer and x is a positive integer)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns an integer 'ret'

#Overall this is what the function does:Queries the user with a message in the format '? [l] [x]' where 'l' and 'x' are positive integers, waits for an integer response, and returns the received integer value.

#State of the program right berfore the function call: m is a positive integer representing the largest value m such that there exists a sequence c_1, \ldots, c_{k-1} such that 1 \leq c_1 < \ldots < c_{k-1} < n and f(1, c_1) = f(c_1 + 1, c_2) = \ldots = f(c_{k-1}+1, n) = m, or -1 if no such m exists.
    print(f'! {m}')
    #This is printed: ! [m] (where m is the largest value m such that there exists a sequence c_1, \ldots, c_{k-1} satisfying certain conditions, or -1 if no such m exists)
    sys.stdout.flush()
    ret = int(input())

#Overall this is what the function does:Prints the largest value m such that there exists a sequence c_1, \ldots, c_{k-1} satisfying certain conditions, or -1 if no such m exists, and then reads an integer from standard input and returns it.

#State of the program right berfore the function call: n and k are positive integers, n is the length of the hidden array and k is the number of subarrays in the desired split.
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: `n` is a positive integer, `k` is a positive integer, `max_val` is the largest integer `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`, or 0 if no such `i` exists.
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
        
    #State: `n` is a positive integer, `k` is a positive integer, `max_val` is the largest integer `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`, or 0 if no such `i` exists, `i` is 0, `m` is 0, `j` is 1, `p` is either 0 if `p` was greater than or equal to `n` at any point during the loop, or the value returned by `func_1(p + 1, m)` after `k` iterations, and `p` is not equal to `n`. If `func_2(m)` was called, `m` is the value that made `p` equal to `n`
    func_2(-1)

#Overall this is what the function does:This function takes two positive integers `n` and `k` as input, where `n` is the length of a hidden array and `k` is the number of subarrays in the desired split. It attempts to find the largest integer `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`. If such an `i` exists, it then tries to find a value `m` that makes `p` equal to `n` after `k` iterations of `func_1(p + 1, m)`. If such an `m` is found, it calls `func_2(m)`. If no such `m` is found, it calls `func_2(-1)`. The function does not return any value.

#State of the program right berfore the function call: stdin contains one input: a positive integer (t) representing the number of test cases.
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `t` is a non-negative integer, the function `func_3()` has been executed `t` times.

#Overall this is what the function does:Reads a positive integer from standard input, representing the number of test cases, and executes the `func_3()` function that many times.

