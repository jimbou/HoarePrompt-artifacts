#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the secret sequence p.
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are the values of the variables a, b, c, and d respectively)
    return input()
    #The program returns a string that is an input from the user, which is expected to be a sequence of characters in the format '? a b c d' where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the secret sequence p.

#Overall this is what the function does:Sends a query to the user with four non-negative integers a, b, c, and d, and returns the user's response as a string in the format '? a b c d', where a, b, c, and d are non-negative integers less than the length of a secret sequence p.

#State of the program right berfore the function call: n is a positive integer greater than 1, func_1 is a function that takes four non-negative integers less than n and returns a string that can be '<', '=', or '>'.
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: Output State: `max_item_idx` is the index of the maximum item in the range `[0, n)`, `n` is unchanged, `func_1` is unchanged.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: Output State: `max_item_idx` is the index of the maximum item in the range `[0, n)`, `pair_idx` is the index of the maximum item in the range `[0, n)`, `n` is unchanged, `func_1` is unchanged.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx] (where max_item_idx is the index of the maximum item in the range [0, n) and pair_idx is the index of the maximum item in the range [0, n))

#Overall this is what the function does:This function finds the index of the maximum item in the range [0, n) using a comparison function func_1, and then finds another index of the maximum item in the same range. It prints the indices of these two maximum items.

