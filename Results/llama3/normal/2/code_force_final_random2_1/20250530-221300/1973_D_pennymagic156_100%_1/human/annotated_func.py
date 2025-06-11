#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as input in the stdin, where each integer was separated by a space.

#Overall this is what the function does:The function reads a space-separated list of integers from standard input and returns it as a list of integers.

#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(input())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: stdin contains one input: a sequence of integers separated by spaces.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers separated by spaces from the standard input, where each integer is converted to an integer type.

#Overall this is what the function does:The function reads a sequence of integers separated by spaces from the standard input, converts each integer to an integer type, and returns a map object containing the converted integers.

#State of the program right berfore the function call: stdin contains a string
    return input().strip()
    #The program returns a string that was read from the standard input, with leading and trailing whitespace removed.

#Overall this is what the function does:Reads a string from standard input, removes leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 1 <= k <= n <= 10^4.
    n, k = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        
        v = func_2()
        
        if v == n:
            v = i
            break
        
    #State: v is returned with the value of func_2(), n and k are positive integers such that 1 <= k <= n <= 10^4, i is equal to 1, and this is printed: "? 1 [i * n]" where i is 1, and v is now returned with the value of func_2(). If v is equal to n, then v is equal to i, which is 1.
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
        
    #State: cnt is 0, l is n + 1, and the string "? 1 (i * v)" is printed k times, where i is the current value of i and v is the current value of v, repeated for each iteration of the loop, and the loop has iterated n // k times.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns None

#Overall this is what the function does:This function takes no parameters and returns None. It performs a series of print operations to the console, first printing a series of strings in the format "? 1 [i * n]" where i ranges from n to 1, and then printing a series of strings in the format "? l (i * v)" where l ranges from 1 to n and i ranges from 1 to n // k. If a certain condition is met, it prints a string in the format "! (i * v)" and calls another function. If the condition is not met, it prints "! -1" and calls another function. The function also calls another function at the beginning and end of its execution.

