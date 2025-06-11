#State of the program right berfore the function call: l is a positive integer, x is a positive integer
    print(f'? {l} {x}')
    #This is printed: ? l x (where l is a positive integer and x is a positive integer)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns an integer value stored in the variable 'ret'.

#Overall this is what the function does:The function takes two positive integers, l and x, as input, prints them to the console, waits for user input, and returns the integer value entered by the user.

#State of the program right berfore the function call: m is a positive integer
    print(f'! {m}')
    #This is printed: ! [m] (where m is a positive integer)
    sys.stdout.flush()
    ret = int(input())

#Overall this is what the function does:Prints an exclamation mark followed by a positive integer `m` to the console, waits for user input, and returns the input as an integer.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: Output State: n is a positive integer such that 1 <= n <= 10^4, k is a positive integer such that 1 <= k <= n, max_val is a positive integer such that 1 <= max_val <= n, stdin is empty
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
        
    #State: Output State: n is a positive integer such that 1 <= n <= 10^4, k is a positive integer such that 1 <= k <= n, max_val is a positive integer such that 1 <= max_val <= n, stdin is empty, i is an integer such that 0 <= i < n // k, m is an integer such that 0 <= m < max_val * n // k, p is an integer such that 0 <= p < n.
    func_2(-1)

#Overall this is what the function does:This function takes two positive integers n and k as input, where 1 <= k <= n <= 10^4, and attempts to find a value m such that a sequence of k operations, each incrementing a counter by m, will result in a final value of n. If such a value is found, the function calls another function func_2 with the value m. If no such value is found, the function calls func_2 with the value -1. The function modifies the input variables n and k, and also uses the standard input, which is expected to be empty at the end of the function's execution.

#State of the program right berfore the function call: stdin contains one input: a positive integer t.
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: The value of `t` is 0, stdin contains no input.

#Overall this is what the function does:Reads a positive integer from standard input and executes a loop that calls another function (func_3) a number of times equal to the input integer, until the input is exhausted.

