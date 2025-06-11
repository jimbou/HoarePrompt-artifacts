#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the number of elements in the secret sequence p.
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are non-negative integers less than the number of elements in the secret sequence p)
    sys.stdout.flush()
    return input().strip()
    #The program returns a string that is the next line of input from the user, with leading and trailing whitespace removed.

#Overall this is what the function does:The function takes no parameters and returns a string that is the next line of input from the user, with leading and trailing whitespace removed. The function also prints a query string to the standard output in the format '? a b c d' (where a, b, c, and d are non-negative integers less than the number of elements in the secret sequence p) and waits for the user's response.

#State of the program right berfore the function call: a and b are non-negative integers such that 0 <= a, b < n, where n is the length of the secret sequence p.
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where a and b are non-negative integers less than the length of the secret sequence p)
    sys.stdout.flush()

#Overall this is what the function does:Prints the values of two non-negative integers a and b, which are less than the length of a secret sequence p, to the standard output in the format "! [a] [b]" and then flushes the output buffer to ensure the output is displayed immediately.

#State of the program right berfore the function call: n is a positive integer greater than 1.
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns nothing, as there is no return statement with a value. The function func_2 has been called with arguments 0 and 1, but its return value is not used. The variable n is an integer larger than 0 and equals 2, but it is not used in the code snippet.
    #State: *`n` is an integer larger than 0, `n` is not equal to 2, stdin contains no input
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: Output State: `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `n` is unchanged and still larger than 0 and not equal to 2, stdin still contains no input.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: Output State: `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `n` is unchanged and still larger than 0 and not equal to 2, `min_indices` is a list containing all indices `i` for which `func_1(max_index, min_indices[0], max_index, i)` returns '=' or '<', stdin still contains no input.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: Output State: `min_index` is the smallest index `i` for which `func_1(max_index, min_indices[0], max_index, i)` returns '=' or '<', `min_indices` is a list containing all indices `i` for which `func_1(max_index, min_indices[0], max_index, i)` returns '=' or '<', `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `n` is unchanged and still larger than 0 and not equal to 2, stdin still contains no input.
    func_2(max_index, min_index)

#Overall this is what the function does:This function determines the maximum and minimum indices based on the results of the `func_1` function, and then calls the `func_2` function with these indices. If the input `n` is 2, it directly calls `func_2` with arguments 0 and 1. The function does not return any value.

