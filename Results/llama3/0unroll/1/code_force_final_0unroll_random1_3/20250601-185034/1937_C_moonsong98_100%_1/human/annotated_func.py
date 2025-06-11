#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the secret sequence p.
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? a b c d (where a, b, c, and d are non-negative integers less than the length of the secret sequence p)
    sys.stdout.flush()
    return input().strip()
    #The program returns a string that is the user's input, which is expected to be a guess for the secret sequence p, and this input is stripped of any leading or trailing whitespace.

#Overall this is what the function does:The function prompts the user to guess a secret sequence by printing a query with four non-negative integers (a, b, c, and d) less than the length of the secret sequence, waits for the user's input, and returns the input as a string stripped of leading and trailing whitespace, which is expected to be the user's guess for the secret sequence.

#State of the program right berfore the function call: a and b are non-negative integers such that 0 <= a, b < n, where n is the length of the secret sequence p.
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where a and b are non-negative integers less than the length of the secret sequence p)
    sys.stdout.flush()

#Overall this is what the function does:Prints the values of two non-negative integers a and b, which are less than the length of a secret sequence p, to the standard output in the format "! [a] [b]", and then flushes the output buffer to ensure the output is displayed immediately.

#State of the program right berfore the function call: n is a positive integer greater than or equal to 2.
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns nothing, as the return statement is empty, and no value or variable is being returned. The state of the program remains unchanged, with n still equal to 2, stdin containing no input, and the function func_2 having been called with arguments 0 and 1.
    #State: *n is an integer, stdin contains no input, and n is not equal to 2
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: Output State: `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `n` remains unchanged.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: Output State: `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `n` remains unchanged, `min_indices` is a list containing all the indices `i` for which `func_1(max_index, min_indices[0], max_index, i)` returns '=' or '<'.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: Output State: `min_index` is the smallest index `i` in `min_indices` for which `func_1(min_index, min_index, min_index, i)` returns '='.
    func_2(max_index, min_index)

#Overall this is what the function does:This function takes a positive integer n as input and performs a series of operations using two external functions, func_1 and func_2. If n is 2, it calls func_2 with arguments 0 and 1 and returns without changing the state of the program. If n is greater than 2, it iterates through the range of n to find the maximum index i for which func_1 returns '<', and then finds all indices i for which func_1 returns '=' or '<' with respect to the maximum index. It then finds the smallest index i among these that returns '=' when compared to itself using func_1. Finally, it calls func_2 with the maximum index and the smallest index as arguments, without returning any value or changing the state of the program.

