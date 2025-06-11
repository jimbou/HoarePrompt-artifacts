#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were inputted from stdin, separated by spaces.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns it as a list of integers.

#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(input())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:The function reads an integer from standard input and returns it without modification.

#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a list of integers, where each integer is a result of converting a string from the input into an integer. The input is a space-separated list of integers.

#Overall this is what the function does:The function reads a space-separated list of integers from standard input, converts each string into an integer, and returns a map object containing the list of integers.

#State of the program right berfore the function call: No precondition can be extracted from the function signature as it does not contain any parameters.
    return input().strip()
    #The program returns a string that is the user's input, stripped of leading and trailing whitespace.

#Overall this is what the function does:The function accepts no parameters and returns a string that is the user's input, stripped of leading and trailing whitespace.

#State of the program right berfore the function call: n is a positive integer and k is a positive integer such that 1 <= k <= n <= 10^4.
    n, k = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        
        v = func_2()
        
        if v == n:
            v = i
            break
        
    #State: Output State: n and k are positive integers such that 1 <= k <= n <= 10^4, v is n.
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
        
    #State: Output State: The loop will execute n // k iterations, and in each iteration, it will print a series of '?' queries with increasing values of l, until l reaches n + 1 or cnt becomes 0. If cnt becomes 0 and l reaches n + 1, it will print a '!' statement with the current value of i * v and then call func_2() before returning. The output state will be the final values of the variables after the loop has finished executing, which will be the last values printed by the '?' and '!' statements.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing, as the return statement is empty. The function func_2() has been called and returned, but its return value is not used. The values of other variables remain unchanged.

#Overall this is what the function does:This function takes no parameters and returns nothing. It prints a series of '?' queries to the console, then either prints a '!' statement with a calculated value and calls another function, or prints '! -1' if the loop completes without finding a match. The function's purpose is to interact with an external system through the printed queries and statements, with the final state being the last values printed to the console.

