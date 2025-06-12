#State of the program right berfore the function call: l is a positive integer, x is a positive integer.
    print(f'? {l} {x}')
    #This is printed: ? [l] [x] (where l is the value of l and x is the value of x)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns an integer value stored in the variable 'ret'.

#Overall this is what the function does:The function takes two positive integers l and x as input, prints their values, waits for user input, and returns the integer value entered by the user.

#State of the program right berfore the function call: m is a positive integer
    print(f'! {m}')
    #This is printed: ! m (where m is a positive integer)
    sys.stdout.flush()
    ret = int(input())

#Overall this is what the function does:Prints a message to the console indicating that the factorial of a positive integer m is about to be calculated, waits for user input, and returns the user's input as an integer.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: `n` is a positive integer, `k` is a positive integer such that 1 <= k <= n <= 10^4, `max_val` is the largest integer `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`, `i` is 0, and `r` is the return value of `func_1(1, max_val * n)`
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
        
    #State: `n` is a positive integer, `k` is a positive integer such that 1 <= k <= n <= 10^4, `max_val` is the largest integer `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`, `i` is 0, `r` is the return value of `func_1(1, max_val * n)`, `m` is 0, `p` is not defined, `j` is not defined. If `func_2` was called, then the loop finished executing and `m` is the value that was passed to `func_2`, otherwise the loop did not finish executing.
    func_2(-1)

#Overall this is what the function does:This function takes two positive integers `n` and `k` as input, where `1 <= k <= n <= 10^4`, and attempts to find the largest integer `m` such that `func_1` returns a value less than or equal to `n` when called with `m` as an argument. If such an `m` is found, the function calls `func_2` with `m` as an argument. If no such `m` is found, the function calls `func_2` with `-1` as an argument. The function does not return any value.

#State of the program right berfore the function call: stdin contains one input: a positive integer t, which is the number of test cases.
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `t` is 0, `func_3` has been called and executed `t` times.

#Overall this is what the function does:Reads a positive integer t from standard input, representing the number of test cases, and calls the function func_3() t times.

