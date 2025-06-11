#State of the program right berfore the function call: l is a positive integer, x is a positive integer such that 1 <= l <= n and 1 <= x <= 10^9, where n is the length of the hidden array.
    print(f'? {l} {x}')
    #This is printed: ? [l] [x] (where l and x are the values of the variables l and x, respectively)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns the value of variable 'ret' which is an integer.

#Overall this is what the function does:The function takes two positive integers `l` and `x` as input, prints a query in the format `? l x`, waits for an integer response, and returns the received integer value.

#State of the program right berfore the function call: m is a positive integer
    print(f'! {m}')
    #This is printed: ! [m] (where m is the value of the positive integer m)
    sys.stdout.flush()
    ret = int(input())

#Overall this is what the function does:Prints a message to the console indicating that the factorial of a positive integer m is being calculated, waits for user input, and returns the user's input as an integer.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: n and k are positive integers such that 1 <= k <= n <= 10^4, max_val is either 0 or the largest integer i such that func_1(1, i * n) <= n, i is 0, r is the return value of func_1(1, 0 * n) and is either less than or equal to n or greater than n, stdin contains no input.
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
        
    #State: `n` is greater than or equal to `k`, `k` is a positive integer, `i` is 0, `max_val` is either 0 or the largest integer `i` such that `func_1(1, i * n)` <= `n`, `r` is the return value of `func_1(1, 0 * n)` and is either less than or equal to `n` or greater than `n`, `m` is 0, `j` is `k`, `p` is the return value of `func_1(p + 1, m)` which is either less than or equal to `n` or greater than `n`.
    func_2(-1)

#Overall this is what the function does:This function takes two positive integers n and k as input, where 1 <= k <= n <= 10^4, and attempts to find the largest integer m such that func_1(p + 1, m) equals n for some p. If such an m is found, the function calls func_2(m). If no such m is found, the function calls func_2(-1).

#State of the program right berfore the function call: stdin contains one input: a positive integer t (1 <= t <= 10^3) representing the number of test cases.
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `t` is a positive integer between 1 and 10^3 (inclusive), stdin is empty, `_` is `t-1`, and a function `func_3()` has been called and executed `t` times.

#Overall this is what the function does:Reads a positive integer t from standard input, representing the number of test cases, and calls the function func_3() t times.

