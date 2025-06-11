#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as input in the stdin, separated by spaces.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(input())
    #The program returns an integer that was provided as input through stdin.

#Overall this is what the function does:The function reads an integer from standard input and returns it as an integer value, effectively passing the input through without modification.

#State of the program right berfore the function call: stdin contains one input: a sequence of space-separated integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of space-separated integers from the standard input, converted to integers.

#Overall this is what the function does:Reads a sequence of space-separated integers from standard input and returns a map object containing the integers.

#State of the program right berfore the function call: stdin contains one input: a string
    return input().strip()
    #The program returns a string that was provided as input, with leading and trailing whitespace removed.

#Overall this is what the function does:The function reads a string from standard input, removes leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4
    n, k = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        
        v = func_2()
        
        if v == n:
            v = i
            break
        
    #State: Output State: n and k are positive integers such that 1 <= k <= n <= 10^4, v is the smallest integer i such that i * n >= n, or 1 if no such i exists.
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
        
    #State: Output State: The loop has executed all iterations, and the output state is the same as the initial state, with the variables n and k remaining unchanged. The loop has printed a series of queries in the format '? l i * v' and possibly a final answer in the format '! i * v', where l is a value between 1 and n (inclusive), i is a value between 1 and n // k (inclusive), and v is the smallest integer i such that i * n >= n, or 1 if no such i exists. The function func_2() has been called multiple times, but its effects are not specified in the given code.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing, as the return statement is empty. The variables n and k remain unchanged, and the function func_2() has been called multiple times, but its effects are not specified. The loop has printed a series of queries and possibly a final answer, and '! -1' is printed. The function func_2() has been called one more time.

#Overall this is what the function does:This function determines the smallest integer i such that i * n >= n, or 1 if no such i exists, and uses this value to print a series of queries in the format '? l i * v' and possibly a final answer in the format '! i * v'. If no answer is found, it prints '! -1'. The function also calls another function, func_2(), multiple times, but its effects are not specified. The input variables n and k remain unchanged throughout the function's execution.

