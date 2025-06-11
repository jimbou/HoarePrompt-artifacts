#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the number of elements in the secret sequence p.
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: a string containing a query with the values of a, b, c, and d (where a, b, c, and d are non-negative integers less than n)
    return input()
    #The program returns a string that is the user's input, which is a query with the values of a, b, c, and d, where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, and n is the number of elements in the secret sequence p.

#Overall this is what the function does:The function sends a query to the user with four non-negative integers (a, b, c, d) less than the number of elements in a secret sequence p, and returns the user's input as a string.

#State of the program right berfore the function call: n is a positive integer greater than 1, func_1 is a function that takes four non-negative integers less than n as input and returns a string that is either '<', '>', or '='.
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `n` is a positive integer greater than 1, `i` is `n-1`, `func_1` is a function that takes four non-negative integers less than `n` as input and returns a string that is either '<', '>', or '=', `max_item_idx` is `n-1` if `ans` is '<', otherwise `max_item_idx` is a value between 0 and `n-2`, and `ans` is either '<', '>', or '=' and equals to `func_1(max_item_idx, max_item_idx, n-1, n-1)`
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: `n` is a positive integer greater than 1, `i` is `n-1`, `func_1` is a function that takes four non-negative integers less than `n` as input and returns a string that is either '<', '>', or '=', `max_item_idx` is `n-1` if `ans` is '<', otherwise `max_item_idx` is a value between 0 and `n-2`, `ans` is either '<', '>', or '=' and equals to `func_1(max_item_idx, max_item_idx, n-1, n-1)`, `ans1` is either '<', '>', or '=' and equals to `func_1(max_item_idx, pair_idx, max_item_idx, i)`, `ans2` is either '<', '>', or '=' and equals to `func_1(pair_idx, pair_idx, i, i)` if `ans1` is '=', otherwise `ans2` is either '<', '>', or '=' and equals to `func_1(max_item_idx, max_item_idx, 0, 0)` if `ans1` is '>', otherwise `ans2` is not defined. If `ans1` is '<', then `pair_idx` is `n-1`. If `ans1` is '=', then `ans2` is either '<', '>', or '=' and if `ans2` is '>', then `pair_idx` is `n-1`. Otherwise, `pair_idx` can be any value between 0 and `n-1` or `max_item_idx`.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx] (where max_item_idx is either n-1 or a value between 0 and n-2, and pair_idx is either n-1 or a value between 0 and n-1 or max_item_idx)

#Overall this is what the function does:This function finds the maximum item index and its pair index based on the comparison results from the input function `func_1`. It iterates through the range of `n` to find the maximum item index and then finds its pair index by comparing with other items. The function prints the maximum item index and its pair index. The maximum item index can be either `n-1` or a value between 0 and `n-2`, and the pair index can be either `n-1` or a value between 0 and `n-1` or the maximum item index.

