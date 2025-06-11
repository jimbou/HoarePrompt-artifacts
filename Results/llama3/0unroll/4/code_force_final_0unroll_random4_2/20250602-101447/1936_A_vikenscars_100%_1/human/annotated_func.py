#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the number of elements in the secret sequence p.
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are the values of the variables a, b, c, and d respectively)
    return input()
    #The program returns a string that is the input provided by the user, which is expected to be a guess of the secret sequence p, where the input is in the format '? a b c d' and a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the number of elements in the secret sequence p.

#Overall this is what the function does:The function takes four integers a, b, c, and d as input, prints a request string in the format '? a b c d', and returns a string input provided by the user, which is expected to be a guess of a secret sequence p in the format '? a b c d', where a, b, c, and d are integers within the bounds of the secret sequence p.

#State of the program right berfore the function call: n is a positive integer greater than 1, and func_1 is a function that takes four indices a, b, c, d and returns a string '<', '=', or '>' based on the comparison of (p_a | p_b) and (p_c | p_d) where p is a permutation of integers from 0 to n-1.
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: Output State: `max_item_idx` is the index of the maximum value in the permutation `p` where `p` is a permutation of integers from 0 to `n-1`.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: Output State: `max_item_idx` is the index of the maximum value in the permutation `p` where `p` is a permutation of integers from 0 to `n-1`, `pair_idx` is the index of the maximum value in the permutation `p` where `p` is a permutation of integers from 0 to `n-1`.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! n-1 n-1 (where n is the length of the permutation p)

#Overall this is what the function does:This function finds the index of the maximum value in a permutation of integers from 0 to n-1 and prints it along with its pair index. The function iterates through the permutation to find the maximum value and its pair, and then prints the indices of these values. The function assumes that the permutation is represented by a function `func_1` that compares pairs of indices and returns a string '<', '=', or '>' based on the comparison. The function prints the indices of the maximum value and its pair in the format '! max_item_idx pair_idx'.

