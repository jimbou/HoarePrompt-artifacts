#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were inputted by the user, separated by spaces.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns the list of integers.

#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(input())
    #The program returns an integer that was provided as input through stdin.

#Overall this is what the function does:The function reads an integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: The input contains a sequence of space-separated integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a result of converting a space-separated string from the input into an integer.

#Overall this is what the function does:The function takes a sequence of space-separated integers as input, converts each string into an integer, and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: stdin contains a string
    return input().strip()
    #The program returns a string that is the input from stdin with leading and trailing whitespace removed.

#Overall this is what the function does:The function reads a string from standard input, removes leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
    n, k = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        
        v = func_2()
        
        if v == n:
            v = i
            break
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `v` is either `n` or `1`, `i` is `1`.
    for i in range(1, n // k + 1):
        cnt, l = k, 1
        
        while cnt and l < n + 1:
            print(f'? {l} {i * v}', flush=True)
            l = func_2() + 1
            cnt -= 1
        
        if cnt == 0 and l == n + 1:
            print(f'! {i * v}', flush=True)
            func_2()
            return
        
    #State: n is a positive integer, k is a positive integer such that k <= n, v is either n or 1, i is n // k + 1, cnt is 0, l is n + 1, and the string "? l i * v" is printed k times where l ranges from 1 to n and v is either n or 1, and the string "! i * v" is printed where i is n // k + 1 and v is either n or 1.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing, as there is no explicit return statement with a value. The function seems to have completed its execution without returning any specific value or variable.

#Overall this is what the function does:The function takes no arguments and returns no value. It performs a series of print operations based on the values of `n` and `k`, which are obtained from another function `func_3()`. The function prints a sequence of strings in the format "? l i * v" and "! i * v" where `l` ranges from 1 to `n`, `i` ranges from 1 to `n // k + 1`, and `v` is either `n` or 1. The function also calls another function `func_2()` multiple times, but its purpose is not clear from the provided code. If a certain condition is met, the function prints "! -1" and returns without any explicit value.

