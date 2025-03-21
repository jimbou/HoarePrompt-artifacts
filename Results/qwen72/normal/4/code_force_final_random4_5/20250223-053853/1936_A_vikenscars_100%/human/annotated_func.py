#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: '? a b c d' (where a, b, c, and d are specific integer values such that 0 <= a, b, c, d < n)
    return input()
    #The program returns the string 'request' which is formatted as '? a b c d', where a, b, c, and d are specific integer values such that 0 <= a, b, c, d < n, and n is the length of the permutation p.
#Overall this is what the function does:The function `func_1` accepts four integer parameters `a`, `b`, `c`, and `d`, each of which must be between 0 and n-1, where n is the length of the permutation p. It prints a query string formatted as '? a b c d' to the console and then returns the user's input as a string. The final state of the program after the function concludes is that the input values `a`, `b`, `c`, and `d` remain unchanged, and the function returns a string that represents the user's response to the printed query.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4, and max_item_idx and pair_idx are integers in the range [0, n-1].
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: max_item_idx is the index of the maximum item in the range [0, n-1] as determined by the comparison function `func_1`. pair_idx remains unchanged.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: pair_idx is the index of the last item in the range [0, n-1] that is equal to or greater than the maximum item as determined by `func_1`.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx] (where [max_item_idx] is the index of the maximum item as determined by `func_1`, and [pair_idx] is the index of the last item in the range [0, n-1] that is equal to or greater than the maximum item)
#Overall this is what the function does:The function `func_2` accepts an integer `n` such that 2 <= n <= 10^4. It determines the index of the maximum item (`max_item_idx`) and the index of the last item (`pair_idx`) in the range [0, n-1] that is equal to or greater than the maximum item, as determined by the comparison function `func_1`. The function then prints the indices in the format `! [max_item_idx] [pair_idx]`. After the function concludes, `max_item_idx` is the index of the maximum item, and `pair_idx` is the index of the last item that is equal to or greater than the maximum item.

