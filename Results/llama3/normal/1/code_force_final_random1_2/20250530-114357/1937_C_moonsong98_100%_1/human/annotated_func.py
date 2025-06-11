#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the number of elements in the secret sequence p.
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are non-negative integers less than the number of elements in the secret sequence p)
    sys.stdout.flush()
    return input().strip()
    #The program returns a string that is the user's input, which is a response to the printed string "? a b c d" where a, b, c, and d are non-negative integers less than the number of elements in the secret sequence p.

#Overall this is what the function does:The function prints a string in the format "? a b c d" where a, b, c, and d are non-negative integers less than the number of elements in the secret sequence p, waits for user input, and returns the user's input as a string.

#State of the program right berfore the function call: a and b are non-negative integers such that 0 <= a, b < n, where n is the number of elements in the secret sequence p.
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where a and b are non-negative integers less than n)
    sys.stdout.flush()

#Overall this is what the function does:Prints the values of two non-negative integers a and b, which are less than the number of elements in a secret sequence p, to the standard output, followed by a flush operation to ensure the output is displayed immediately.

#State of the program right berfore the function call: n is a positive integer greater than or equal to 2.
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
        
    #State: `n` is an integer larger than 0, `n` is not equal to 2, `i` is `n-1`, `res` is the return value of `func_1(0, max_index, 0, n-1)`, and `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<'.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: `n` is an integer larger than 0, `n` is not equal to 2, `i` is `n-1`, `res` is the return value of `func_1(max_index, min_indices[0], max_index, n-1)`, `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', and `min_indices` is a list containing either `n-1`, or `max_index` and `n-1`, or `max_index`.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: `n` is an integer larger than 0, `n` is not equal to 2, `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `min_indices` is a list containing either `n-1`, or `max_index` and `n-1`, or `max_index`, `min_index` is the smallest index in `min_indices`, `res` is the result of `func_1(min_index, min_index, min_index, min_index)`, and `i` is the last element in the list `min_indices`.
    func_2(max_index, min_index)

#Overall this is what the function does:This function takes a positive integer n as input, where n is greater than or equal to 2. It then performs a series of operations using two external functions, func_1 and func_2. If n is 2, the function calls func_2 with arguments 0 and 1 and returns without any output. If n is greater than 2, the function iteratively finds the maximum index i for which func_1 returns '<', and then finds the minimum index i for which func_1 returns '=' or '<' with respect to the maximum index. Finally, it calls func_2 with the maximum and minimum indices as arguments, but does not return any value.

