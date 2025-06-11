#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as input in stdin, separated by spaces.

#Overall this is what the function does:The function reads a line of input from stdin, splits it into space-separated integers, and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains one input: an integer
    return int(input())
    #The program returns an integer that was provided as input from stdin

#Overall this is what the function does:Reads an integer from standard input and returns it as output.

#State of the program right berfore the function call: The input is a string of space-separated integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a result of converting a space-separated string from the input into an integer.

#Overall this is what the function does:The function accepts a string of space-separated integers as input and returns a map object containing a sequence of integers, where each integer is the result of converting a space-separated string from the input into an integer.

#State of the program right berfore the function call: No precondition can be extracted from this function as it does not take any parameters. It reads a line from the standard input and returns it as a string after removing leading and trailing whitespaces.
    return input().strip()
    #The program returns a string that was read from the standard input, with leading and trailing whitespaces removed.

#Overall this is what the function does:Reads a line from the standard input, removes leading and trailing whitespaces, and returns the resulting string.

#State of the program right berfore the function call: n and k are positive integers, n is the length of a hidden array and k is the number of subarrays in the desired split.
    n, k = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        
        v = func_2()
        
        if v == n:
            v = i
            break
        
    #State: n is a positive integer, k is equal to n, i is equal to 0, and this is printed: "? 1 (0 * n)". If the returned value of func_2() is equal to n, then v is equal to 1. Otherwise, v is equal to the returned value of func_2().
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
        
    #State: cnt is equal to 0, l is equal to n + 1, i is equal to n // k, and the strings "? 1 i * v", "? 2 i * v", ..., "? n i * v" are printed.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing, as there is no value or variable specified in the return statement. The program has simply terminated without providing any output or result.

#Overall this is what the function does:This function takes no parameters and returns nothing. It prints a series of strings in the format "? a b" and "! c" to the console, where a, b, and c are integers. The function's purpose is to interact with an external entity (likely a game or a puzzle) by sending queries and receiving responses. The function's behavior is determined by the responses it receives from the external entity, and it may terminate early if certain conditions are met. In all cases, the function will eventually print "! -1" and terminate without providing any output or result.

