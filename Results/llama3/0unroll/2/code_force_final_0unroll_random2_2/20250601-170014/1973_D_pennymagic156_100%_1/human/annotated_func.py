#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were in the space-separated list in stdin.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(input())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a list of integers, where each integer is a value from the input space-separated list of integers from stdin.

#Overall this is what the function does:The function reads a space-separated list of integers from standard input, converts each integer to an integer type, and returns a map object containing the list of integers.

#State of the program right berfore the function call: No precondition can be determined for this function as it only reads and returns input from the user without any specific constraints or expectations on the input format or content.
    return input().strip()
    #The program returns a string that is the user's input, stripped of leading and trailing whitespace.

#Overall this is what the function does:The function reads user input, removes leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
    n, k = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        
        v = func_2()
        
        if v == n:
            v = i
            break
        
    #State: Output State: n and k are positive integers such that 1 <= k <= n <= 10^4, v is the smallest integer i such that i * n >= n.
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
        
    #State: Output State: The loop will execute for a total of n // k iterations, and in each iteration, it will print n // k number of lines in the format '? l i * v' where l ranges from 1 to n // k + 1. After each iteration, it will print a line in the format '! i * v' and then call func_2() and return. The final output state will be the last printed line '! i * v' where i is the last value of the loop variable, which is n // k.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing, and the last printed line is '! -1'

#Overall this is what the function does:This function determines the smallest integer i such that i * n >= n, where n is a positive integer, and then iterates from 1 to n // k, printing lines in the format '? l i * v' and '! i * v' for each iteration. If the loop completes without finding a match, it prints '! -1' and returns without a value. The function performs a series of print statements and function calls, but does not modify or return any values.

