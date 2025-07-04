#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the secret permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? a b c d (where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n)
    return input()
    #The program returns the input provided to it, which is the string '? a b c d' where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, and n is the length of the secret permutation p.
#Overall this is what the function does:The function accepts four non-negative integer parameters `a`, `b`, `c`, and `d`, each less than `n` (the length of a secret permutation `p`). It constructs and prints a string in the format '? a b c d' and then returns the input string provided to it, which is expected to be the same format.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `n` is an integer such that 2 <= n <= 10^4, `max_item_idx` is the largest index `i` in the range 1 to n-1 for which `func_1(max_item_idx, max_item_idx, i, i)` returns '<', or 0 if `func_1` never returns '<`.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: `n` is an integer such that 2 <= n <= 10^4, `max_item_idx` is the largest index `i` in the range 1 to n-1 for which `func_1(max_item_idx, max_item_idx, i, i)` returns '<', or 0 if `func_1` never returns '<', and `pair_idx` is the index `i` in the range 0 to n-1 for which `func_1(max_item_idx, pair_idx, max_item_idx, i)` returns '<' for the first time, or if no such `i` exists, it is the index `i` for which `func_1(pair_idx, pair_idx, i, i)` returns '>' for the first time after an '=' result.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx] (where max_item_idx is the largest index i in the range 1 to n-1 for which func_1(max_item_idx, max_item_idx, i, i) returns '<', or 0 if no such index exists, and pair_idx is the index i in the range 0 to n-1 for which func_1(max_item_idx, pair_idx, max_item_idx, i) returns '<' for the first time, or the index i for which func_1(pair_idx, pair_idx, i, i) returns '>' for the first time after a '=' result if no such '<' result exists)
#Overall this is what the function does:The function accepts an integer `n` within the range of 2 to 10,000. It determines two indices, `max_item_idx` and `pair_idx`, based on the results of the function `func_1` called with different parameters. It prints these indices in the format `! [max_item_idx] [pair_idx]`. The indices are determined by specific comparison results returned by `func_1`.

