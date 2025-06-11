#State of the program right berfore the function call: l is a positive integer, x is a positive integer
    print(f'? {l} {x}')
    #This is printed: ? [l] [x] (where l and x are positive integers)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns the integer 'ret'.

#Overall this is what the function does:The function prints a message to the console in the format '? [l] [x]' where l and x are positive integers, waits for user input, and returns the input as an integer.

#State of the program right berfore the function call: m is a positive integer representing the largest value that can be obtained by splitting the array into exactly k subarrays such that all subarrays have the product of their length and their maximum equal to m.
    print(f'! {m}')
    #This is printed: ! m (where m is the largest value that can be obtained by splitting the array into exactly k subarrays such that all subarrays have the product of their length and their maximum equal to m)
    sys.stdout.flush()
    ret = int(input())

#Overall this is what the function does:The function reads the largest value that can be obtained by splitting an array into exactly k subarrays such that all subarrays have the product of their length and their maximum equal to m from user input and returns it as an integer.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `max_val` is either 0 or the largest `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`, `i` is 0, `r` is the return value of `func_1(1, 1 * n)`.
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
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `max_val` is either 0 or the largest `i` such that `func_1(1, i * n)` returns a value less than or equal to `n`, `i` is 0, `r` is the return value of `func_1(1, 1 * n)`, and either `func_2(m)` has been called with `m` being the largest `i * max_val` such that `p` equals `n` after the inner loop, or `func_2` has not been called if no such `m` exists.
    func_2(-1)

#Overall this is what the function does:This function takes two positive integers `n` and `k` as input, where `1 <= k <= n <= 10^4`, and attempts to find the largest value `m` such that a certain condition is met. It iterates through possible values of `m` in descending order, checking if a specific inner loop results in a value `p` equal to `n`. If such an `m` is found, the function calls `func_2(m)` and returns. If no such `m` is found, the function calls `func_2(-1)`. The function does not return any value, but instead relies on the side effects of calling `func_2` with either a valid `m` or -1.

#State of the program right berfore the function call: stdin contains one input: a positive integer t (1 <= t <= 10^3)
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `_` is `t-1`, `t` is a positive integer between 1 and 10^3, and the function `func_3()` has been called `t` times.

#Overall this is what the function does:Reads a positive integer t from standard input and calls the function func_3() t times.

