#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret sequence p.
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? a b c d (where a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret sequence p)
    return input()
    #The program returns a string that is an input from the user, which is expected to be a response to the printed string "? a b c d", where a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret sequence p.

#Overall this is what the function does:The function takes four integers a, b, c, and d as input, prints a string in the format "? a b c d" to the console, and returns a string input from the user in response to the printed string.

#State of the program right berfore the function call: n is a positive integer greater than 1, func_1 is a function that takes four non-negative integers less than n and returns a string that is either "<", "=", or ">".
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `n` is a positive integer greater than 1, `func_1` is a function that takes four non-negative integers less than `n` and returns a string that is either "<", "=", or ">", `max_item_idx` is the index of the maximum item found so far, `i` is `n-1`, and `ans` is the result of `func_1(max_item_idx, max_item_idx, i, i)`
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: `n` is a positive integer greater than 1, `func_1` is a function that takes four non-negative integers less than `n` and returns a string that is either "<", "=", or ">", `max_item_idx` is the index of the maximum item found so far, `i` is `n-1`, `ans` is the result of `func_1(max_item_idx, max_item_idx, i, i)`, and `pair_idx` is the index of the maximum item found so far.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [n-1] [n-1] (where n-1 is the index of the maximum item found so far)

#Overall this is what the function does:This function finds the index of the maximum item in a set of n items, where n is a positive integer greater than 1. It uses a comparison function `func_1` to compare items and determine the maximum. The function first finds the index of the maximum item by comparing each item with the current maximum. Then, it finds the index of the second maximum item by comparing each item with the current maximum and the second maximum. Finally, it prints the indices of the maximum and second maximum items.

