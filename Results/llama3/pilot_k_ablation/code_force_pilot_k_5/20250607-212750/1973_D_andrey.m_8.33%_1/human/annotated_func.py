#State of the program right berfore the function call: l is a positive integer, x is a positive integer less than or equal to 10^9.
    print(f'? {l} {x}')
    #This is printed: ? <value of l> <value of x> (where <value of l> is a positive integer and <value of x> is a positive integer less than or equal to 10^9)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns an integer value stored in the variable 'ret'.

#Overall this is what the function does:The function takes two positive integers, l and x, as input, prints them to the console in the format '? l x', waits for user input, and returns the user's input as an integer.

#State of the program right berfore the function call: m is a positive integer representing the largest value m such that there exists a sequence c_1, \ldots, c_{k-1} such that 1 \leq c_1 < \ldots < c_{k-1} < n and f(1, c_1) = f(c_1 + 1, c_2) = \ldots = f(c_{k-1}+1, n) = m
    print(f'! {m}')
    #This is printed: ! [m] (where m is the largest value m such that there exists a sequence c_1, ..., c_{k-1} satisfying the given conditions)
    sys.stdout.flush()
    ret = int(input())

#Overall this is what the function does:Prints the largest value m such that there exists a sequence c_1, ..., c_{k-1} satisfying the given conditions, and then reads and returns an integer input from the user.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: `n` is at least 1, `i` is equal to 0, `k` is a positive integer, `stdin` is empty, `max_val` is either 0 or the largest integer `i` such that `func_1(1, i * n)` is less than or equal to `n`.
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
        
    #State: `n` is at least `k`, `k` is a positive integer and at most `n`, `i` is equal to 0, `max_val` is either 0 or the largest integer `i` such that `func_1(1, i * n)` is less than or equal to `n`, `m` is 0, `j` is equal to `k`, and `p` is equal to `func_1(p + 1, m)` (with `k` iterations of `func_1`).
    func_2(-1)

#Overall this is what the function does:This function takes two positive integers n and k as input, where 1 <= k <= n <= 10^4, and performs the following actions:

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `t` is an integer greater than or equal to 0, `_` is `t-1`, and the function `func_3()` has been executed `t` times.

#Overall this is what the function does:Reads an integer from standard input and executes the function `func_3()` that many times.

