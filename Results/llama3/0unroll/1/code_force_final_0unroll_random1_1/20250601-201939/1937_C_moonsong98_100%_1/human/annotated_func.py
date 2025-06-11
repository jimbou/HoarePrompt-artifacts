#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the number of elements in the secret sequence p.
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are integers within the range 0 <= a, b, c, d < n)
    sys.stdout.flush()
    return input().strip()
    #The program returns a string that is the user's input, which is a response to the printed string "? a b c d" where a, b, c, and d are the values of the variables a, b, c, and d respectively, and the input has been stripped of leading and trailing whitespace.

#Overall this is what the function does:The function takes four integers a, b, c, and d as input, prints a string in the format "? a b c d" to the console, waits for user input, and returns the user's input as a string after removing leading and trailing whitespace.

#State of the program right berfore the function call: a and b are non-negative integers such that 0 <= a < n and 0 <= b < n, where n is the number of elements in the secret sequence p.
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where a and b are non-negative integers less than the number of elements in the secret sequence p)
    sys.stdout.flush()

#Overall this is what the function does:Prints the values of two non-negative integers, a and b, to the console, separated by a space, and flushes the output buffer to ensure the output is displayed immediately.

#State of the program right berfore the function call: n is a positive integer greater than or equal to 2
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns nothing
    #State: *`n` is an integer larger than or equal to 2, `n` is not equal to 2, stdin contains no input
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: Output State: `n` is an integer larger than or equal to 2, `n` is not equal to 2, `max_index` is `n-1`, stdin contains no input.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: Output State: `min_indices` is a list containing all indices `i` in the range `[0, n)` for which `func_1(max_index, i, max_index, i)` returns `=`.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: Output State: `min_indices` is a list containing all indices `i` in the range `[0, n)` for which `func_1(max_index, i, max_index, i)` returns `=`, `min_index` is the first index in `min_indices` for which `func_1(min_index, min_index, min_index, i)` returns `=`.
    func_2(max_index, min_index)

#Overall this is what the function does:The function takes a positive integer n greater than or equal to 2 as input and performs the following actions:

