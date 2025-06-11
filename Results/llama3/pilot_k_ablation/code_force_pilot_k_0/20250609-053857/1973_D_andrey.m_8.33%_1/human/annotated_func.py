#State of the program right berfore the function call: l is a positive integer and x is a positive integer such that 1 <= l <= n and 1 <= x <= 10^9, where n is the length of the hidden array.
    print(f'? {l} {x}')
    #This is printed: ? [l] [x] (where l is a positive integer between 1 and n, and x is a positive integer between 1 and 10^9)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns the integer ret.

#Overall this is what the function does:The function takes two positive integers, `l` and `x`, as input, where `l` is between 1 and `n` (the length of a hidden array) and `x` is between 1 and 10^9. It prints a query in the format `? l x`, waits for a response, and returns the received integer response as output.

#State of the program right berfore the function call: m is a positive integer.
    print(f'! {m}')
    #This is printed: ! m (where m is a positive integer)
    sys.stdout.flush()
    ret = int(input())

#Overall this is what the function does:Prints a message to the console indicating that the factorial of a positive integer m is about to be calculated, waits for the user to input an integer, and returns the user's input as an integer.

#State of the program right berfore the function call: n and k are positive integers, n is the length of the hidden array and k is the number of subarrays in the desired split.
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: Output State: n is a positive integer, k is a positive integer, max_val is n, stdin is empty
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
        
    #State: Output State: n is a positive integer, k is a positive integer, max_val is n, stdin is empty, i is 0, m is 0, p is 0
    func_2(-1)

#Overall this is what the function does:Splits an array of length n into k subarrays and returns the maximum size of the subarrays if the split is possible, otherwise returns -1.

#State of the program right berfore the function call: stdin contains one input: a positive integer t, where 1 <= t <= 10^3
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: The loop has executed `t` times, where `t` is a positive integer between 1 and 10^3 (inclusive), and `func_3()` has been called `t` times. The state of other variables remains unchanged.

#Overall this is what the function does:Reads a positive integer t from standard input and calls the function func_3() t times, without modifying any other variables or returning any value.

