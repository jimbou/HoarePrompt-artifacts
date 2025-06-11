#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the number of elements in the secret sequence p.
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n)
    return input()
    #The program returns a string that contains the values of a, b, c, and d in the format '? a b c d', where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, and n is the number of elements in the secret sequence p.

#Overall this is what the function does:Sends a query with four non-negative integers (a, b, c, d) to a secret sequence p and returns a string containing the values of a, b, c, and d in the format '? a b c d'.

#State of the program right berfore the function call: n is a positive integer greater than 1, func_1 is a function that takes four non-negative integers less than n and returns a string that is either '<', '=', or '>', and the function func_1 is correctly implemented to compare the bitwise OR of two pairs of elements from a secret sequence p.
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: Output State: `max_item_idx` is the index of the maximum item in the range `[0, n)` as determined by `func_1`, `n` remains unchanged, `func_1` remains unchanged.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: Output State: `pair_idx` is the index of the maximum item in the range `[0, n)` as determined by `func_1`, `max_item_idx` remains unchanged, `n` remains unchanged, `func_1` remains unchanged.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [the index of the maximum item in the range [0, n) as determined by func_1]

#Overall this is what the function does:This function determines the index of the maximum item in a secret sequence p using a comparison function func_1, and then finds the index of the maximum item in the range [0, n) as determined by func_1. It prints the indices of these two maximum items. The function takes no parameters and returns no value, but it modifies the external state by printing the result. The function assumes that n is a positive integer greater than 1, and func_1 is a correctly implemented comparison function.

