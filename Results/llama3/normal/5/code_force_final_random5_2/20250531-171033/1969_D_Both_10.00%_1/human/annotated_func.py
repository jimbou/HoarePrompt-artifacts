#State of the program right berfore the function call: stdin contains one input: an integer
    return int(putin())
    #The program returns an integer that was input from stdin.

#Overall this is what the function does:The function reads an integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, putin().split())
    #The program returns a map object that contains a sequence of integers, which are the result of converting each space-separated integer from the input list in stdin to an integer.

#Overall this is what the function does:Converts a space-separated list of integers from standard input into a map object containing a sequence of integers.

#State of the program right berfore the function call: main_ar and sec_arr are lists of pairs of integers, where each pair represents the prices of an item for Alice and Bob, respectively.
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: `main_ar` is a list of pairs of integers, `sec_arr` is an empty list, `sub_summ` is equal to the sum of the first elements of all pairs of integers in the initial list `sec_arr`, `val_a` is the last pair of integers in the initial list `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: `main_ar` is a list of pairs of integers, `sec_arr` is an empty list, `val_a` is the last pair of integers in the list `main_ar`, `sub_summ` is equal to the sum of the first elements of all pairs of integers in the initial list `main_ar` plus the sum of all pairs of integers in the list `main_ar` that have a sum greater than or equal to 0.
    return sub_summ
    #The program returns the sum of the first elements of all pairs of integers in the initial list `main_ar` plus the sum of all pairs of integers in the list `main_ar` that have a sum greater than or equal to 0.

#Overall this is what the function does:This function calculates and returns the sum of the first elements of all pairs of integers in the input list `main_ar`, plus the sum of all pairs of integers in `main_ar` that have a total value greater than or equal to 0. It does not modify the input lists `main_ar` and `sec_arr`, but it does empty `sec_arr` and uses its initial values to calculate a partial sum. The function effectively ignores the values in `sec_arr` after emptying it, and focuses solely on the pairs in `main_ar` for its final calculation.

