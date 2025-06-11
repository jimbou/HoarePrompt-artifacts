#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    return int(putin())
    #The program returns an integer that is greater than 0

#Overall this is what the function does:Reads an integer from standard input and returns it, ensuring the returned value is greater than 0.

#State of the program right berfore the function call: putin() returns a string of space-separated integers.
    return map(int, putin().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a result of converting a string of space-separated integers returned by the putin() function into an integer.

#Overall this is what the function does:The function accepts no parameters and returns a map object containing a sequence of integers. It takes a string of space-separated integers as input, splits it into individual strings, converts each string into an integer, and returns the resulting sequence of integers.

#State of the program right berfore the function call: main_ar and sec_arr are lists of pairs of integers, where each pair represents the prices of an item for Alice and Bob, respectively.
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: `main_ar` is a list of pairs of integers, `sec_arr` is an empty list, `sub_summ` is equal to the sum of the first elements of all pairs in the initial `sec_arr`, `val_a` is the last pair in the initial `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: `main_ar` is an empty list, `sec_arr` is an empty list, `sub_summ` is equal to the sum of the first elements of all pairs in the initial `sec_arr` plus the sum of the elements of all pairs in the initial `main_ar` where the sum of the elements of each pair is greater than or equal to 0, `val_a` is the last pair in the initial `sec_arr`, `val_b` is the last pair in the initial `main_ar`.
    return sub_summ
    #The program returns the sum of the first elements of all pairs in the initial `sec_arr` plus the sum of the elements of all pairs in the initial `main_ar` where the sum of the elements of each pair is greater than or equal to 0. Since both `main_ar` and `sec_arr` are empty lists, the sum of the first elements of all pairs in `sec_arr` is 0 and the sum of the elements of all pairs in `main_ar` where the sum of the elements of each pair is greater than or equal to 0 is also 0. Therefore, the program returns 0.

#Overall this is what the function does:This function calculates and returns the sum of the first elements of all pairs in the input list `sec_arr` and the sum of the elements of all pairs in the input list `main_ar` where the sum of the elements of each pair is greater than or equal to 0. The function consumes both input lists, leaving them empty.

