#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret sequence p.
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are integers within the range [0, n), where n is the length of the secret sequence p)
    sys.stdout.flush()
    return input().strip()
    #The program returns a string that is the user's input, which is expected to be a guess of the secret sequence p, and this input string has been stripped of any leading or trailing whitespace.

#Overall this is what the function does:The function prompts the user to guess a secret sequence by printing a query with four indices (a, b, c, and d) and returns the user's input as a stripped string, which is expected to be a guess of the secret sequence.

#State of the program right berfore the function call: a and b are non-negative integers such that 0 <= a < n and 0 <= b < n, where n is the number of elements in the secret sequence p.
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where a and b are non-negative integers less than n)
    sys.stdout.flush()

#Overall this is what the function does:Prints the values of two non-negative integers, a and b, to the console, separated by a space, and flushes the output buffer to ensure the output is displayed immediately.

#State of the program right berfore the function call: n is a positive integer greater than or equal to 2.
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns nothing, as there is no value or expression specified in the return statement. The value of `n` remains 2, and the function `func_2` has been called with arguments 0 and 1, but its return value is not used. Stdin remains empty.
    #State: *`n` is an integer larger than 0, stdin contains no input, and `n` is not equal to 2
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: `n` is an integer larger than 0 and not equal to 2, `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `i` is `n-1`, `res` is the value returned by `func_1(0, max_index, 0, n-1)`, and stdin contains no input.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: `n` is an integer larger than 0 and not equal to 2, `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `i` is `n-1`, `res` is the value returned by `func_1(max_index, min_indices[0], max_index, n-1)`, `min_indices` is a list containing either `n-1` or `max_index` or both `n-1` and `max_index` depending on the value of `res` which was returned by `func_1(max_index, max_index, max_index, 0)`, and stdin contains no input.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: Output State: **`n` is an integer larger than 0 and not equal to 2, `max_index` is the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `min_indices` is a list containing either `n-1` or `max_index` or both `n-1` and `max_index` depending on the value of `res` which was returned by `func_1(max_index, max_index, max_index, 0)`, `min_index` is the last element of `min_indices` which is either `n-1` or `max_index` or both `n-1` and `max_index` depending on the value of `res` which was returned by `func_1(max_index, max_index, max_index, 0)`, and `res` is the return value of `func_1(min_index, min_index, min_index, min_index)`.
    #
    #In natural language, the output state after the loop executes all the iterations is that `n` remains an integer larger than 0 and not equal to 2, `max_index` remains the largest index `i` for which `func_1(0, max_index, 0, i)` returns '<', `min_indices` remains a list containing either `n-1` or `max_index` or both `n-1` and `max_index` depending on the value of `res` which was returned by `func_1(max_index, max_index, max_index, 0)`, `min_index` is updated to the last element of `min_indices` which is either `n-1` or `max_index` or both `n-1` and `max_index` depending on the value of `res` which was returned by `func_1(max_index, max_index, max_index, 0)`, and `res` is updated to the return value of `func_1(min_index, min_index, min_index, min_index)`.
    func_2(max_index, min_index)

#Overall this is what the function does:This function takes an integer n as input, where n is greater than or equal to 2. If n is 2, it calls the function func_2 with arguments 0 and 1 and returns without any output. If n is greater than 2, it finds the maximum index i for which func_1(0, max_index, 0, i) returns '<', then finds the minimum index i for which func_1(max_index, min_indices[0], max_index, i) returns '=' or '<', and finally calls func_2 with the maximum and minimum indices. The function does not return any value and does not modify the input variable n.

