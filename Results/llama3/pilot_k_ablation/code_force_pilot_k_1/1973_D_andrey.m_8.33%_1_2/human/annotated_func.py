#State of the program right berfore the function call: l is a positive integer, x is a positive integer
    print(f'? {l} {x}')
    #This is printed: ? [l] [x] (where l is the value of l and x is the value of x)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns integer 'ret'

#Overall this is what the function does:The function prints the values of two positive integers 'l' and 'x' to the console, waits for user input, reads an integer from the input, and returns that integer.

#State of the program right berfore the function call: m is a positive integer.
    print(f'! {m}')
    #This is printed: ! [m] (where m is a positive integer)
    sys.stdout.flush()
    ret = int(input())

#Overall this is what the function does:Prints an exclamation mark followed by a positive integer m, waits for user input, and returns the input as an integer.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `max_val` is either 0 or the largest integer `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`, `stdin` contains no input.
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
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `max_val` is either 0 or the largest integer `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`, `stdin` contains no input. Either `func_2` has been called with an argument `m` such that `func_1(p + 1, m)` returns `n` for some `p`, or `func_2` has not been called and `max_val` is the largest integer `i` such that `func_1(1, i * n)` returns a value less than `n`.
    func_2(-1)

#Overall this is what the function does:This function takes two positive integers `n` and `k` as input, where `1 <= k <= n <= 10^4`, and performs the following actions:

#State of the program right berfore the function call: stdin contains one input: a positive integer t (1 <= t <= 10^3)
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `t` is 0, and the function `func_3()` has been called and executed `t` times.

#Overall this is what the function does:Reads a positive integer from standard input and calls the function `func_3()` that many times.

