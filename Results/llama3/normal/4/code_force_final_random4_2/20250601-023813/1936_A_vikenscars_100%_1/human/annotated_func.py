#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret sequence p.
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are integers within the range 0 <= a, b, c, d < n)
    return input()
    #The program returns a string that is the input provided by the user, which is expected to be a response to the printed string "? [a] [b] [c] [d]", where a, b, c, and d are integers such that 0 <= a, b, c, d < n, and n is the length of the secret sequence p.

#Overall this is what the function does:The function takes four integers a, b, c, and d as input, prints a string in the format "? [a] [b] [c] [d]" to the console, and returns a string that is the user's response to the printed string.

#State of the program right berfore the function call: n is a positive integer, func_1 is a function that takes four non-negative integers less than n as arguments and returns a string that is either '<', '=', or '>'.
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `i` is `n-1`, `max_item_idx` is the index of the maximum value that `func_1` returns '<' for, and `n` is unchanged.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: `i` is `n-1`, `max_item_idx` is the index of the maximum value that `func_1` returns '<' for, `n` is unchanged, and `pair_idx` is the index of the maximum value that `func_1` returns '<' for.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! <index> <index> (where <index> is the index of the maximum value that func_1 returns '<' for)

#Overall this is what the function does:Finds the index of the maximum value that a given function `func_1` returns '<' for, and prints the index of this maximum value along with the index of the maximum value that `func_1` returns '<' for, considering all possible pairs of indices.

