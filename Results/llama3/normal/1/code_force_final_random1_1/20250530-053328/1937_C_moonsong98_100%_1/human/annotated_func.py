#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret sequence p.
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are integers such that 0 <= a, b, c, d < n)
    sys.stdout.flush()
    return input().strip()
    #The program returns a string that is the user's response to the message "? a b c d" where a, b, c, and d are integers such that 0 <= a, b, c, d < n, and n is the length of the secret sequence p.

#Overall this is what the function does:The function prints a message to the user in the format "? a b c d" where a, b, c, and d are integers, and then returns the user's response as a string.

#State of the program right berfore the function call: a and b are non-negative integers such that 0 <= a < n and 0 <= b < n, where n is the number of elements in the secret sequence p.
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where a and b are non-negative integers less than n, the number of elements in the secret sequence p)
    sys.stdout.flush()

#Overall this is what the function does:Prints the values of two non-negative integers a and b, less than the number of elements in a secret sequence p, to the standard output, followed by a flush operation to ensure the output is displayed immediately.

#State of the program right berfore the function call: n is a positive integer greater than 1.
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns nothing, as the return statement is empty. The value of `n` remains 2, and the function `func_2` has been called with arguments 0 and 1, but its return value is not used.
    #State: *`n` is an integer larger than 0, `n` is not equal to 2, stdin contains no input.
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: `n` is an integer larger than 0, `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `i` is `n-1`, `res` is the value returned by `func_1(0, max_index, 0, n-1)`.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: `n` is an integer larger than 0, `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `i` is `n-1`, `res` is the result of `func_1(max_index, min_indices[0], max_index, n-1)`, `min_indices` is a list containing all indices `i` for which `func_1(max_index, min_indices[0], max_index, i)` returns '<' or '='.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: `n` is an integer larger than 0, `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `res` is the result of `func_1(min_index, min_index, min_index, i)`, `min_index` is equal to `i` if `res` equals '=', `min_indices` is a list containing all indices `i` for which `func_1(max_index, min_indices[0], max_index, i)` returns '<' or '=', and `min_indices` must be empty.
    func_2(max_index, min_index)

#Overall this is what the function does:This function determines the maximum and minimum indices based on the results of the `func_1` function and then calls the `func_2` function with these indices. If the input `n` is 2, it directly calls `func_2` with arguments 0 and 1. Otherwise, it iterates through the range of `n` to find the maximum index where `func_1` returns '<', and then finds the minimum index where `func_1` returns '<' or '='. If multiple minimum indices are found, it selects the one that returns '=' when compared to itself. Finally, it calls `func_2` with the maximum and minimum indices. The function does not return any value.

