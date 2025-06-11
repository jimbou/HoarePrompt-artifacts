#State of the program right berfore the function call: l is a positive integer, x is a positive integer.
    print(f'? {l} {x}')
    #This is printed: ? [l] [x] (where l and x are the values of l and x respectively)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns the integer 'ret'.

#Overall this is what the function does:The function takes two positive integers, l and x, as input, prints them to the console, waits for user input, and returns the user's input as an integer.

#State of the program right berfore the function call: m is a positive integer
    print(f'! {m}')
    #This is printed: ! [m] (where m is a positive integer)
    sys.stdout.flush()
    ret = int(input())

#Overall this is what the function does:Prints an exclamation mark followed by a positive integer m, waits for user input, and returns the user's input as an integer.

#State of the program right berfore the function call: n and k are positive integers, n is the length of the hidden array and k is the number of subarrays in the desired split.
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: n is a positive integer, k is a positive integer, max_val is the maximum value of i such that func_1(1, i * n) returns a value less than or equal to n.
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
        
    #State: n is a positive integer greater than or equal to k, k is a positive integer greater than 0, i is 0, max_val is the maximum value of i such that func_1(1, i * n) returns a value less than or equal to n, m is 0, j is k, and p is 0.
    func_2(-1)

#Overall this is what the function does:This function takes two positive integers n and k as input, where n is the length of a hidden array and k is the number of subarrays in the desired split. It attempts to find the maximum value of i such that func_1(1, i * n) returns a value less than or equal to n, and then uses this value to find a suitable subarray size m. If a suitable m is found, the function calls func_2(m) and returns. If no suitable m is found, the function calls func_2(-1). The function's purpose is to perform a specific operation on the hidden array based on the input parameters n and k, and it affects the input variables by potentially modifying the hidden array.

#State of the program right berfore the function call: stdin contains one input: a positive integer (t) representing the number of test cases.
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `t` is a positive integer that must be greater than or equal to 0, stdin is empty, _ is `t-1`, and a function named func_3 has been called and executed `t` times.

#Overall this is what the function does:Reads a positive integer from standard input, representing the number of test cases, and calls a function named func_3 that number of times.

