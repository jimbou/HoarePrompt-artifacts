#State of the program right berfore the function call: l is a positive integer and x is a positive integer such that 1 <= l <= n and 1 <= x <= 10^9, where n is the length of the hidden array.
    print(f'? {l} {x}')
    #This is printed: ? 5 12345
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns the integer 'ret'

#Overall this is what the function does:The function takes two positive integers, `l` and `x`, as input, where `1 <= l <= n` and `1 <= x <= 10^9`, and returns an integer `ret` obtained from user input after printing a query string to the console.

#State of the program right berfore the function call: m is a positive integer
    print(f'! {m}')
    #This is printed: ! m (where m is a positive integer)
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
        
    #State: n and k are positive integers such that 1 <= k <= n <= 10^4, stdin is empty, i is 0, r is the value returned by func_1(1, 0 * n). If r is less than or equal to n, max_val is 0. Otherwise, max_val is the value of max_val before the loop started.
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
        
    #State: i is 0, m is 0, j is 1, p is 0.
    func_2(-1)

#Overall this is what the function does:This function takes two positive integers n and k as input, where 1 <= k <= n <= 10^4, and performs the following actions:

#State of the program right berfore the function call: stdin contains one input: a positive integer t (1 <= t <= 10^3).
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `_` is `t-1`, a function named `func_3` has been called `t` times and returned None, `t` is a positive integer between 1 and 10^3.

#Overall this is what the function does:Reads a positive integer t from standard input and calls a function named func_3 t times, without returning any value or modifying the input variable t.

